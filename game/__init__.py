import logging
import os

logs_path = os.path.join(os.getcwd(), "artifacts/logs", "log")
logging.basicConfig(filename=f"{logs_path}.txt",
                    format='[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
print(logs_path)