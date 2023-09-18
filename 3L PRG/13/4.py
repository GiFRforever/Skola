for num in range(2, 1000):
    sum: int = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        print(num)
