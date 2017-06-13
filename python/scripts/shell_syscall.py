#!/usr/bin/python
import subprocess
import commands
import argparse
import os


#class subprocess.Popen(args, bufsize=0, executable=None, stdin=None,
#    stdout=None, stderr=None, preexec_fn=None, close_fds=False, shell=False,
#    cwd=None, env=None, universal_newlines=False, startupinfo=None,
#    creationflags=0)


cmd1 = "echo a list of the direcotry: "
cmd2 = "ls -l"
cmds = [cmd1, cmd2]


#1 using module subprocess
for cmd in cmds:
  subprocess.call(cmd, shell=True)

p = subprocess.Popen('ls - l, shell=True, stdout=subprocess.PIPE)
print p.stdout.read()

p = subprocess.Popen('ls -l', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
out, err = p.communicate()
out.print()

subprocess.check_call(["ls", "-l"])

#2 using module os
os.system("ls -l")


#3 using module commands
commands.getoutput("ls -l")

