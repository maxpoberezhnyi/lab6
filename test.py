def words_selection(file_path, threshold):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            filtered_words = [obj.strip() for obj in lines if len(obj) > threshold]

            if filtered_words:
                print(f"Об'єкти з кількістю символів більше {threshold}:")
                for obj in filtered_words:
                    print(obj)
            else:
                print(f"Немає об'єктів з кількістю символів більше {threshold}")
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    

if __name__ == "__main__":
    file_path = r'd:\lab6\txt'
    
    try:
        threshold = int(input("Вкажіть мінімальну кількість символів: "))
    except ValueError:
        print("Введіть число!")
    else:
        words_selection(file_path, threshold)