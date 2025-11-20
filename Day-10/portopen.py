import socket
import sys

def is_port_open(host, port):
    """Check if a port is open on a host."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <host> <port>")
        sys.exit(1)
    
    host = sys.argv[1]
    port = int(sys.argv[2])
    
    if is_port_open(host, port):
        print(f"Port {port} is open on {host}")
    else:
        print(f"Port {port} is closed on {host}")