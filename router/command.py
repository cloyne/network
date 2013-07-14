import sys

import paramiko

def cmd(command):
  # setup ssh
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

  # connect to ssh
  ssh.connect('router', username='admin', password='pirateparty', key_filename='./id_dsa')

  # execute command over ssh
  stdin, stdout, stderr = ssh.exec_command(command)

  # pipe output
  sys.stdout.write(stdout.read())
  sys.stderr.write(stderr.read())

  ssh.close()
