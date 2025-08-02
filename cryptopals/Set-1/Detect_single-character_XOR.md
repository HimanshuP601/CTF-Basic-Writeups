# Cryptopals Set 1 - Challenge 4: Detect Single-Character XOR

## 🧠 Task

One of the 60-character strings in the provided file has been encrypted using a single-character XOR.

**Your job:** Detect which line has been encrypted and recover the original plaintext.

---

## 📌 Goal

- Detect the encrypted line from `file.txt`.
- Identify the XOR key used.
- Recover and print the original plaintext.

---

## 🔐 Cryptopals Rule

> Always operate on **raw bytes**, never on encoded strings. Only use **hex and base64** for pretty-printing.

---

## 🛠️ Strategy

This is an extension of Challenge 3. We:
1. Loop through each line in the input file.
2. Convert hex to raw bytes.
3. Try all 256 possible XOR single-byte keys.
4. Decode and check for human-readable strings.
5. Score each result based on English letter frequency.
6. Return the best-scoring plaintext.

---

## ✅ Solution: `Detect_single-character_XOR.py`

```python
def readable(text):
    return all(32 <= ord(c) <= 126 or c in '\n\r\t' for c in text)

with open('file.txt', 'r') as f:
    for line in f:
        byte_str = bytes.fromhex(line.strip())
        for i in range(256):
            xored = bytes([b ^ i for b in byte_str])
            try:
                text = xored.decode('utf-8')
                if readable(text):
                    with open('decoded.txt', 'a') as f:
                        f.write(f'Key {i} ({chr(i)}): {text}\n')
            except UnicodeDecodeError:
                continue
```
### Output Snippet: decoded.txt
```
...
Key 53 (5): Now that the party is jumping
...
```
### Final Answer

- Encrypted Line: Line that produces: Now that the party is jumping
- Key Used: 53 (ASCII '5')
- Plaintext: Now that the party is jumping
---

