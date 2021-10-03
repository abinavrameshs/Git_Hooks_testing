#!/usr/bin/python

import sys

def main():
	print(f"Number of args = {len(sys.argv)}")
	print(f"Arguement list = {str(sys.argv)}")
	print("Hello to git hooks")

	sys.exit(1)

if __name__ == "__main__" :
	main()