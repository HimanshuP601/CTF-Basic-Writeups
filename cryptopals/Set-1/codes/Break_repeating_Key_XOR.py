import base64

def hamming (str1:str , str2:str ) -> int:
    if (len(str1) != len(str2)):
        raise ValueError("Strings must of equal length.")
    return sum(bin(a^b).count('1') for a,b in zip(str1,str2))


def key_len(cipher:str , max_len = 40 , min_len = 2 , num_chunks=4):
    key_score = []

    for keysize in range(min_len , max_len+1):
        chunks = [cipher[i*keysize:(i+1)*keysize] for i in range (num_chunks)]

        if len(chunks[-1]) < keysize:
            continue

        dists = []
        for i in range (num_chunks-1):
            dist = hamming(chunks[i] , chunks[i+1])
            norm = dist / keysize
            dists.append(norm)
        
        avg_dist = sum(dists) / len(dists)
        key_score.append((keysize , avg_dist))

    key_score.sort(key=lambda x:x[1])
    return key_score


def main():
    with open('file2.txt' , 'rb') as f:
        b64_data = f.read()
    ciphertext = base64.b64decode(b64_data)    

    scores = key_len(ciphertext)

    for keysize , score in scores[:5]:
        print(f"Keysize: {keysize}, Normalized distance: {score:.3f}")

if __name__ == '__main__':
    main()

