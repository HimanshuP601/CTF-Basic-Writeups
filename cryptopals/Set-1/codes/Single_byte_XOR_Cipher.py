hex_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
byte_hex = bytes.fromhex(hex_str)

for i in range(256):
    xored = bytes([ b ^ i for b in byte_hex])
    try:
        text = xored.decode('utf-8')
        print(f'Key {i} ({chr(i)}): {text}')
    except UnicodeDecodeError:
        continue
