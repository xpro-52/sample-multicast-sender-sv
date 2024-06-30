import socket
import time
from datetime import datetime

# network interface of sender
sender_address = '192.168.8.10'

# address and port of multicast group
multicast_group = '224.1.1.1'
port = 5004

# finally close
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.setsockopt(socket.IPPROTO_IP,  # ipv4
                         socket.IP_MULTICAST_IF,  # do multicast bellow interface
                         socket.inet_aton(sender_address))

    while True:
        now = datetime.strftime(datetime.now(), '%Y-%M-%d %H:%M:%S')
        message = f'[{now}] This is a multicast message'
        print(f'Sending "{message}" to {multicast_group}:{port}')
        sock.sendto(message.encode(), (multicast_group, port))
        time.sleep(1)
