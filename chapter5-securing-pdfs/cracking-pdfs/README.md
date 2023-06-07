Before running the script, install the following dependencies:
```bash
$ pip install -r requirements.txt
```
Running the script on the [RockYou wordlist](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt):
```bash
$ python pdf_cracker.py foo-protected.pdf rockyou.txt
Guessing password:  28%|██████████████████████████▌                                                                   | 4061847/14344391 [04:59<12:38, 13565.22it/s]
[+] Password found: abc123
```
If you want to use a custom wordlist, you can pass it as an argument:
```bash
$ python pdf_cracker.py foo-protected.pdf wordlist.txt
```