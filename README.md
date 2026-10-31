# Configurable Password Generator

## 1. Project Description
The Configurable Password Generator is a Python-based application that generates secure random passwords according to the user's preferences. Users can choose the password length and select which character types to include.

## 2. Features
- Custom password length.
- Include uppercase letters (A–Z).
- Include lowercase letters (a–z).
- Include numbers (0–9).
- Include special characters.
- Ensures at least one character from each selected category.
- Securely shuffles generated passwords.
- Validates user input.
- Allows generating multiple passwords.
- Does not automatically store generated passwords.

## 3. Technologies Used
- Python 3
- `secrets` module
- `string` module

## 4. How to Run

1. Install Python 3.
2. Save the program as `password_generator.py`.
3. Open a terminal in the project folder.
4. Run the following command:

```bash
python password_generator.py
```

## 5. How It Works

1. The user enters the desired password length.
2. The program asks which character types to include.
3. It selects at least one character from every selected category.
4. Remaining characters are selected securely using `secrets.choice()`.
5. The password characters are securely shuffled.
6. The generated password is displayed on the screen.

## 6. Security Measures
- Uses Python's `secrets` module for cryptographically secure random selection.
- Avoids fixed or predictable password patterns.
- Does not automatically save passwords to files or databases.
- Ensures all selected character categories are represented.

## 7. Input Validation
- Rejects non-numeric password lengths.
- Rejects password lengths below 1.
- Requires at least one character category.
- Ensures password length is sufficient for the selected categories.

## 8. Example

```text
===== PASSWORD GENERATOR =====

Enter password length: 12
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y
Include numbers? (y/n): y
Include special characters? (y/n): y

Generated Password: aB7@kP2#mX9!
Password generated successfully!
```

## 9. Project Structure

```text
Password-Generator/
│
├── password_generator.py
└── README.md
```

## 10. Conclusion

This project demonstrates the use of Python functions, loops, conditional statements, input validation, and secure random generation. It provides a simple and secure way to generate customizable passwords.
