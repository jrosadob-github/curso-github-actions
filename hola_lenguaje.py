import os


def main():
    language = os.getenv("LANGUAGE")
    print(f"¡Hola, {language} desde GitHub!")


if __name__ == "__main__":
    main()