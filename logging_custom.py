import sys
import logging

logging.basicConfig(level=logging.DEBUG, filename="timelapse-tool.log")

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

def get_logger(name: str):
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    return logger

