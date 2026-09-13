from PIL import Image
import os


def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path).convert("RGB")

    pixels = image.load()

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = pixels[x, y]

            r = r ^ key
            g = g ^ key
            b = b ^ key

            pixels[x, y] = (r, g, b)

    image.save(output_path)
    print(f"\nEncrypted image saved as: {output_path}")


def decrypt_image(input_path, output_path, key):
    # XOR encryption is reversible.
    # Applying the same operation again decrypts the image.
    encrypt_image(input_path, output_path, key)


def main():
    print("=" * 50)
    print("        IMAGE ENCRYPTION TOOL - TASK 2")
    print("=" * 50)

    print("\n1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("\nEnter your choice (1 or 2): ")

    input_path = input("Enter image path: ")

    if not os.path.exists(input_path):
        print("\nError: Image file not found.")
        return

    while True:
        try:
            key = int(input("Enter encryption key (0-255): "))

            if 0 <= key <= 255:
                break

            print("Please enter a value between 0 and 255.")

        except ValueError:
            print("Please enter a valid number.")

    if choice == "1":
        output_path = input("Enter output path: ")
        encrypt_image(input_path, output_path, key)

    elif choice == "2":
        output_path = input("Enter output path: ")
        decrypt_image(input_path, output_path, key)

    else:
        print("\nInvalid choice.")

    print("=" * 50)


if __name__ == "__main__":
    main()