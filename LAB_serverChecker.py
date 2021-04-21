"""
We want you to write a simple CLI (Command Line Interface) tool which can be
used in order to diagnose the current status of a particular http server.
The tool should accept one or two command line arguments:

(obligatory) the address (IP or qualified domain name) of the server to be
diagnosed (the diagnosis will be extremely simple, we just want to know if
the server is dead or alive)
(optional) the server's port number (any absence of the argument means that
the tool should use port 80)
use the HEAD method instead of GET — it forces the server to send the full
response header but without any content; it's enough to check if the server is working properly; the rest of the request remains the same as for GET.
We also assume that:

the tool checks if it is invoked properly, and when the invocation lacks any
arguments, the tool prints an error message and returns an exit code equal to 1;
if there are two arguments in the invocation line and the second one is not an
integer number in the range 1..65535, the tool prints an error message and
returns an exit code equal to 2;
if the tool experiences a timeout during connection, an error message is printed
and 3 is returned as the exit code;
if the connection fails due to any other reason, an error message appears
and 4 is returned as the exit code;
if the connection succeeds, the very first line of the server’s response is
printed.

"""

import sys
import socket

port_num = 80

if len(sys.argv) not in [2, 3]:
    exit("improper number of arguments: at least one is required and notr more than two allowed:\
     \n - http server address required\
      \n - port number(defaults to 80)")
if len(sys.argv) == 3:
    try:
        port_num = int(sys.argv[2])
    except ValueError:
        exit("Port number must be a number")
if not 0<=port_num<=65535:
    exit("port number must me number between 0 and 65535")

server_address = sys.argv[1]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((server_address, port_num))
except Exception as e:
    exit(e.args[1])

# add ssl to request
# sock = ssl.wrap_socket(sock, keyfile=None, certfile=None,
# server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)

sock.send(b"HEAD / HTTP/1.1\r\nHost: " +
          bytes(server_address, "utf8") +
          b"\r\nConnection: close\r\n\r\n")

reply = sock.recv(1000).decode('utf-8')

shutdown_failure = None
try:
    sock.shutdown(socket.SHUT_RDWR) #this breaks on ssl ports
except Exception as e:
    shutdown_failure = e.args[1]
sock.close()

if shutdown_failure:
    exit(shutdown_failure)
elif reply:
    exit(f"{reply[:12]} found")
else:
    exit('no data recieved')
