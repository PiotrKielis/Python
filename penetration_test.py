import socket
import time

hosts = ['google.com', 'github.com']
ports = {'TCP': [21, 22, 80, 443], 'UDP': [53, 123]}

def port_scan(host, port, protocol='TCP'):
    print(f'Scanning {protocol} port {port} on {host}')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM if protocol == 'TCP' else socket.SOCK_DGRAM)
    client_socket.settimeout(0.5)  # ustawienie timeoutu na 500ms
    try:
        client_socket.connect((host, port))
        banner = client_socket.recv(1024).decode().strip()
        if banner:
            print(f'Port {port} is open')
            print(f'Banner: {banner}')
        else:
            print(f'Port {port} is open')
        client_socket.close()
    except Exception as e:
        pass

def penetration_test(hosts, ports):
    for host in hosts:
        print(f'Starting penetration test for {host}...\n')
        open_ports = set()
        for protocol, port_list in ports.items():
            for port in port_list:
                port_scan(host, port, protocol)
                if port in open_ports:
                    continue
                open_ports.add(port)
        if open_ports:
            print(f'\nOpen ports on {host}: {open_ports}\n')
        else:
            print(f'No open ports on {host}\n')

penetration_test(hosts, ports)
