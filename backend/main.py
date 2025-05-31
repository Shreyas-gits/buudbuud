import json
import logging

from upstox_client import HistoryV3Api
from helpers.logging_setup import setup_logging

setup_logging()

logger = logging.getLogger(__name__)

def main():
    try:
        with open('/home/shreyas/projects/project_buudbuud/backend/complete.json', 'r') as f:
            instrument_data = json.load(f)
            instrument_key_mapping = {item['instrument_key']: item for item in instrument_data}
            logger.info("Successfully loaded instrument data from 'complete.json'.")
    except FileNotFoundError:
        logger.error("Error: 'complete.json' not found. Make sure it's in the same directory as main.py.")
        instrument_key_mapping = None
    except json.JSONDecodeError:
        logger.error("Error: Could not decode JSON from 'complete.json'. Check if the file is valid JSON.")

    instrument_key = instrument_key_mapping["NSE_EQ|INE0NCC01015"]
    history = HistoryV3Api()
    ans = history.get_historical_candle_data1(instrument_key, "hours", "4", "2025-02-01", "2025-01-01")
    print(ans)

if __name__ == "__main__":
    main()



