import paramiko
#import threading
from threading import Thread

server_list=['localhost']
mount_point = '/dev/mapper/fedora-root'
threashold = 90

def check_disk(server,mount_point):
  s = paramiko.SSHClint()
  s.set_mising_host_key_policy(paramiko.AutoAddPolicy()) #avoid enter a password
  s.connect(server,username='mylogin',password='mypassword',allow_agent=False,look_for_keys=False)
  err,out,ins = s.exec_command("df -h")
  ss = out.read()
  for line in ss.split('\n'):
    if len(line.split()) > 0:
      if line.split()[0] == mount_point:
        return int(line.split()[4].rstrip('%')))
      

for server in server_list:
  disk_usage = check_disk(server,mount_point)
    if disk_usage > threshold:
      print('Sending email')
    else:
      print('All is well')

def server_check(server):
  disk_usage = check_disk(server,mount_point)
  if disk_usage > threshold:
      print('Sending email')
  else:
      print('All is well')

#None thread loop
for server in server_list:
  server_check(server)


#Thread loop
for server in server_list:
  t = Tread(target=server_check, arge=(server,))
  t.start()
        
