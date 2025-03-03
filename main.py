import time
import sys


def slow_typing(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def display_intro():
    ascii_art = r"""
  _____       ______                             _   
 |  __ \     |  ____|                           | |  
 | |__) |   _| |__   _ __   ___ _ __ _   _ _ __ | |_ 
 |  ___/ | | |  __| | '_ \ / __| '__| | | | '_ \| __|
 | |   | |_| | |____| | | | (__| |  | |_| | |_) | |_ 
 |_|    \__, |______|_| |_|\___|_|   \__, | .__/ \__|
         __/ |                        __/ | |        
        |___/                        |___/|_|        
    """
    slow_typing(ascii_art, 0.002)
    slow_typing("Welcome to PyEncrypt - Your simple password encryption tool!", 0.05)
    time.sleep(1)


def simple_encrypt(text):
    encrypted = "".join(chr(ord(char) + 3) for char in text)
    return encrypted


def simple_decrypt(text):
    decrypted = "".join(chr(ord(char) - 3) for char in text)
    return decrypted


def password_encryptor():
    slow_typing("Enter your password:", 0.03)
    password = input("→ ")

    encrypted_password = simple_encrypt(password)
    slow_typing("Encrypting...", 0.03)
    time.sleep(1)
    slow_typing(f"Encrypted Password: {encrypted_password}", 0.03)

    slow_typing("Decrypting for verification...", 0.03)
    time.sleep(1)
    decrypted_password = simple_decrypt(encrypted_password)
    slow_typing(f"Decrypted Password: {decrypted_password}", 0.03)

    slow_typing("Do you want to close the app? (y/n)", 0.03)
    choice = input("→ ").strip().lower()
    if choice == "y":
        slow_typing("Closing PyEncrypt...", 0.03)
        time.sleep(1)
    else:
        slow_typing("Restarting PyEncrypt...", 0.03)
        time.sleep(1)
        password_encryptor()


if __name__ == "__main__":
    display_intro()
    password_encryptor()
