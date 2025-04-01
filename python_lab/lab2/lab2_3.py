import random

# Розмірність масиву (10 вагонів, 20 місць в кожному)
rows = 10
cols = 20

# Функція для генерації масиву
def generate_train_seats():
    # Генерація масиву 10x20 з випадковими 0 і 1
    train = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
    return train

# Функція для виведення масиву (зайнятих та вільних місць)
def print_train(train):
    for i in range(rows):
        print(f"Вагон {i + 1}: ", " ".join(str(train[i][j]) for j in range(cols)))

# Функція для перевірки, чи є вільні місця в обраному вагоні
def check_free_seats(train, wagon_number):
    if wagon_number < 1 or wagon_number > rows:
        print("Некоректний номер вагона!")
        return
    # Перевірка на наявність вільних місць у вибраному вагоні
    free_seats = train[wagon_number - 1].count(0)
    if free_seats > 0:
        print(f"У вагоні {wagon_number} є {free_seats} вільних місць.")
    else:
        print(f"У вагоні {wagon_number} немає вільних місць.")

# Основна програма
def main():
    # Генерація інформації про місця
    train = generate_train_seats()
    
    # Виведення масиву місць
    print("Інформація про місця у потязі:")
    print_train(train)
    
    # Введення номера вагона для перевірки
    wagon_number = int(input("\nВведіть номер вагона для перевірки вільних місць: "))
    
    # Перевірка вільних місць у вибраному вагоні
    check_free_seats(train, wagon_number)

# Запуск програми
if __name__ == "__main__":
    main()
