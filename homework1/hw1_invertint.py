def reverse(number):
    n2 = 0
    n1 = number
    while n1 > 0:
        digit = n1 % 10;  # находим остаток - последнюю цифру числа
        n1 = n1 // 10;  # делим нацело - убираем из числа последнюю цифру
        n2 = n2 * 10  # увеличиваем разрядность второго числа
        n2 = n2 + digit  # добавляем очередную цифру
    return n2
    raise NotImplementedError
