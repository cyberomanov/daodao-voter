import random
import time

from loguru import logger


def sleep_in_range(sec_from: int, sec_to: int, log: str = None):
    sleep_time = random.randint(sec_from, sec_to)
    if log:
        logger.info(f"sleep {round(sleep_time, 2)} sec | {log}.")
    time.sleep(sleep_time)
