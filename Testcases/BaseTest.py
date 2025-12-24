
import logging


logging.basicConfig(filename='/Users/jaypatel/PycharmProjects/pythonProjectBH/logs/automation.log', format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', datefmt='%Y-%m-%d:%H:%M:%S', level=logging.INFO)
logger = logging.getLogger(__name__)