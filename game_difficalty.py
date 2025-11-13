import random
from datetime import datetime

# Словари для разных уровней сложности
WORD_LISTS = {
    'легкий': ['кот', 'дом', 'сад', 'нос', 'рот', 'сон', 'мир', 'час', 'брат', 'цвет'],
    'средний': ['программа', 'компьютер', 'библиотека', 'телефон', 'солнце', 'погода'],
    'сложный': ['электричество', 'достопримечательность', 'самостоятельность', 'благополучие']
}

# Максимальное количество ошибок для каждого уровня
MAX_ATTEMPTS = {'легкий': 8, 'средний': 6, 'сложный': 4}


def get_difficulty():
    """Выбор сложности"""
    print("\nВыберите сложность:")
    print("1 - Легкий (8 попыток)")
    print("2 - Средний (6 попыток)")
    print("3 - Сложный (4 попытки)")

    choice = input("Ваш выбор (1-3): ")
    difficulties = {'1': 'легкий', '2': 'средний', '3': 'сложный'}
    return difficulties.get(choice, 'легкий')


def display_word(word, guessed_letters):
    """Отображение слова с угаданными буквами"""
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)


def calculate_score(word, attempts_used, max_attempts, difficulty):
    """Расчет очков"""
    base_score = len(word) * 10
    attempts_bonus = (max_attempts - attempts_used) * 5
    multiplier = {'легкий': 1, 'средний': 2, 'сложный': 3}[difficulty]
    return (base_score + attempts_bonus) * multiplier


def save_score(player, score, word, difficulty):
    """Сохранение счета"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open('scores.txt', 'a', encoding='utf-8') as f:
        f.write(f"{timestamp} | {player} | {difficulty} | {word} | {score}\n")


def play_game():
    """Основная функция игры"""
    difficulty = get_difficulty()
    player_name = input("\nВведите ваше имя: ") or "Игрок"

    word = random.choice(WORD_LISTS[difficulty]).upper()
    max_attempts = MAX_ATTEMPTS[difficulty]
    attempts = 0
    guessed_letters = set()

    print(f"\nИгра началась! Слово из {len(word)} букв. Попыток: {max_attempts}")

    while attempts < max_attempts:
        print(f"\nСлово: {display_word(word, guessed_letters)}")
        print(f"Осталось попыток: {max_attempts - attempts}")

        guess = input("Введите букву: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Введите одну букву!")
            continue

        if guess in guessed_letters:
            print("Вы уже вводили эту букву!")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print("Верно!")

            # Проверка победы
            if all(letter in guessed_letters for letter in word):
                score = calculate_score(word, attempts, max_attempts, difficulty)
                print(f"\nПоздравляем! Вы угадали слово: {word}")
                print(f"Ваш счет: {score} очков")
                save_score(player_name, score, word, difficulty)
                return
        else:
            attempts += 1
            print("Не угадали!")

    # Проигрыш
    print(f"\nИгра окончена! Загаданное слово: {word}")
    save_score(player_name, 0, word, difficulty)


def main():
    """Главное меню"""
    while True:
        print("\n=== ВИСЕЛИЦА ===")
        print("1 - Новая игра")
        print("2 - Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            play_game()
        elif choice == '2':
            print("До свидания!")
            break
        else:
            print("Неверный выбор!")


if __name__ == "__main__":
    main()