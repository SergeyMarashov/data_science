import numpy as np

def guesser(number: int = 1) -> int:
    """Угадываем число методом деления интервалов на 2 две равные части 
    (первым загадываем 50, потом либо 25 либо 75 и так далее...)
       Функция принимает загаданное число и возвращает число попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    interval = (1, 101)
    while True:
        count += 1
        predict = sum(interval) // 2
        if number == predict:  # условие выход из цикла
            break
        if number > predict:
            interval = (predict, interval[1])
        elif number < predict:
            interval = (interval[0], predict)

    return count

def cocollecting_statistics(loocking_number):
    """ Функция для сбора статистики расчетов нашего когда.
        Принимает функцию, выдает сообщение о максимальном, минимальном и среднем
        количестве результатов выполнения нашего кода за 1000 запусков
    """
    
    count_lst = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:   
        count_lst.append(loocking_number(number))
    
    print(f'Среднее число попыток {int(np.mean(count_lst))}') # Ожидаемо 6
    print(f'Максимальное количество попыток {max(count_lst)}') # Ожидаемо 8
    print(f'Минимальное количество попыток {min(count_lst)}') # Ожидаемо 1
    
if __name__ == "__main__":
    cocollecting_statistics(guesser)