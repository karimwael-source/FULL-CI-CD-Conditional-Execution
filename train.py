import argparse
import time
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Dummy training script for CI/CD assignment")
    parser.add_argument(
        "--fail",
        action="store_true",
        help="Force the training job to fail so you can test failure handling and artifact upload.",
    )
    args = parser.parse_args()

    print("Starting training pipeline...")
    print("Loading dataset...")
    time.sleep(1)
    print("Preprocessing data...")
    time.sleep(1)
    print("Training model on simulated GPU job...")
    time.sleep(1)

    if args.fail:
        print("ERROR: Simulated training failure happened.")
        raise RuntimeError("Forced failure for testing GitHub Actions artifact upload")

    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    model_file = output_dir / "model.txt"
    model_file.write_text("dummy model created successfully\n", encoding="utf-8")

    print("Training finished successfully.")
    print(f"Saved artifact to {model_file}")


if __name__ == "__main__":
    main()