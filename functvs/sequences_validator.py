def is_perfect(n):
    summation = 0
    for i in range(1, n):
        if n % i == 0:
            summation += i
    return summation == n
