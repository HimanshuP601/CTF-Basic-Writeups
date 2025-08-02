# Task: Single-byte XOR Cipher

## Description

In this challenge, a hex-encoded string has been XOR'd against a single character. The goal is to determine the single-byte key, decrypt the message, and retrieve the original plaintext.

---

## Input (Hex-encoded string):

```
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
```

---

## Objective

- XOR the byte-decoded hex string against all possible single-byte values (0–255).
- Score each resulting output using a metric to judge how “English-like” the result is (e.g., character frequency).
- Identify the key that produces the most plausible English sentence.

---

## Cryptopals Rule Reminder

> **Always operate on raw bytes, never on encoded strings.** Only use hex and base64 for pretty-printing.

---

## Python Solution

```python
hex_str = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
byte_hex = bytes.fromhex(hex_str)

for i in range(256):
    xored = bytes([b ^ i for b in byte_hex])
    try:
        text = xored.decode('utf-8')
        print(f'Key {i} ({chr(i)}): {text}')
    except UnicodeDecodeError:
        continue
```

### Output: 
```
Key 88 (X): Cooking MC's like a pound of bacon
```
 This is a grammatically correct and meaningful English sentence, so we conclude:
- Key (ASCII): X
- Key (Decimal): 88
- Decrypted Message: Cooking MC's like a pound of bacon
---
