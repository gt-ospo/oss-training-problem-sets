"""Utilities for second set of flag examples.
"""

import string
import sys
import time
from collections import Counter
from enum import Enum
from pathlib import Path

DownloadStatus = Enum('DownloadStatus', 'OK NOT_FOUND ERROR')

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

DEFAULT_CONCUR_REQ = 1
MAX_CONCUR_REQ = 1

SERVERS = {
    'REMOTE': 'https://www.fluentpython.com/data/flags',
    'LOCAL':  'http://localhost:8000/flags',
    'DELAY':  'http://localhost:8001/flags',
    'ERROR':  'http://localhost:8002/flags',
}
DEFAULT_SERVER = 'LOCAL'

SOURCE_DIR = Path("flags")
DEST_DIR = Path('downloaded')
COUNTRY_CODES_FILE = Path('country_codes.txt')

def save_flag(img: bytes, filename: str) -> None:
    (DEST_DIR / filename).write_bytes(img)

def initial_report(cc_list: list[str],
                   actual_req: int,
                   server_label: str) -> None:
    if len(cc_list) <= 10:
        cc_msg = ', '.join(cc_list)
    else:
        cc_msg = f'from {cc_list[0]} to {cc_list[-1]}'
    print(f'{server_label} site: {SERVERS[server_label]}')
    plural = 's' if len(cc_list) != 1 else ''
    print(f'Searching for {len(cc_list)} flag{plural}: {cc_msg}')
    if actual_req == 1:
        print('1 connection will be used.')
    else:
        print(f'{actual_req} concurrent connections will be used.')

def final_report(cc_list: list[str],
                 counter: Counter[DownloadStatus],
                 start_time: float) -> None:
    elapsed = time.perf_counter() - start_time
    print('-' * 20)
    plural = 's' if counter[DownloadStatus.OK] != 1 else ''
    print(f'{counter[DownloadStatus.OK]:3} flag{plural} downloaded.')
    if counter[DownloadStatus.NOT_FOUND]:
        print(f'{counter[DownloadStatus.NOT_FOUND]:3} not found.')
    if counter[DownloadStatus.ERROR]:
        plural = 's' if counter[DownloadStatus.ERROR] != 1 else ''
        print(f'{counter[DownloadStatus.ERROR]:3} error{plural}.')
    print(f'Elapsed time: {elapsed:.2f}s')

def expand_cc_args(every_cc: bool,
                   all_cc: bool,
                   cc_args: list[str],
                   limit: int) -> list[str]:
    if (limit < 0):
        raise ValueError("*** Usage error: 'No negative limits'")
    elif (limit == 0):
        limit = sys.maxsize
        
    codes: set[str] = set()
    A_Z = string.ascii_uppercase
    if every_cc:
        codes.update(a+b for a in A_Z for b in A_Z)
    elif all_cc:
        text = COUNTRY_CODES_FILE.read_text()
        codes.update(text.split())
    else:
        for cc in (c.upper() for c in cc_args):
            if len(cc) == 1 and cc in A_Z:
                codes.update(cc + c for c in A_Z)
            elif len(cc) == 2 and all(c in A_Z for c in cc):
                codes.add(cc)
            else:
                raise ValueError('*** Usage error: each CC argument '
                                 'must be A to Z or AA to ZZ.')
    return sorted(codes)[:limit]

# Setup
def main(download_many):
    # Country Codes
    allFlagsInFile = False
    allFlagCombination = False
    ccList = []
    ccLimit = 0
    numConcurrency = 1
    maxConcurrency = 1
    serverOption = 'REMOTE' # Server Option: 'REMOTE', 'LOCAL', 'DELAY', 'ERROR'
    
    try:
        ccList = expand_cc_args(allFlagsInFile, allFlagCombination, ccList, ccLimit)
    except ValueError as exc:
        sys.exit(1)
    if not ccList:
        ccList = sorted(POP20_CC)[:ccLimit]
    
    base_url = SERVERS[serverOption]
    
    actual_req = min(maxConcurrency, numConcurrency, len(ccList))
    initial_report(ccList, actual_req, serverOption)
    
    DEST_DIR.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    counter = download_many(ccList, base_url, False, actual_req)
    final_report(ccList, counter, t0)
