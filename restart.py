from subprocess import run as srun
import logging
from os import path as ospath
from sys import executable
from os import execl as osexecl

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
                    level=logging.INFO)

UPSTREAM_REPO = 'https://github.com/MAHESH-KADALI/compressor-bot-with-all-features'
UPSTREAM_BRANCH = 'main'

if UPSTREAM_REPO is not None:
    if ospath.exists('.git'):
        srun(["rm", "-rf", ".git"])

    update = srun([f"git init -q \
                     && git add . \
                     && git commit -sm update -q \
                     && git remote add origin {UPSTREAM_REPO} \
                     && git fetch origin -q \
                     && git reset --hard origin/{UPSTREAM_BRANCH} -q"], shell=True)

    if update.returncode == 0:
        logging.info('Successfully upgraded with latest commit from UPSTREAM_REPO')
        osexecl(executable, executable, "-m", "BindhuEncoder")
    else:
        logging.error('Something went wrong while upgrading, check UPSTREAM_REPO if valid or not!')

osexecl(executable, executable, "-m", "BindhuEncoder")
