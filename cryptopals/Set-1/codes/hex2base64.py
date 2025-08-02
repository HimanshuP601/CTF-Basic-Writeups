import base64

hex_str = input("Enter hex value:")
byte_str = bytes.fromhex(hex_str)
b64_str = base64.b64encode(byte_str)
print(f"\nHex:{hex_str}")
print(f"Base64:{b64_str.decode()}")
