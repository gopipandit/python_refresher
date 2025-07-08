def power(base, exponent):
    return base**exponent

def sqrt(num):
    return round(num**0.5,2)


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_armstrong(num):
    num2 = num
    ln = len(str(num))
    s = 0
    for i in str(num2):
        s += int(i) ** ln
    return s == num



if __name__ == '__main__':
    num = 27

    print(is_prime(num))
