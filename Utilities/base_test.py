import os
import json
from pathlib import Path
import pytest

from Utilities import logger_utils


@pytest.mark.usefixtures("setup", "actions_utils")
class BaseTest:
    ROOT_PATH = str(Path(__file__).parent.parent)
    CONSTANTS_PATH = ROOT_PATH+"/constants.json"
    CONSTANTS = None
    log = logger_utils.get_logger()

    def get_env_vars(self):
        self.log.info('Fetching environment variables')
        user = os.environ['user']
        pwd = os.environ['password']
        return user, pwd

    def get_env_value(self, param):
        self.log.info('Fetching environment variable '+ param)
        return os.environ[param]

    def get_data(self):
        self.log.info('Loading data from JSON file')
        config_file = open(self.CONSTANTS_PATH)
        self.CONSTANTS = json.load(config_file)
        return self.CONSTANTS
