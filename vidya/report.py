"""Q55(b): Command-line reports using argparse."""

import argparse
import csv
import json


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Generate a VIDYA student marks report."
    )

    parser.add_argument(
        "--file",
        default="data/marks.csv",
        help="Path to the CSV marks file (default: data/marks.csv)",
    )

    parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Number of top records to display (default: 5)",
    )

    parser.add_argument(
        "--subject",
        default="Python",
        help="Subject column to rank students by (default: Python)",
    )

    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format: text or json (default: text)",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Display additional report information",
    )

    return parser.parse_args()


def main():
    args = parse_arguments()

    if args.top < 1:
        print("Error: --top must be at least 1.")
        return

    try:
        with open(args.file, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            records = list(reader)
            columns = reader.fieldnames or []

    except FileNotFoundError:
        print(f"Error: File not found: {args.file}")
        return

    except PermissionError:
        print(f"Error: Permission denied: {args.file}")
        return

    # Find the requested subject column without case sensitivity.
    subject_column = next(
        (column for column in columns
         if column.lower() == args.subject.lower()),
        None,
    )

    if subject_column is None:
        print(
            f"Error: Subject '{args.subject}' not found. "
            "Available subjects: "
            + ", ".join(
                column for column in columns
                if column.lower() in ("python", "dbms", "statistics")
            )
        )
        return

    try:
        records.sort(
            key=lambda record: float(record[subject_column]),
            reverse=True,
        )
    except (ValueError, TypeError):
        print(f"Error: Values in '{subject_column}' must be numeric.")
        return

    top_records = records[:args.top]

    if args.verbose:
        print("VIDYA report settings:")
        print("File:", args.file)
        print("Top records:", args.top)
        print("Subject:", subject_column)
        print("Format:", args.format)

    if args.format == "json":
        print(json.dumps(top_records, indent=4))
    else:
        print(f"VIDYA Report — Subject: {subject_column}")
        print(f"File: {args.file}")
        print(f"Records shown: {len(top_records)}")

        for rank, record in enumerate(top_records, start=1):
            print(
                f"{rank}. {record.get('name', 'Unknown')} — "
                f"{subject_column}: {record[subject_column]}"
            )

    if args.verbose:
        print("Total matching records:", len(records))


if __name__ == "__main__":
    main()
