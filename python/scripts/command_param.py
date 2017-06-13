                                                                                                      #!/usr/bin/python
import subprocess
import commands
import argparse
import sys

#cmd1 = "echo a list of the direcotry: "
#cmd2 = "ls -l"

#cmds = [cmd1, cmd2]

#for cmd in cmds:
#  subprocess.call(cmd, shell=True)

#subprocess.check_call(["ls", "-l"])

#Parse command line arguents
#parser = argparse.ArgumentParser(description='Batch change filenames.')
#parser.add_argument('inputFileName',metavar='baseNameIn')
#parser.add_argument('outputFileName',metavar='baseNameOut')
#args=parser.parse_args()


def runBash(cmd):
  output = commands.getoutput('ls')
 # print (output)
  ll = list(output.split('\n'))
  return(ll)


def changeName(oldName,newNameBase):
  temp = oldName.split('.')
  newName = newNameBase + '.' + temp[1] + '.' + temp[2]
  subprocess.call(["mv", oldName, newName])

def changeAllNames(oldNameBase,newNameBase):
  files = runBash("ls")
  for afile in files:
    print afile
    if afile.split('.')[0] == oldNameBase:
      changeName(afile,newNameBase)

#Change files with base test to base new
#changeAllNames("test","new")
#changeAllNames(args.inputFileName, args.outputFileName)
if len(sys.argv) == 3:
  changeAllNames(sys.argv[1], sys.argv[2])

