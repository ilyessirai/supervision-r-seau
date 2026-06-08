import socket
import urllib.parse

def scan_ports(target, ports):
    """
    Scans a target for open ports.
    Target can be an IP address or a URL/Hostname.
    """
    try:
        # Handle URLs by extracting the hostname
        if "://" in target:
            target = urllib.parse.urlparse(target).hostname
        
        # Resolve hostname to IP
        print(f"Resolving {target}...")
        target_ip = socket.gethostbyname(target)
        print(f"Scanning target {target} ({target_ip})...")
        
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: Open")
            else:
                # Silently fail or print closed for training clarity
                pass 
            sock.close()
            
    except socket.gaierror:
        print(f"Error: Could not resolve hostname {target}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage with a hostname/URL
    target_addr = "google.com" 
    ports_to_scan = [80, 443, 22, 8080]
    scan_ports(target_addr, ports_to_scan)
