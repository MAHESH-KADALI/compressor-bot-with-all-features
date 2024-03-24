from subprocess import run as srun
import logging
from os import path as ospath

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)

UPSTREAM_REPO = 'https://github.com/MAHESH-KADALI/compressor-bot-with-all-features'
UPSTREAM_BRANCH = 'master'
