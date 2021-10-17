# GIT HOOKS sample

This project is used to illustrate some of the uses of GIT Hooks.

Steps to install Git Hooks : 
1. Clone the repository (By default, you will be on master branch)
2. Run install_hooks.sh on linux/Mac OR install_hooks.bat on windows

Step 2 makes sure that client-side GIT hooks are installed.

# INFO about GIT Hooks

Hooks are programs you can place in a hooks directory to trigger actions at certain points in git’s execution. Hooks that don’t have the executable bit set are ignored.

The types of GIT hooks implemented in this project are : 

## pre-commit
1. We can auto-format python code using Black formatter

## commit-msg
1. Check if commit message follows standard practises
2. We can provide meaningful instructions on how to prepare a commit message.

## pre-rebase 
1. can be used to abort rebase command on any commits

# Important information

To bypass any client side hook, use `--no-verify` flag along with the command.
For example, 
to bypass a client-side commit hook, please add `git commit -m "First commit" --no-verify`

# Useful Commands : 

1. View directory structure in Linux

`find . | sed -e "s/[^-][^\/]*\// |/g" -e "s/|\([^ ]\)/|-\1/"`
