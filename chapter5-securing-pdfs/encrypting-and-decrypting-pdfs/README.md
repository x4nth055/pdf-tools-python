Before running the scripts, install the required dependencies:
```bash
$ pip install -r requirements.txt
```
Encrypting the [Chapter_2_Building_Malware.pdf](Chapter_2_Building_Malware.pdf) file with the password `0123456`:
```bash
$ python encrypt_pdf.py Chapter_2_Building_Malware.pdf 0123456
```
The encrypted file is saved as `encrypted_Chapter_2_Building_Malware.pdf`.

Decrypting the encrypted file with the correct password:
```bash
$ python decrypt_pdf.py encrypted_Chapter_2_Building_Malware.pdf 0123456
Password correct, decrypting...
```
A new file named `decrypted_encrypted_Chapter_2_Building_Malware.pdf` is created.

Decrypting the encrypted file with the wrong password:
```bash
$ python decrypt_pdf.py encrypted_Chapter_2_Building_Malware.pdf 0123456789
Password incorrect!
```