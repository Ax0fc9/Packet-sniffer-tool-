from scapy.all import sniff

def process_packet(packet):

    if packet.haslayer("IP"):
        ip_src = packet["IP"].src
        ip_dst = packet["IP"].dst
        proto = packet["IP"].proto
        print(f"[+] Packet: {ip_src}  {ip_dst} | Protocol: {proto}")


print(".......... Capturing the network, press Ctrl+C to stop capturing")


sniff(prn=process_packet, store=False)
