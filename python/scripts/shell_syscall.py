#!/usr/bin/python
import subprocess
import commands
import argparse
import os

cmd1 = "echo a list of the direcotry: "
cmd2 = "ls -l"
cmds = [cmd1, cmd2]


#1 using module subprocess
for cmd in cmds:
  subprocess.call(cmd, shell=True)

p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
print p.stdout.read()

subprocess.check_call(["ls", "-l"])

#2 using module os
os.system("ls -l")


#3 using module commands
commands.getoutput("ls -l")

