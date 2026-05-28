import logging
from functools import wraps
from datetime import datetime
from selenium.webdriver.remote.webdriver import WebDriver

logging.basicConfig(filename='logs/test_execution.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',filemode='a',force=True)
def automation_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        test_name = func.__name__
        logging.info(f"Starting test: {test_name}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Test {test_name} completed successfully")
            return result
        except Exception as e:
            logging.error(f"Test {test_name} failed with error: {e}")
            raise 
        finally:
            logging.info(f"Finished test: {test_name}")
    return wrapper