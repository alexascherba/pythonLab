import random

def IsOddNumber(N):
    if N % 2 != 0:
        return True

a1 = random.randint(1,100)
a2 = random.randint(1,100)
a3 = random.randint(1,100)
a4 = random.randint(1,100)
a5 = random.randint(1,100)

print(f"Число {a1} нечетное: {IsOddNumber(a1)}")
print(f"Число {a2} нечетное: {IsOddNumber(a2)}")
print(f"Число {a3} нечетное: {IsOddNumber(a3)}")
print(f"Число {a4} нечетное: {IsOddNumber(a4)}")
print(f"Число {a5} нечетное: {IsOddNumber(a5)}")
