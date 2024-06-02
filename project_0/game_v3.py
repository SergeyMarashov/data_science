def guesser(number: int = 1) -> int:
    """Угадываем число методом деления интервалов на 2 две равные части 
    (первым загадываем 50, потом либо 25 либо 75 и так далее...)
       Функция принимает загаданное число и возвращает число попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
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


    # Ваш код заканчивается здесь

    return count
def guessing_statistics(guesser) -> dict:
    """Проводит анализ за сколько раз угадываются числа от 1 до 100

    Args:
        guesser ([type]): функция угадывания    

    Returns:
        dict: Keys: количество угадываний; Values: количество чисел из диапазона от 1 до 100
    """
    count_dict = {} # словарь для хранения сохранения количества попыток
    temp_value = 0 # временная переменная количесвта попыток на текущее число
    for i in range(1,101):
        temp_value = guesser(i)
        if not temp_value in count_dict: # если текущего эл. нет в  словаре
            count_dict[temp_value] = 1
        else:
            count_dict[temp_value] += 1 # добавляем ему значение +1
            
    return(dict(sorted(count_dict.items())))
    
print (guessing_statistics(guesser))