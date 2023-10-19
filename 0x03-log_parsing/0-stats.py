#!/usr/bin/python3
""" 0. Log Parsing"""
from sys import stdin
from typing import Dict, Sequence

possible_stat_codes: Sequence[int] = (200, 301, 400, 401, 403, 404, 405, 500)
stat_codes_count: Dict[int, int] = {k: 0 for k in possible_stat_codes}

total_size = 0


def show_log(index: int, line: str, total_size: int) -> None:
    """
    Generates the log file output
    :param index: line number
    :param line: context of line from stdin
    :param total_size: total size in bytes
    :return: Nothing
    """
    size = int(line.split(' ')[-1])
    stat_code = int(line.split(' ')[-2])
    total_size += size

    if stat_code in possible_stat_codes and isinstance(stat_code, int):
        stat_codes_count[stat_code] += 1

    if (index + 1) % 10 == 0:
        print(f'File Size: {total_size}')
        for code in possible_stat_codes:
            if stat_codes_count[code] > 0:
                print(f'{code}: {stat_codes_count[code]}')


try:
    for index, line in enumerate(stdin):
        show_log(index, line, total_size)
except KeyboardInterrupt:
    show_log(index, line, total_size)
