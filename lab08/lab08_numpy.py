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

#задание 3

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print("shape:", temperatures.shape)
print("ndim:", temperatures.ndim)
print("size:", temperatures.size)
print("temperatures[1,2]:", temperatures[1, 2])
print("первая строка:", temperatures[0])
print("последний столбец:", temperatures[:, -1])
print("первые две строки без 1-го столбца:\n", temperatures[:2, 1:])
print("центр 2x2:\n", temperatures[0:2, 1:3])

#задание 4

matrix = np.arange(1, 26).reshape(5, 5)
top3 = matrix[:3]
print("первые 3 строки, shape:", top3.shape)
print(top3)

last2 = matrix[-2:]
print("последние 2 строки, shape:", last2.shape)
print(last2)

first2cols = matrix[:, :2]
print("первые 2 столбца, shape:", first2cols.shape)
print(first2cols)

block = matrix[1:4, 2:5]
print("строки 1–3, столбцы 2–4, shape:", block.shape)
print(block)

corner = matrix[-2:, -2:]
print("правый нижний 2x2, shape:", corner.shape)
print(corner)