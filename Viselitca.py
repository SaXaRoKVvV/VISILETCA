import random


def choose_word():
    words = ['компьютер', 'программа', 'алгоритм', 'виселица', 'студент']
    return random.choice(words)


def display_state(word, guessed_letters, attempts):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display


def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("🎮 Виселица - Угадай слово!")

    while attempts > 0:
        print(f"\nСлово: {display_state(word, guessed_letters, attempts)}")
        print(f"Попытки: {attempts}")

        guess = input("Введите букву: ").lower()

        if len(guess) != 1:
            print("Введите одну букву!")
            continue

        if guess in guessed_letters:
            print("Уже угадывали!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Есть такая буква!")
        else:
            print("❌ Нет такой буквы!")
            attempts -= 1

        # Проверка победы
        if all(letter in guessed_letters for letter in word):
            print(f"🎉 Победа! Слово: {word}")
            break
    else:
        print(f"💀 Проигрыш! Слово: {word}")


if __name__ == "__main__":
    play_game()