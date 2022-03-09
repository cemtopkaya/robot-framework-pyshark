import pyshark 
from simple_crawl import double

def network_conversation(packet):
  try:
    protocol = packet.transport_layer
    source_address = packet.ip.src
    source_port = packet[packet.transport_layer].srcport
    destination_address = packet.ip.dst
    destination_port = packet[packet.transport_layer].dstport
    return (f'{protocol} {source_address}:{source_port} --> {destination_address}:{destination_port}')
  except AttributeError as e:
    pass

def yaz_dostum():
    print("merhaba cem000")
    # double.Pool
    capture = pyshark.FileCapture('ex.pcap')
    conversations = []
    for packet in capture:
        results = network_conversation(packet)
        if results != None:
            conversations.append(results)

    for item in sorted(conversations):
        print (item)

# def read_from_file():
#     capture = pyshark.FileCapture('test.pcap')