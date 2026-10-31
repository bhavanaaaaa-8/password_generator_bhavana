
import secrets
import string


def get_password_options():
    print("\n===== PASSWORD GENERATOR =====")

    while True:
        try:
            length = int(input("Enter password length: "))

            if length < 1:
                print("Password length must be at least 1.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    character_types = []

    if input("Include uppercase letters? (y/n): ").lower() == "y":
        character_types.append(string.ascii_uppercase)

    if input("Include lowercase letters? (y/n): ").lower() == "y":
        character_types.append(string.ascii_lowercase)

    if input("Include numbers? (y/n): ").lower() == "y":
        character_types.append(string.digits)

    if input("Include special characters? (y/n): ").lower() == "y":
        character_types.append(string.punctuation)

    if not character_types:
        print("Error: Select at least one character type.")
        return None, None

    if length < len(character_types):
        print("Error: Password length must be at least",
              len(character_types), "for the selected types.")
        return None, None

    return length, character_types


def generate_password(length, character_types):

    # Select at least one character from every selected type
    password = []

    for characters in character_types:
        password.append(secrets.choice(characters))

    # Combine all selected character sets
    all_characters = "".join(character_types)

    # Fill the remaining password length
    while len(password) < length:
        password.append(secrets.choice(all_characters))

    # Securely shuffle the password
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def main():

    while True:
        length, character_types = get_password_options()

        if length is not None:
            password = generate_password(length, character_types)

            print("\nGenerated Password:", password)
            print("Password generated successfully!")

        choice = input(
            "\nGenerate another password? (y/n): "
        ).lower()

        if choice != "y":
            print("\nThank you for using Password Generator!")
            break


if __name__ == "__main__":
    main()
