n = int(input("Enter time: "))
a = n // 3600
b = (n - 3600 * a) // 60
c = n - 3600 * a - 60 * b
print(f"{a}:{b}:{c}")
