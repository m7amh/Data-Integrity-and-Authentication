
import hashlib
import struct
from Crypto.Hash import MD5


def hex_to_state(h):
    # Convert hash to internal state (A,B,C,D)
    bytes_hash = bytes.fromhex(h)
    a = struct.unpack('<I', bytes_hash[0:4])[0]
    b = struct.unpack('<I', bytes_hash[4:8])[0]
    c = struct.unpack('<I', bytes_hash[8:12])[0]
    d = struct.unpack('<I', bytes_hash[12:16])[0]
    return a, b, c, d

def md5_pad(message_bit_length):
    # MD5 padding as in Merkle-Damgård
    message_bit_length += 64  # account for the length field itself
    pad_len = (56 - (message_bit_length // 8) % 64) % 64
    padding = b'\x80' + b'\x00' * (pad_len - 1)
    padding += struct.pack('<Q', message_bit_length)
    return padding

# The known message and its MAC
intercepted_message = b"amount=100&to=alice"
original_mac = "614d28d808af46d3702fe35fae67267c"  # Use the value from server.py
data_to_append = b"&admin=true"
secret_length_guess = 16  # طول المفتاح السري (في هذا المثال نعرف أنه 16 بايت)

# Calculate the deleted length up to the beginning of the new data
message_bit_length = (secret_length_guess + len(intercepted_message)) * 8
pad = md5_pad(message_bit_length)

# Recalculate from internal state using Crypto.Hash.MD5
h = MD5.new()
h.update(intercepted_message)
# Pad the message to a block boundary

# Assuming original_mac is the MAC of intercepted_message
# Set the internal state of MD5 to the original_mac
h.digest_size = 16  
h.MD5_state = struct.unpack('<4I', bytes.fromhex(original_mac))
# Now you can continue hashing with the new data
h.update(pad + data_to_append)
forged_mac = h.hexdigest()


print("Forged Message:", intercepted_message + pad + data_to_append)
print("Forged MAC:", forged_mac)