from colorama import init, Fore
from pathlib import Path
from sys import platform
from datetime import datetime
from pathlib import Path
import re

elogfile = Path(Path(__file__).parents[1].resolve(), 'logs/error.log')
netlogfile = Path(Path(__file__).parents[1].resolve(), 'logs/network.log')
dlogfile = Path(Path(__file__).parents[1].resolve(), 'logs/debug.log')
regexReplacing = {}

def set_elogfile(file):
    global elogfile
    elogfile = Path(Path(__file__).parents[1].resolve(), file)

def set_dlogfile(file):
    global dlogfile
    dlogfile = Path(Path(__file__).parents[1].resolve(), file)

def set_netlogfile(file):
    global netlogfile
    netlogfile = Path(Path(__file__).parents[1].resolve(), file)

def eprint(text, log=False):
    logprint(Fore.RED + 'E: ', text, log)

def iprint(text, log=False):
    logprint(Fore.CYAN + 'I: ', text, log)

def wprint(text, log=False):
    logprint(Fore.YELLOW + 'W: ', text, log)

def okprint(text, log=False):
    logprint(Fore.GREEN + 'OK: ', text, log)

def logprint(prefix, text, log):
    text = str(text)
    prefix = str(prefix)
    print(prefix + text)
    if log == 'debug' or log == 'd':
        dlog(text)
    elif log == 'error' or log == 'e':
        elog(text)

def dlog(text):
    log(dlogfile, text)

def netlog(text):
    log(netlogfile, text)

def elog(text):
    log(elogfile, text)

def set_regex_replacing(regexes):
    global regexReplacing
    regexReplacing = regexes

def log(filename, text):
    text = str(text)
    current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    for regex in regexReplacing:
        text = re.sub(regex, regexReplacing[regex], text)
    text = '[' + current_time + '] ' + text + '\n'
    filename.parents[0].mkdir(exist_ok=True)
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)

init(autoreset=True)