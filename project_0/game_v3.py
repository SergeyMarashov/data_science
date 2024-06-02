def game_core_v3(number: int = 1) -> int:
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
    interval = [1, 101]
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
