#!/usr/bin/python3
""" 0. Log Parsing. """
from sys import stdin
from typing import Dict, Sequence


possible_stat_codes: Sequence[int] = (200, 301, 400, 401, 403, 404, 405, 500)
stat_codes_count: Dict[int, int] = {k: 0 for k in possible_stat_codes}
total: Dict[str, int] = {'size': 0}


def print_stats(total_size: int) -> None:
    """
    Prints total size and number of occurrences for each status code
    :param total_size:
    :return: Nothing
    """
    print(f'File Size: {total_size}')
    for stat_code in possible_stat_codes:
        if stat_codes_count[stat_code] > 0:
            print(f'{stat_code}: {stat_codes_count[stat_code]}')


def show_log(line_num: int, current_size: int, stat_code: int) -> None:
    """
    Generates the log file output
    :param line_num: line number
    :param current_size:
    :param stat_code:
    :return: Nothing
    """
    total['size'] += current_size

    if stat_code in possible_stat_codes:
        stat_codes_count[stat_code] += 1

    if line_num % 10 == 0:
        print_stats(total['size'])


running: bool = True
n_line: int = 1

while running:
    try:
        line = stdin.readline()
        size = int(line.split(' ')[-1])
        code = int(line.split(' ')[-2])
    except ValueError:
        continue
    except (KeyboardInterrupt, EOFError):
        print_stats(total['size'])
        running = False
    else:
        show_log(n_line, size, code)

    n_line += 1
