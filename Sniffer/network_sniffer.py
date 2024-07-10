import argparse
from scapy.all import sniff, wrpcap, Raw
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.l2 import ARP


def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet.getlayer(IP)
        print(f"IP Packet: {ip_layer.src} -> {ip_layer.dst}")

        if packet.haslayer(TCP):
            tcp_layer = packet.getlayer(TCP)
            print(f"TCP Packet: {tcp_layer.sport} -> {tcp_layer.dport}")

            if packet.haslayer(Raw):
                print(f"Payload: {packet[Raw].load}")

        elif packet.haslayer(UDP):
            udp_layer = packet.getlayer(UDP)
            print(f"UDP Packet: {udp_layer.sport} -> {udp_layer.dport}")

            if packet.haslayer(Raw):
                print(f"Payload: {packet[Raw].load}")

        elif packet.haslayer(ICMP):
            icmp_layer = packet.getlayer(ICMP)
            print(f"ICMP Packet: Type {icmp_layer.type} Code {icmp_layer.code}")

    elif packet.haslayer(ARP):
        arp_layer = packet.getlayer(ARP)
        print(f"ARP Packet: {arp_layer.psrc} -> {arp_layer.pdst} ({arp_layer.op})")


def main():
    parser = argparse.ArgumentParser(description="A simple network sniffer.")
    parser.add_argument('-c', '--count', type=int, default=10, help="Number of packets to capture")
    parser.add_argument('-f', '--filter', type=str, default="", help="BPF filter for packet capture")
    parser.add_argument('-o', '--output', type=str, default="captured_packets.pcap",
                        help="Output file to save captured packets")

    args = parser.parse_args()

    print(f"Starting sniffer with filter: {args.filter}")
    captured_packets = sniff(prn=packet_callback, count=args.count, filter=args.filter)

    print(f"Saving captured packets to {args.output}")
    wrpcap(args.output, captured_packets)


if __name__ == "__main__":
    main()
