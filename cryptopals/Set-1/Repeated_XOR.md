# Task: Implement Repeating-Key XOR

## Description

In this challenge, we are asked to implement a **repeating-key XOR cipher**, which applies a given key repeatedly across the length of the plaintext to produce ciphertext.

---

### Input Plaintext:
```
Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal
```
### Key:
```
ICE
```

---

### Expected Output (Hex Encoded):
```
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
```

---

## How Repeating-Key XOR Works

- Treat the key as a repeating stream of bytes.
- XOR each byte of the plaintext with the corresponding byte of the key (cycling through the key).
- Output the result as a hex string (for readability).

---

## Python Solution

```python
def rep_xor(msg: bytes , key: bytes) -> bytes:
    key_len = len(key)
    return bytes([msg[i] ^ key[i % key_len] for i in range(len(msg))])

while True:
    try:
        inp_str = input("hex:")
        str_byte = inp_str.encode()
        key = b'ICE'
        result = rep_xor(str_byte , key)
        print(f"XORed: {result.hex()}")
    except KeyboardInterrupt:
        print("\nExited!")
        break
    except ValueError:
        print("Invalid hex input.")
```
### Example Usage
Input:
```
Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal
```
Output(Hex):
```
0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
```
The output matches the expected hex string — indicating the implementation is correct.

---


