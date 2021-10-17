#!/usr/bin/python

import sys
import re
import os
import subprocess


def main():
    print("##### Running pre-commit hook ########")
    print("Number of arguments are\n {0}\n The arguments are {1}".format(len(sys.argv),str(sys.argv) ))
    
    
    ## Get the present working directory
    current_dir = os.getcwd()
    print('The working directory is {}'.format(current_dir))
    print("Running BLACK formatter on all files before committing")
    black_format = subprocess.Popen('black ./src/ ', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    std_out, std_err = black_format.communicate()
    print('stdout is {0}\nstderr is {1}'.format(std_out,std_err))   
    
    #sys.exit(1)
    

if __name__=="__main__" :
    main() 