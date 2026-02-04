# Interactive Binary Vulnerability Scanner

An automated binary vulnerability scanner and fuzzer designed to detect format string vulnerabilities and buffer overflow vulnerabilities in Linux executables. This tool performs intelligent fuzzing with automatic leak classification, crash detection, and offset calculation.

## 🎯 Features

### Format String Fuzzing
- **Automated offset iteration** - Tests format string offsets from 1 to 60
- **Intelligent leak detection** - Automatically captures and parses hex addresses from program output
- **Address classification** - Categorizes leaked addresses into:
  - Stack/Libc leaks (high memory addresses)
  - PIE/Heap leaks
  - Binary leaks (non-PIE)
  - NULL pointers
  - Small integers
- **Real-time structured output** - Displays results as they're discovered

### Buffer Overflow Fuzzing
- **Progressive payload sizing** - Tests with incrementally larger payloads (64, 128, 256, 512, 1024, 2048, 4096 bytes)
- **Automatic crash detection** - Identifies SIGSEGV crashes automatically
- **Offset calculation** - Extracts the exact offset to RIP/EIP using cyclic patterns
- **Core dump analysis** - Leverages core files for precise offset determination

### Interactive Menu System
- **Checksec** - Run security checks on the binary
- **Format String Fuzzer** - Run only format string tests
- **Buffer Overflow Fuzzer** - Run only buffer overflow tests
- **Full Auto Scan** - Run both fuzzers sequentially
- User-friendly menu-driven interface

## 📋 Requirements

- Python 3.6+
- Linux operating system (required for binary exploitation primitives)
- pwntools library

## 🔧 Installation

### Step 1: Clone or Download
```bash
git clone https://github.com/12bijaya/Format_String_Fuzzer.git
cd Format_String_Fuzzer
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

Or install pwntools directly:
```bash
pip install pwntools
```

### Step 3: Make the Script Executable (Optional)
```bash
chmod +x fuzz.py
```

## 🚀 Usage

### Basic Usage
```bash
python3 fuzz.py <path-to-binary>
```

### Example
```bash
python3 fuzz.py ./vulnerable_program
```

### Interactive Menu
Once launched, you'll see an interactive menu:
```
========================================
    INTERACTIVE BINARY VULN SCANNER
========================================
    [1] Start Vulnerability Scan
    [2] Format String Fuzzer
    [3] Buffer Overflow Fuzzer
    [4] Full Auto Scan (Both)
    [5] Exit
========================================
```

**Option 1**: Run `checksec` to view binary security protections (NX, PIE, RELRO, etc.)

**Option 2**: Run only the format string fuzzer

**Option 3**: Run only the buffer overflow fuzzer

**Option 4**: Run both fuzzers automatically in sequence

**Option 5**: Exit the tool

## 📊 Sample Output

### Format String Fuzzer Output
```
========================================
[*] STARTING FORMAT STRING FUZZER
========================================
[*] Fuzzing offsets 1 to 60...
Offset 1  → Stack/Libc leak → 0x7ffd12345678
Offset 2  → Binary leak (No PIE) → 0x400756
Offset 3  → NULL           → (nil)
Offset 6  → Stack/Libc leak → 0x7f9876543210

----------------------------------------
[FORMAT STRING RESULTS]
Offset 1  → Stack/Libc leak → 0x7ffd12345678
Offset 2  → Binary leak (No PIE) → 0x400756
Offset 6  → Stack/Libc leak → 0x7f9876543210
----------------------------------------
```

### Buffer Overflow Fuzzer Output
```
========================================
[*] STARTING BUFFER OVERFLOW FUZZER
========================================
[*] Testing payload size: 64 bytes...
[*] Testing payload size: 128 bytes...
[!] CRASH DETECTED with 128 bytes! (SIGSEGV)

----------------------------------------
[BUFFER OVERFLOW RESULTS]
Crash detected ✔
RIP overwritten ✔
Offset found: 72 bytes
----------------------------------------
```

## 🛠️ Advanced Configuration

### Enabling Core Dumps
For precise offset calculation in buffer overflow fuzzing, enable core dumps:
```bash
ulimit -c unlimited
echo "core" | sudo tee /proc/sys/kernel/core_pattern
```

### Architecture Support
The tool automatically detects the binary architecture and adapts:
- **x86-64** (amd64)
- **x86** (i386)
- Other architectures supported by pwntools

## 📝 How It Works

### Format String Detection
1. Launches the target binary for each offset (1-60)
2. Sends a format string payload: `%N$p` where N is the offset
3. Captures program output and searches for hex addresses
4. Classifies leaked addresses based on memory ranges
5. Displays results in a structured table

### Buffer Overflow Detection
1. Generates cyclic patterns of increasing sizes
2. Sends each pattern to the target binary
3. Monitors for crash signals (SIGSEGV)
4. Analyzes core dumps to find the exact offset to RIP/EIP
5. Reports crash status and offset if found

## ⚠️ Important Notes

- **Legal Use Only**: Only use this tool on binaries you own or have explicit permission to test
- **Core Dumps**: The buffer overflow fuzzer works best with core dumps enabled
- **Local Testing**: This tool is designed for local binary analysis, not remote exploitation
- **Timeout Handling**: The tool uses intelligent timeout handling to deal with various program behaviors

## 🐛 Troubleshooting

### "pwntools not installed" Error
```bash
pip install pwntools
```

### "Could not load ELF context" Warning
This warning appears when the binary format is unusual but fuzzing will still proceed.

### No Offset Found in Buffer Overflow
Enable core dumps:
```bash
ulimit -c unlimited
```

### Permission Denied
Make the binary executable:
```bash
chmod +x your_binary
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit pull requests.

## 📄 License

This project is open source and available under the MIT License.

## 🔗 Resources

- [Pwntools Documentation](https://docs.pwntools.com/)
- [Format String Vulnerabilities](https://owasp.org/www-community/attacks/Format_string_attack)
- [Buffer Overflow Basics](https://owasp.org/www-community/vulnerabilities/Buffer_Overflow)

## 👨‍💻 Author

**12bijaya**

---

**Disclaimer**: This tool is for educational and authorized security testing purposes only. Unauthorized access to computer systems is illegal.
