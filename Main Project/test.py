import base64

message = input("type a message: ")
message_bytes = message.encode('ascii')
base64_bytes = base64.b64decode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print ("message {} ({})".format(message, base64_message))
