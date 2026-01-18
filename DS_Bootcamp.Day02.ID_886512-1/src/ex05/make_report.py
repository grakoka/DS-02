import sys
from analytics import Research
from config import num_of_steps, report_template


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 make_report.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        research = Research(file_path)
        data = research.file_reader()

        analytics = Research.Analytics(data)
        heads, tails = analytics.counts()
        head_frac, tail_frac = analytics.fractions(heads, tails)

        predictions = analytics.predict_random(num_of_steps)
        predicted_heads = sum(p[0] for p in predictions)
        predicted_tails = sum(p[1] for p in predictions)

        report = report_template.format(
            total=len(data),
            tails=tails,
            heads=heads,
            tail_percent=tail_frac,
            head_percent=head_frac,
            steps=num_of_steps,
            predicted_tails=predicted_tails,
            predicted_heads=predicted_heads,
        )

        print(report)

        analytics.save_file(report, "report", "txt")
        print("Report saved to 'report.txt'.")

    except Exception as e:
        print(f"Error: {e}")
