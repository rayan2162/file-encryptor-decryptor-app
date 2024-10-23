# **File Encryptor & Decryptor App**

A simple GUI application built with **Tkinter** to encrypt and decrypt text files using the **Fernet encryption** method from the `cryptography` library.

---

## **Features**

- **Generate Encryption Key**: Creates a key used for encrypting and decrypting files.
- **Encrypt Files**: Protects files by encrypting their contents.
- **Decrypt Files**: Unlocks previously encrypted files using the same key.
- **User-Friendly Interface**: Easy-to-use GUI built with Tkinter.

---

## **How to Use**

### **1. Run the application**

- Download the `app.exe` from the **release** folder.
- Double-click `app.exe` to launch the GUI. No need to install Python or dependencies.

### **2. How to use application features**

1. **Generate Key**:

   - Click **"Generate Key"** to create an encryption key (`key.key`).
   - Save this key securely; it's required for both encryption and decryption.

2. **Encrypt File**:

   - Click **"Encrypt File"** and select a text file.
   - The selected file will be encrypted and overwritten with encrypted content.

3. **Decrypt File**:

   - Click **"Decrypt File"** and select an encrypted file.
   - If the correct key is used, the file will be decrypted successfully.

4. **Exit**:
   - Click **"Exit"** to close the application.

---

## **Dependencies**

If you want to run the **source code** directly, ensure you have the following installed:

1. **Python 3.x**
2. **cryptography library**  
   Install it using:

```bash
   pip install cryptography
```

---

## **Build Instructions**

To generate the `.exe` file from the source code:

1. Install **PyInstaller**:

   ```bash
       pip install pyinstaller
   ```

2. Run the following command:

   ```bash
       pyinstaller --onefile --windowed encryptor_gui.py
   ```

3. The executable will be available in the `/dist` folder.

---

## **Notes**

- Keep the **`key.key`** file safe! Without it, you cannot decrypt encrypted files.
- The encryption method used is **Fernet** from the `cryptography` library, which ensures secure symmetric encryption.

---

## **License**

This project is open-source and free to use.
