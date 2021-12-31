import logging
import sys
from tqdm import tqdm

log_file = "./log_please_delete.txt"

logger = logging.getLogger()
# here
logger.setLevel(logging.INFO)
fmt = logging.Formatter("%(asctime)s: [ %(message)s ]", "%m/%d/%Y %I:%M:%S %p")
handler = logging.StreamHandler()
handler.setFormatter(fmt)

logfile = logging.FileHandler(log_file, "w")
logfile.setFormatter(fmt)
logger.addHandler(logfile)

handler.setLevel(logging.INFO)
logger.addHandler(handler)
logger.info("COMMAND: %s" % " ".join(sys.argv))


for i in tqdm(range(10)):
    print(i)
    logging.info("my_info")
    
