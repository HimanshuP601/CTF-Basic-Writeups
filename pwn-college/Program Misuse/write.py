import datetime

def format_description(description, binary_name):
    # Replace only the first exact word match with a Markdown backtick version
    return description.replace(binary_name, f"`{binary_name}`", 1)

def read_multiline_input(label):
    print(f"{label} (finish input with a line containing only 'EOF'):")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "EOF":
            break
        lines.append(line)
    return "\n".join(lines)

def main():
    print("📘 CTF Writeup Generator v3 (by Himanshu Parate)\n")

    # Constants
    platform = "pwn.college"
    difficulty = "Beginner"
    author = "Himanshu Parate"
    category = "Program Misuse"
    binary_base_path = "/usr/bin/"

    # Inputs
    challenge_name = input("Challenge Name: ").strip()
    binary_name = challenge_name.lower()
    binary_path = binary_base_path + binary_name
    filename = input("Output Filename (e.g., socat.md): ").strip()

    # Read sections
    print("\n📝 Enter Exploitation Description")
    raw_description = read_multiline_input("Paste description")
    formatted_description = format_description(raw_description, binary_name)

    print("\n💻 Enter Exploit Command")
    exploit_command = read_multiline_input("Paste command")

    print("\n📤 Enter Command Output")
    command_output = read_multiline_input("Paste output")

    date = datetime.date.today().strftime("%Y-%m-%d")

    # Final markdown output
    content = f"""# Challenge Name: {challenge_name}
**Category**: {category}  
**Platform**: {platform}  
**Difficulty**: {difficulty}  
**Date**: {date}  
**Author**: {author}

---

## 🧠 Summary:
The challenge abuses a SUID bit set on `{binary_path}`, allowing an unprivileged user to read the root-owned flag file at `/flag`.

---

## 🔍 Enumeration

```bash
ls -l {binary_path}
```

Output:
```
-rwsr-xr-x 1 root root 47480 Sep  5  2019 {binary_path}
```

- The `s` in `-rws` indicates it's a SUID binary.
- `{binary_name}` runs with **root privileges**.

## 🚀 Exploitation

{formatted_description}

```bash
{exploit_command}
```

Output:
```
{command_output}
```
"""

    with open(filename, "w") as f:
        f.write(content)

    print(f"\n✅ Successfully saved writeup to `{filename}`")

if __name__ == "__main__":
    main()
