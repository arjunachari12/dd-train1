import logging
import json
import os
import traceback

class CustomJSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            'timestamp': self.formatTime(record),
            'level': record.levelname,
            'message': record.getMessage(),
            'service': 'my_python_app',  # Replace with your service name
            'environment': 'development',  # Optional: Add environment information
        }
        if record.exc_info:
            log_entry['exception'] = {
                'type': type(record.exc_info[1]).__name__,
                'message': str(record.exc_info[1]),
                'traceback': ''.join(traceback.format_exception(*record.exc_info))
            }
        return json.dumps(log_entry) + '\n'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create the log directory if it doesn't exist
log_dir = '/var/log/my_app'
os.makedirs(log_dir, exist_ok=True)

# Create a file handler to write logs to the JSON file
file_handler = logging.FileHandler(os.path.join(log_dir, 'application.json'), mode='a')
file_handler.setFormatter(CustomJSONFormatter())

logger.addHandler(file_handler)

# Example log messages
logger.info("This is an informational message")
logger.warning("A warning occurred")

# Generate 20 errors
for i in range(20):
    try:
        # Simulate an error
        raise ValueError(f"This is sample error number {i + 1} for logging")
    except ValueError as e:
        logger.exception(f"Caught an error: {e}")

# Additional logging to verify 
logger.info("End of logging example")
