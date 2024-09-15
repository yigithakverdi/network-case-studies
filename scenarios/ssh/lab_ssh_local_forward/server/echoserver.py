# Echo server program
import socket
import threading

HOST = '0.0.0.0'                 # Symbolic name meaning all available interfaces
PORT = 8080              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

def target(conn, addr):
  print('Connected by', addr)
  if addr[0] == "10.0.3.2":
    conn.sendall(b"This service is not available in Germany. Closing\n")
    conn.close()
    return
  conn.sendall(b"hi, connected from Italy\n")
  while True:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(b"-->  "+data)
  conn.close()

while True:
  conn, addr = s.accept()
  t = threading.Thread(target=target, args=(conn, addr))
  t.daemon = False
  t.start()
