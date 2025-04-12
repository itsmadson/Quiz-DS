def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# تست با 5 عدد اول
print(list(fibonacci_gen(5)))  # خروجی: [0, 1, 1, 2, 3]

# تست با 10 عدد اول
print(list(fibonacci_gen(10)))  # خروجی: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]