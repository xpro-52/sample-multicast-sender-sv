import socket
import struct
import time

# Set multicast address and port
multicast_group = '224.1.1.1'
port = 5004

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
    while True:
        message = b'This is a multicast message'
        print(f'Sending "{message}" to {multicast_group}:{port}')
        sock.sendto(message, (multicast_group, port))
        time.sleep(1)
finally:
    sock.close()
