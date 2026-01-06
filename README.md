# Format String Exploit Script

## Quick Start
```bash
pip install pwntools
python3 exploit.py

# Usecase
## Change './chall' to your binary name
context.binary = binary = ELF('./chall')

# Update these to match your program's prompts
p.recvuntil(b'Enter your input here:')
p.recvuntil(b'You inputed:')


#Example output
```
1: 0x7ffd12345678
2: 0x400000
3: (nil)
4: 0x7f1234567890
```


