import logging
from datetime import datetime

LOGFILE = 'csnova.log'

def setup_logging():
    logging.basicConfig(
        filename=LOGFILE,
        filemode='w',
        level=logging.INFO,
        format='%(message)s'
    )

def log_header():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"# Logging: {now}\n## result: no errors\n### --------------------------------")

def log_section(section):
    logging.info(f"\n## {section}")

def log_subsection(subsection):
    logging.info(f"### {subsection}")

def log_info(message):
    logging.info(f"Info: {message}")

def log_error(message):
    logging.info(f"Error: {message}")