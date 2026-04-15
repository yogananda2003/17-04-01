import argparse
import re
import subprocess
import sys
from collections import Counter


DEFAULT_AI_AUTHORS = {
    "cursor",
    "copilot",
    "chatgpt",
    "claude",
    "gemini",
    "ai",
}


def run_command(command):
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def parse_ai_acceptance(stats_output):
    match = re.search(r"(\d+)%\s+AI code accepted", stats_output, re.IGNORECASE)
    if not match:
        return None
    return int(match.group(1))


def parse_blame(blame_output):
    """
    Parse lines from `git ai blame` output.
    Expected line example:
    cdc399b9 (cursor 2026-04-15 14:12:01 +0530 1) def add(a, b):
    """
    counts = Counter()
    total_code_lines = 0

    for line in blame_output.splitlines():
        if not line.strip():
            continue
        match = re.match(r"^\S+\s+\((.+?)\s+\d{4}-\d{2}-\d{2}", line)
        if not match:
            continue
        author = match.group(1).strip()
        counts[author] += 1
        total_code_lines += 1

    return counts, total_code_lines


def main():
    parser = argparse.ArgumentParser(
        description="Check whether a file is likely AI-generated using git-ai."
    )
    parser.add_argument("file", help="Path to file to inspect")
    parser.add_argument(
        "--run-checkpoint",
        action="store_true",
        help="Run `git ai checkpoint` before checking",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=50,
        help="AI percentage threshold for verdict (default: 50)",
    )
    parser.add_argument(
        "--show-raw",
        action="store_true",
        help="Print raw git-ai outputs for troubleshooting",
    )
    args = parser.parse_args()

    rc, _, _ = run_command("git rev-parse --is-inside-work-tree")
    if rc != 0:
        print("Error: current directory is not a git repository.")
        sys.exit(2)

    if args.run_checkpoint:
        print("Running: git ai checkpoint ...")
        rc, out, err = run_command("git ai checkpoint")
        if out:
            print(out)
        if err:
            print(err, file=sys.stderr)
        if rc != 0:
            print("Warning: checkpoint command failed, continuing with available data.")

    rc, stats_out, stats_err = run_command("git ai stats")
    if rc != 0:
        print("Error: `git ai stats` failed.")
        if stats_err:
            print(stats_err, file=sys.stderr)
        sys.exit(2)

    blame_cmd = f"$env:GIT_PAGER='cat'; git ai blame {args.file}"
    rc, blame_out, blame_err = run_command(f'powershell -Command "{blame_cmd}"')
    if rc != 0:
        print(f"Error: `git ai blame {args.file}` failed.")
        if blame_err:
            print(blame_err, file=sys.stderr)
        sys.exit(2)

    ai_acceptance = parse_ai_acceptance(stats_out)
    author_counts, total_lines = parse_blame(blame_out)
    ai_line_count = sum(
        count
        for author, count in author_counts.items()
        if author.lower() in DEFAULT_AI_AUTHORS
    )
    ai_line_percent = (ai_line_count / total_lines * 100) if total_lines else 0.0

    print("\n=== AI Attribution Report ===")
    print(f"File: {args.file}")
    print(f"Total blamed lines: {total_lines}")
    print(f"AI-attributed lines: {ai_line_count} ({ai_line_percent:.1f}%)")
    if ai_acceptance is not None:
        print(f"Repository AI acceptance (git ai stats): {ai_acceptance}%")
    else:
        print("Repository AI acceptance (git ai stats): not detected")

    print("\nAuthor line breakdown:")
    if author_counts:
        for author, count in author_counts.most_common():
            print(f"- {author}: {count}")
    else:
        print("- No blame data parsed")

    likely_ai = ai_line_percent >= args.threshold
    verdict = "YES (likely AI-generated)" if likely_ai else "NO (likely human-written)"
    print(f"\nVerdict (threshold {args.threshold}%): {verdict}")

    if args.show_raw:
        print("\n--- Raw `git ai stats` ---")
        print(stats_out or "(empty)")
        print("\n--- Raw `git ai blame` ---")
        print(blame_out or "(empty)")


if __name__ == "__main__":
    main()
