import numpy as np

#задание 1

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

#задание 2

print("третий:", hours[2])
print("последний:", hours[-1])
print("индексы 2–5:", hours[2:6])
print("каждый второй:", hours[::2])
print("обратный порядок:", hours[::-1])

