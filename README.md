#🔐 SCT_CS_1 – Caesar Cipher Encryption & Decryption
TASK-01
Create a program that can encrpyt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decrption

Task 01 – Simple Text Encryption Program
This project implements a Caesar Cipher, one of the oldest and simplest text encryption techniques.
The program allows the user to:


🔹 Encrypt a message


🔹 Decrypt a message


🔹 Enter a custom shift value


🔹 Automatically handle alphabetical wrapping (A → Z, Z → A)


🔹 Preserve letter case (uppercase/lowercase)



🚀 Features


Supports both encryption and decryption


User chooses their own shift value


Handles lowercase and uppercase alphabets correctly


Ignores non-alphabet characters (keeps numbers, symbols, spaces unchanged)


Beginner-friendly and easy to extend



🧠 What is the Caesar Cipher?
The Caesar Cipher shifts each letter in the text by a fixed number of positions in the alphabet.
Example with shift = 3:


A → D


B → E


X → A


Z → C


Decryption reverses the process.

📌 How It Works


User selects Encrypt or Decrypt


User enters a message


User enters a shift value


Program processes each character:


If it's a letter → shift it


If not → leave it unchanged




Program prints the result



🛠️ Requirements


Python 3.x


No external libraries needed



📂 Project Structure
SCT_CS_1/
│── SCT_CS_1.py
│── README.md


🖥️ Example Usage
==================================================
  --- CAESAR CIPHER ENCRYPTION/DECRYPTION ---
==================================================

Options:
1. Encrypt a message
2. Decrypt a message
3. Exit

Enter your choice (1-3): 1

Enter the message to encrypt: HELLO WORLD
Enter the shift value (0-25): 3

--------------------------------------------------
Original message: HELLO WORLD
Shift value: 3
Encrypted message: KHOOR ZRUOG
--------------------------------------------------

Options:
1. Encrypt a message
2. Decrypt a message
3. Exit

Enter your choice (1-3): 2

Enter the message to decrypt: KHOOR ZRUOG
Enter the shift value (0-25): 3

--------------------------------------------------
Original message: KHOOR ZRUOG
Shift value: 3
Decrypted message: HELLO WORLD
--------------------------------------------------

Options:
1. Encrypt a message
2. Decrypt a message
3. Exit

Enter your choice (1-3):


🤝 Contributing
Feel free to fork this repository and submit pull requests for improvements!
