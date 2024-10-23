import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

# Function to generate a key and save it to a file
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key from the key file
def load_key():
    if not os.path.exists("key.key"):
        messagebox.showerror("Error", "Key not found. Generate one first!")
        return None
    with open("key.key", "rb") as key_file:
        return key_file.read()

# Function to encrypt the selected file
def encrypt_file():
    key = load_key()
    if not key:
        return
    fernet = Fernet(key)

    file_path = filedialog.askopenfilename(title="Select File to Encrypt")
    if file_path:
        with open(file_path, "rb") as file:
            original_data = file.read()

        encrypted_data = fernet.encrypt(original_data)

        with open(file_path, "wb") as file:
            file.write(encrypted_data)

        messagebox.showinfo("Success", f"{os.path.basename(file_path)} has been encrypted.")

# Function to decrypt the selected file
def decrypt_file():
    key = load_key()
    if not key:
        return
    fernet = Fernet(key)

    file_path = filedialog.askopenfilename(title="Select File to Decrypt")
    if file_path:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()

        try:
            decrypted_data = fernet.decrypt(encrypted_data)
        except Exception as e:
            messagebox.showerror("Error", "Decryption failed. Incorrect key or corrupted file.")
            return

        with open(file_path, "wb") as file:
            file.write(decrypted_data)

        messagebox.showinfo("Success", f"{os.path.basename(file_path)} has been decrypted.")

# GUI setup
root = tk.Tk()
root.title("File Encryptor & Decryptor")
root.geometry("400x200")
root.resizable(False, False)

# Widgets
label = tk.Label(root, text="File Encryptor & Decryptor", font=("Arial", 16))
label.pack(pady=10)

generate_key_button = tk.Button(root, text="Generate Key", width=20, command=generate_key)
generate_key_button.pack(pady=5)

encrypt_button = tk.Button(root, text="Encrypt File", width=20, command=encrypt_file)
encrypt_button.pack(pady=5)

decrypt_button = tk.Button(root, text="Decrypt File", width=20, command=decrypt_file)
decrypt_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", width=20, command=root.quit)
exit_button.pack(pady=10)

# Run the application
root.mainloop()
