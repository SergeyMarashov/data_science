"""Игар угадай число"""

import numpy as np

number = np.random.randint(1,100)
# кол-во попыток
count = 0
while True:
    count += 1
    predict_number = int(input('угадай число'))
    
    if predict_number > number:
        print('Число должно быть меньше')
        
    elif predict_number < number:
        print('Число должно быть больше')
        
    else:
        print(f'Вы угадали число ! это число = {number} , за {count} попыток')
        break
    
    
