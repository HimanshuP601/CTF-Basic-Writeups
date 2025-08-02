def rep_xor(msg: bytes , key: bytes) -> bytes:
    key_len = len(key)
    return bytes([msg[i] ^ key[i % key_len] for i in range(len(msg))])
while True:
    try:
        inp_str = input("hex:")
        str_byte = inp_str.encode()
        key = b'ICE'
        result = rep_xor(str_byte , key)
        print("fXORED: {result.hex()}")
    except KeyboardInterrupt:
        print("\nExited!")
        break
    except ValueError:
        print("Invalid hex input.")
