#!/usr/bin/python

import sys
import re

def show_rules():
    print("""
    The commit failed because one or many of the commit rules were not adhered to! Please check the rules and commit again!
    These are the rules for every commit message. Kindly request you to follow these : 
    1. Subject of the commit message must be <=50 characters in length
    2. The body of the commit message must be <=72 characters in length
    3. Commit message Subject should always start with capital letters
    4. No swear words should be used in commit message 
    """)
    
def main():
    print("##### Running commit-msg hook ########")
    print("Number of arguments are\n {0}\n The arguments are {1}".format(len(sys.argv),str(sys.argv) ))
    
    print("Run check commit message function")
    
    commit_msg_file = sys.argv[1]
    
    with open(commit_msg_file, "r") as fp:
        lines = fp.readlines()

        for idx, line in enumerate(lines):
            if line[0] == "#":
                continue

            if (not line_valid(idx, line)) or (is_swear(line)) :
                show_rules()
                sys.exit(1)

    sys.exit(0)


def line_valid(idx, line):
	if idx == 0 :
        # The subject line (1st line) should contain <=50 chars and should start with Capitals
		return re.match("^[A-Z].{,48}[0-9A-z \t]$", line)
	else:
        # All other lines should have <=72 characters
		return len(line.strip()) <= 72

def is_swear(line):
    swears_to_check = ['fuck', 'shit', 'jerk']
    if any(swear in line.lower() for swear in swears_to_check):
        print("Line contained swear word, please avoid using any in your commit messages")
        return True
    else : 
        return False
    
if __name__=="__main__" :
    main()