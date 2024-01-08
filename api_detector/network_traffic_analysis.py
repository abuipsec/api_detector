import scapy.all as scapy

def capture_traffic(interface="eth0", count=10):
    """
    Capture network traffic using Scapy.

    Args:
        interface (str): The network interface to capture traffic from.
        count (int): The number of packets to capture.

    Returns:
        list: List of captured packets.
    """
    packets = scapy.sniff(iface=interface, store=True, count=count)
    return packets

def analyze_http_packets(packets):
    """
    Analyze HTTP packets from the captured network traffic.

    Args:
        packets (list): List of network packets.

    Returns:
        list: List of HTTP packets.
    """
    http_packets = [packet for packet in packets if packet.haslayer(scapy.IP) and packet.haslayer(scapy.TCP) and
                    packet.haslayer(scapy.Raw) and packet[scapy.TCP].dport == 80]
    return http_packets

# Example usage:
# packets = capture_traffic(interface="eth0", count=20)
# http_packets = analyze_http_packets(packets)
# print(http_packets)
