import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    while True:
        try:
            length = int(input("Gib die gewünschte Passwortlänge ein (8-50 Zeichen, keine persönlichen Daten!): "))
            if length < 8 or length > 50:
                print("Ungültige Länge! Bitte eine Zahl zwischen 8 und 50 eingeben.")
            else:
                print("Generiertes Passwort:", generate_password(length))
                break
        except ValueError:
                print("Ungültige Eingabe! Bitte nur eine Zahl eingeben, z.B. 12.")
