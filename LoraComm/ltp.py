from scapy.all import Ether, Packet, ByteField, bind_layers


class LTP(Packet):
	name = "TCP "
	fields_desc=[ByteField("packet_type",1),
				ByteField("dev_id",1),
				ByteField("tag_id",1),
				ByteField("next_header",1)]

bind_layers(Ether, LTP);