import random
import string

def generate_password(length=12):
    # Визначення набору символів: літери, цифри та спецсимволи
    characters = string.ascii_letters + string.digits + string.punctuation
    # Генерація пароля випадковим вибором символів
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        # Запит довжини пароля у користувача
        length = int(input("Введіть довжину пароля: "))

        # Перевірка, чи довжина достатня
        if length < 4:
            print("Довжина повинна бути не менше 4 символів.")
        else:
            print("Ваш згенерований пароль:", generate_password(length))
    except ValueError:
        # Якщо користувач ввів не число
        print("Будь ласка, введіть число.")

