# программа запитує дії для виконання ('зашифрувати' або 'розшифрувати')
# при виборі першої программа імпортує зашифровану компію одного текстового файлу в інший 
# при виборі другої, імпортує розшифровані дані з файлу в інший файл, в розшфрованому вигляду
def encrypt_content(words):
    encrypted_content = ""
    for word in words:
        if word.isalpha():
            encrypted_word = chr((ord(word) - ord('a') + 25) % 26 + ord('a'))
            encrypted_content += encrypted_word
        else:
            encrypted_content += word
    return encrypted_content

def decrypt_content(words):
    decrypted_content = ""
    for word in words:
        if word.isalpha():
            decrypted_word = chr((ord(word) - ord('a') - 25) % 26 + ord('a'))
            decrypted_content += decrypted_word
        else:
            decrypted_content += word
    return decrypted_content

def encrypt_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            words = input_file.read().split()

            encrypted_words = [encrypt_content(word.lower()) for word in words]

            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(" ".join(encrypted_words))

            print(f"Результат збережено у файлі: {output_file_path}")
    except Exception as e:
        print(f"Виникла помилка: {e}")

def decrypt_file(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            words = input_file.read().split()

            decrypted_words = [decrypt_content(word.lower()) for word in words]

            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(" ".join(decrypted_words))

            print(f"Результат збережено у файлі: {output_file_path}")
    except Exception as e:
        print(f"Виникла помилка: {e}")

if __name__ == "__main__":
    operation = input("Введіть операцію ('зашифрувати' або 'розшифрувати'): ").lower()

    if operation == 'зашифрувати':
        input_file_path = "D:/lab6/txt"
        output_file_path = "D:/lab6/testlab"
        encrypt_file(input_file_path, output_file_path)
    elif operation == 'розшифрувати':
        input_file_path = "D:/lab6/testlab"
        output_file_path = "D:/lab6/testlab2"
        decrypt_file(input_file_path, output_file_path)
    else:
        print("Невірна операція. Виберіть 'зашифрувати' або 'розшифрувати'.")