"""
1. Создай гистограмму для случайных данных, сгенерированных с помощью функции `numpy.random.normal`.

​

# Параметры нормального распределения

mean = 0 # Среднее значение

std_dev = 1 # Стандартное отклонение

num_samples = 1000 # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению

data = np.random.normal(mean, std_dev, num_samples)

2. Построй диаграмму рассеяния для двух наборов случайных данных, сгенерированных с помощью функции `numpy.random.rand`.​

import numpy as np

random_array = np.random.rand(5) # массив из 5 случайных чисел

print(random_array)

3. Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные, найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны​

В поле для ответа загрузи скриншоты сделанных заданий или ссылку на Git.​

Загружай скриншоты в формате изображений (png, jpg или pdf). Чтобы быстро сделать и сохранить скриншот в формате изображения, можешь установить специальную программу, например Joxi.

"""
import matplotlib.pyplot as plt
import numpy as np

mean = 0 # Среднее значение
std_dev = 1 # Стандартное отклонение
num_samples = 1000 # Количество образцов
data = np.random.normal(mean, std_dev, num_samples)

plt.hist(data)
plt.show()


random_arrayX = np.random.rand(5) # массив из 5 случайных чисел
random_arrayY = np.random.rand(5)
print(random_arrayX)
print(random_arrayY)
plt.scatter(random_arrayX, random_arrayY)
plt.show()


