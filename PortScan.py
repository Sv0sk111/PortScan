import socket
YELLOW = '\033[93m'
CYAN = '\033[96m\033[40m'
RESET = '\033[0m'

def scan_ports():
    ip = input("Enter IP address: ")
    start_port = input("Enter start port: ")
    end_port = input("Enter end port: ")
    print(f'Scanning IP {ip} for open ports...')
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port}: Open")
        else:
            print("Error: Port wasn't open!")
        sock.close()

def scan_all_ports(ip):
    ip = input("Enter IP address: ")
    print(f'Scanning IP {ip} for open ports...')
    for port in range(0, 65536): 
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) 
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

def ascii():
    print(CYAN + "    ____             __  _____                 ")
    print("   / __ \____  _____/ /_/ ___/_________ _____  ")
    print("  / /_/ / __ \/ ___/ __/\__ \/ ___/ __ `/ __ \\")
    print(" / ____/ /_/ / /  / /_ ___/ / /__/ /_/ / / / / ")
    print("/_/    \____/_/   \__//____/\___/\__,_/_/ /_/  " + RESET)
    
def main():
    ascii()
    print(YELLOW + "0. Exit\n1. Scan specific port\n2. Scan all ports\n" + RESET)
    choice = input("Enter: ")
    if choice == '0':
        print("Thank you for using PortScan!")
        return 0
    elif choice == 1:
        scan_ports()
    elif choice == 2:
        scan_all_ports()
    else:
        print("Error: Invalid choice!")
    
if __name__ == "__main__":
    main()

