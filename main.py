from loguru import logger

from modules.executor import main_executor
from tools.other.add_logger import add_logger
from tools.other.sleep import sleep_in_range
from user_data.config import sleep_between_loops

if __name__ == '__main__':
    add_logger()
    try:
        while True:
            try:
                main_executor()
                sleep_in_range(
                    sec_from=sleep_between_loops[0],
                    sec_to=sleep_between_loops[1],
                    log="sleep between loops"
                )
            except Exception as e:
                logger.exception(e)
    except KeyboardInterrupt:
        exit()
