from loguru import logger

from modules.executor import main_executor
from tools.other.add_logger import add_logger

if __name__ == '__main__':
    add_logger()
    try:
        while True:
            try:
                main_executor()
            except Exception as e:
                logger.exception(e)
    except KeyboardInterrupt:
        exit()
