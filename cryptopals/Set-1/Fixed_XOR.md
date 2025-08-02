i# Task: Fixed XOR

## Description

In this challenge, we are required to write a function that performs a **bitwise XOR** operation on two equal-length byte buffers. This operation is fundamental in many cryptographic algorithms and is a key step in understanding how ciphertexts are constructed using simple operations.

---

### Inputs:

**Hex String 1:**
```
1c0111001f010100061a024b53535009181c
```
**Hex String 2:**
```
686974207468652062756c6c277320657965
```
---
### Expected Output:
```
746865206b696420646f6e277420706c6179
```

---

## Python Solution

Below is the Python implementation used to solve this task:

```python
hex1 = '1c0111001f010100061a024b53535009181c'
hex2 = '686974207468652062756c6c277320657965'

# Convert hex strings to bytes
byte1 = bytes.fromhex(hex1)
byte2 = bytes.fromhex(hex2)

# Perform XOR on corresponding bytes
res_byte = bytes(a ^ b for a, b in zip(byte1, byte2))

# Convert result back to hex
res_hex = res_byte.hex()

print(f"Result: {res_hex}")
```
### Explanation
- Hex to Bytes:
    - Convert each hex string to a bytes object using bytes.fromhex().
- Byte-wise XOR:
    - Use Python’s zip() to iterate over the byte pairs from both inputs.
    - Apply the XOR (^) operation on each byte-pair.
    - Create a new bytes object from the result.
- Bytes to Hex:
    - Convert the resulting XORed bytes back to a hex string using .hex() for display.

### Output
When executed, the script prints:
```
Result: 746865206b696420646f6e277420706c6179
```
---





