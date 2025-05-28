import json
import logging
from upstox_client import HistoryV3Api

logger = logging.getLogger(__name__)

try:
    with open('complete.json', 'r') as f:
        instrument_key_mapping = json.load(f)
except FileNotFoundError:
    logger.error("Error: 'complete.json' not found. Make sure it's in the same directory as main.py.")
    instrument_key_mapping = None
except json.JSONDecodeError:
    logger.error("Error: Could not decode JSON from 'complete.json'. Check if the file is valid JSON.")
    instrument_key_mapping = None



