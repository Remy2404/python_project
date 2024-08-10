from ipaddress import ip_network, ip_address

def calculate_subnet(network, num_ips):
    net = ip_network(network)
    subnets = list(net.subnets(new_prefix=(32 - (num_ips - 1).bit_length())))
    return subnets[0]

def print_subnet_details(company, section, subnet, num_ips):
    print(f"Company {company} - {section}:")
    print(f"  Network Address: {subnet.network_address}")
    print(f"  First IP: {subnet.network_address + 1}")
    print(f"  Last IP: {subnet.network_address + num_ips - 2}")
    print(f"  Broadcast Address: {subnet.broadcast_address}")
    print(f"  Subnet Mask: {subnet.netmask}")
    print()

# Company DEF
print("Company DEF")
print_subnet_details("DEF", "Section A", calculate_subnet("192.168.56.0/24", 120), 120)
print_subnet_details("DEF", "Section B", calculate_subnet("192.168.56.128/25", 10), 10)
print_subnet_details("DEF", "Section C", calculate_subnet("192.168.56.134/28", 10), 10)

# Company LMN
print("Company LMN")
print_subnet_details("LMN", "Dept A", calculate_subnet("192.168.216.0/23", 250), 250)
print_subnet_details("LMN", "Dept B", calculate_subnet("192.168.217.0/23", 250), 250)
print_subnet_details("LMN", "Dept C", calculate_subnet("192.168.218.0/23", 250), 250)

# Company OPQ
print("Company OPQ")
print_subnet_details("OPQ", "Production", calculate_subnet("192.168.99.0/25", 60), 60)
print_subnet_details("OPQ", "Admin", calculate_subnet("192.168.99.64/26", 30), 30)
print_subnet_details("OPQ", "Delivery", calculate_subnet("192.168.99.96/28", 10), 10)

# Connecting Networks
print("Connecting Networks")
print_subnet_details("Connecting DEF to LMN", "", calculate_subnet("192.168.1.0/24", 254), 254)
print_subnet_details("Connecting LMN to OPQ", "", calculate_subnet("192.168.2.0/24", 254), 254)
