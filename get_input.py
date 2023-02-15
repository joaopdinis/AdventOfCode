from sys import argv
from requests import get
import datetime
import os
import os.path

dt = datetime.datetime.today()

if len(argv) == 2:
    day = int(argv[1])
elif len(argv) == 3:
    day = int(argv[1])
    year = int(argv[2])
else:
    day = dt.day
    year = dt.year

if not os.path.exists(f'day{day}'):
    os.mkdir(os.path.join(os.getcwd(), f'day{day}'))
    f = open(os.path.join(os.getcwd(), f'day{day}', 'puzzle1.py'), 'w')
    f.write('input = [l.strip() for l in open(\'input.txt\')]')
    f.close()
    f = open(os.path.join(os.getcwd(), f'day{day}', 'puzzle2.py'), 'w')
    f.write('input = [l.strip() for l in open(\'input.txt\')]')
    f.close()

cookies = {'cookie': '_ga=GA1.2.83295175.1670323861;', 'session': '53616c7465645f5ffa3c4ba41ba84128c944feaaeccde2d31f2e2b3eb49b81f06aafdebb91b2f9cf8e853d500f80edd16376b2c6baceb1865e62e2ea9ed9d8e7;', '_gid': 'GA1.2.1248926858.1670954609'}

url = f'https://adventofcode.com/{year}/day/{day}/input'

print(get(url, cookies=cookies).text)