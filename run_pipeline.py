
import subprocess
import sys
import logging
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(
            LOG_DIR / "master_pipeline.log",
            encoding="utf-8"
        ),
        logging.StreamHandler()
    ],
    force=True
)

SCRIPTS = [
    "01_read_data.py",
    "02_data_quality.py",
    "06_clean_data_with_logging.py",
    "07_validate_data.py",
    "04_convert_parquet.py",
    "05_upload_to_s3.py"
]

def run_pipeline():
    start_time = datetime.now()

    logging.info("========== ETL PIPELINE STARTED ==========")

    for script in SCRIPTS:
        script_path = BASE_DIR / "scripts" / script

        logging.info(f"Running: {script}")

        try:
            subprocess.run(
                [sys.executable, str(script_path)],
                cwd=BASE_DIR,
                check=True
            )

            logging.info(f"SUCCESS: {script}")

        except subprocess.CalledProcessError:
            logging.exception(f"FAILED: {script}")
            logging.error("Pipeline stopped due to failure")
            sys.exit(1)

    duration = datetime.now() - start_time

    logging.info("========== ETL PIPELINE COMPLETED ==========")
    logging.info(f"Total execution time: {duration}")

if __name__ == "__main__":
    run_pipeline()
