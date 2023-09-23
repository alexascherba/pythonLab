import random
import time

random.seed(42)
big_list = [random.randint(1, 10000) for _ in range(10**4)]
def buble(arr):
    n = len(arr)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]: #if arr[j] > arr[j+1]: для сортировки по возрастанию пузырьком
                arr[j], arr[j+1] = arr[j+1], arr[j]

stat_time = time.time()
buble(big_list)
end_time = time.time()
print(big_list)
print(f"Время выполнения сортировки {end_time - stat_time}")
