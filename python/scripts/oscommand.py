#!/usr/bin/python
import subprocess
import os
import commands
import sys
import argparse


os.chdir("test_dir")

def runBash(cmd):
  output = commands.getoutput('ls')
  ll = list(output.split('\n'))
  return(ll)

print runBash('ls')

os.chdir("../")

print runBash('ls')


