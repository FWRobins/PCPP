import socket

'''import ssl for https sits, else get 301 response'''
import ssl

# server_addr = input("server address?")
server_addr = "pythoninstitute.org"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# change post to 443 for ssl
sock.connect((server_addr, 443))

# add ssl to request
sock = ssl.wrap_socket(sock, keyfile=None, certfile=None,
server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)

sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")

reply = sock.recv(1000)

sock.shutdown(socket.SHUT_RDWR)
sock.close()

print(repr(reply))
