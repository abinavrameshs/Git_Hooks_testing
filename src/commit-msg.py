#!/usr/bin/python

import sys

def main():
	print("Number of args = ")
	print(len(sys.argv))
	print("Arguement list = ")
	print(str(sys.argv))
	print("########### ")

	commit_file=sys.argv[1]

	with open(commit_file, "r") as fp :
		lines = fp.readlines()

		for i, line in enumerate(lines) :
			print("The line Number is ", i )
			print(line)

	sys.exit(0)

if __name__ == "__main__" :
	main()