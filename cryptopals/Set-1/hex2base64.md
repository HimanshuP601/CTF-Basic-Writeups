# Task: Convert Hex to Base64

## Description

In this task, we are required to convert a given hexadecimal string into its equivalent Base64 representation.

### Input Hex String:
```
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
```
### Expected Base64 Output:
```
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
```

---
## Objective

To convert hexadecimal-encoded data into Base64-encoded format. This is a foundational operation in cryptography challenges like those found in the Cryptopals Crypto Challenges.

## Rule Reminder (Cryptopals Rule)

> **Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.**

This means:
- Do not manipulate strings directly as characters.
- Convert from hex to raw bytes.
- Encode those bytes into Base64.

## Python Solution

Below is the Python script to achieve this conversion:

```python
import base64

hex_str = input("Enter hex value:")
byte_str = bytes.fromhex(hex_str)
b64_str = base64.b64encode(byte_str)
print(f"\nHex:{hex_str}")
print(f"Base64:{b64_str.decode()}")
```
### Example Usage
Input:
```
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
```
Output:
```
Hex:49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
Base64:SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
```
---
