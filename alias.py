#!/usr/bin/env python3
from os.path import exists, expanduser

h = expanduser('~')

with open(f'{h}/.bash_profile', 'a') as x:
	count = 0
	x1 = x.read().splitlines()
	x2 = [line[:-1] for line in x]
	if 'alias cls=\'python3 colorls.py\'' in x2:
		count += 1
	if count > 0:
		pass
	elif count == 0:
		x.write('\n\nalias cls=\'python3 colorls.py\'')
