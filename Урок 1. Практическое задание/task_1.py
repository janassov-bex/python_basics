"""
Задание 1.

Поработайте с переменными, создайте несколько,
выведите на экран, запросите у пользователя несколько чисел и
строк и сохраните в переменные, выведите на экран.

Пример:
Ведите ваше имя: Василий
Ведите ваш пароль: vas
Введите ваш возраст: 45
Ваши данные для входа в аккаунт: имя - Василий, пароль - vas, возраст - 45
"""
digit = 123
name = 'Student'
print(f'Ваше имя {name}, Ваше число: {digit}')

user_name = input('Введте ваше имя:')
user_pass = input('Введте ваш пароль:')
user_age = input('Введте ваш возраст:')

print(f'Ваши данные для входа в аккаунт: имя - {user_name}, пароль - {user_pass}, возраст - {user_age}')

