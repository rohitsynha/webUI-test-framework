import logging


class LogGen:

    @staticmethod
    def loggen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(filename=".\\logs\\automation.log",
                            format='%(asctime)s: %(levelname)s:%(message)s',
                            datefmt='%m%d%Y %I:%M:%S %p',
                            level=logging.INFO)
        logger = logging.getLogger()
        return logger