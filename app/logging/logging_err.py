import logging
import logging.config
import yaml
import os


class Logger():
    __instance = None

    @staticmethod
    def inst():
        if Logger.__instance == None:
            Logger.__instance = Logger()
        return Logger.__instance

    def __init__(self):
        with open(os.path.join('logging', 'config.yaml'), 'r') as f:
            log_cfg = yaml.safe_load(f.read())
            logging.config.dictConfig(log_cfg)


    def message_error(self, err):
        logger = logging.getLogger('err')
        # logger.setLevel(logging.INFO)
        logger.error(err)


    def message_info(self, mess):
        logger = logging.getLogger('info')

        logger.info(mess)
        return mess

    def message_debug(self, mess):
        logger = logging.getLogger('debug')
        logger.info(mess)
