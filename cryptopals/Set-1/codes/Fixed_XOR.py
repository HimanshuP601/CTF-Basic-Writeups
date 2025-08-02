hex1 = '1c0111001f010100061a024b53535009181c'
hex2 = '686974207468652062756c6c277320657965'

byte1 = bytes.fromhex(hex1)
byte2 = bytes.fromhex(hex2)

res_byte = bytes(a^b for a,b in zip(byte1,byte2))

res_hex = res_byte.hex()

print(f"Result:{res_hex}")
