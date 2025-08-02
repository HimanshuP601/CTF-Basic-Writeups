def readable(text):
    return all( 32<= ord(c) <= 126 or c in '\n\r\t' for c in text)

with open('file.txt' , 'r') as f:
    for line in f:
        byte_str = bytes.fromhex(line.strip())
        for i in range(256):
            xored = bytes([b ^ i for b in byte_str])
            try:
                text = xored.decode('utf-8')
                if readable(text):
                    with open ('decoded.txt' , 'a') as f:
                        f.write(f'Key {i} {chr(i)}: {text}\n')

            except UnicodeDecodeError:
                continue
