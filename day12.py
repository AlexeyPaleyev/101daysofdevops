import paramiko
sshcn = paramiko.SSHClient()
sshcn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshcn.connect("3.124.191.141", username="ubuntu", key_filename="onixua.pem")

stdin, stdout, stderr = sshcn.exec_command('uptime')
print (stdout.readlines())
sshcn.close()
