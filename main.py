#!/usr/bin/env python3
from rich import print
import sys, os

# Green -> returns True if marked active, but not important
active = []
with open('active.txt', 'r') as i:
	j = i.readlines()
	if len(j) > 0:
		active = [line[:-1] for line in j]

# Red -> important returns True if marked important
important = []
with open('important.txt', 'r') as i:
	j = i.readlines()
	if len(j) > 0:
		important = [line[:-1] for line in j]

# Yellow -> updateable returns True if pip requirements need update
updateable = []
with open('updateable.txt', 'r') as i:
	j = i.readlines()
	if len(j) > 0:
		updateable = [line[:-1] for line in j]


# organize a virtual ls of parent dir and color dirs
def dirlist():
	curdir = os.getcwd()
	curdir = curdir.split('/')
	del curdir[-1]
	parentdir = "/".join(curdir)

	files = [x for x in os.listdir(parentdir)]
	for index, fi in enumerate(files):
		if fi in active:
			files[index] = f'[green]{fi}[/green]'
		elif fi in important:
			files[index] = f'[red]{fi}[/red]'
		elif fi in updateable:
			files[index] = f'[yellow]{fi}[/yellow]'
		elif fi not in active and fi not in important and fi not in updateable:
			files[index] = f'[white]{fi}[/white]'

	for a, b, c in zip(files[::3], files[1::3], files[2::3]):
		print('{0}		{1}		{2}'.format(a,b,c))

def main():
	dirlist()

if __name__ == "__main__":
	main()
