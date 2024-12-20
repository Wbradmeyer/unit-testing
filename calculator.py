def add(x, y):
    """add numbers"""
    return x + y

def subtract(x, y):
    """subtract numbers"""
    return x - y

def divide(x, y):
    """divide numbers"""
    return x / y

def multiply(x, y):
    """multiply numbers"""
    return x * y

def error(x, y):
    return 0

def count_by(x, n):
    count_list = []
    for i in range(1, n + 1):
        count_list.append(i * x)
    return count_list

def is_single_digit_even(x, y):
    if (x + y) % 2 or (x + y) > 9 or (x + y) < 2:
        return False
    else:
        return True
    
def is_in_num_list(x):
    return x

def bigger_num(x):
    return x

def num_to_power_of(x, y):
    return x ** y

def is_square_root(x, y):
    return True if y * y == x else False