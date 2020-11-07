"""Задания по ветвлениям, итерациям и вводу данных."""

# напиши функцию, которая принимает на вход любое
# количество чисел и сообщает, есть ли среди них чётное
def is_even():
    
    num_list = input('Введите числа через пробел: ')
    
    for counter in num_list.split(' '):
        
        if int(counter) % 2 == 0:
            print('В этом списке есть четное число')
            break

# используй тернарный оператор, чтобы вызвать функцию
# если возраст больше 21 года, в противном случае верни
# сообщение "Мы не продаём алкоголь несовершеннолетним."
age = 17
print("Мы не продаём алкоголь несовершеннолетним.") if age < 21 else sell_alcohol()


# напиши функцию, которая проверит, является ли строка ключевым словом в Питоне
# тебе понадобится модуль keyword, импортируй его и изучи с помощью dir()
def function_keyword():
    import keyword
    string = input()
    print('String is indeed a keyword in Python') if keyword.iskeyword(string) else print('String is not a keyword')
import keyword
print(keyword.kwlist)
function_keyword()

# напиши функцию, которая возвращает тип данных на русском языке:
# число, строка, булевый, None, список, кортеж, множество, словарь
# пример: get_type("что-то") возвращает "Это строка."
# пример2: get_type(42) возвращает "Это словарь."

def get_type(your_var):                  
    if type(your_var) == int:    
        return 'Это число'                   
    elif type(your_var) == bool: 
        return 'Это булевый'                  
    elif type(your_var) == str:  
        return 'Это строка'                   
    elif type(your_var) == list: 
        return 'Это список'                  
    elif type(your_var) == tuple:
        return 'Это кортеж'  
    elif type(your_var) == float:
        return 'Это число'           
    elif type(your_var) == set:
        return 'Это множество'   
    elif type(your_var) == dict:
        return 'Это словарь'               
    else: 
        print("Ты че в меня впихнул, эээ")