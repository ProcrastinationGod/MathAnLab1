import matplotlib.pyplot as plt

x = lambda n: (n / (n + 1)) * (2 + (-1) ** n)

# Нужный нам eps
eps = 0.01
# Верхний предел
L = 3

# Начиная с 2 (т.к. четная подпоследовательность) ищем номер n0 начиная
# с которого члены подпоследовательности попадают в eps-окрестность предела.   

n_curr = 2
while True:
    # Если находим такой n, то прерываем цикл
    if abs(x(n_curr) - L) < eps:
        n0 = n_curr
        break
    n_curr += 2

print(f"Для eps = {eps}: n0 = {n0}")

n_list, x_list = [], []

# Добавляем в списки номера + значения, 100 точек
for n in range(n0, n0 + 100*2, 2):
    n_list.append(n)
    x_list.append(x(n))

plt.figure(figsize=(10, 5))
plt.scatter(n_list, x_list, color='red', label=f'Подпоследовательность при n >= {n0} (первые 100)')
plt.axhline(y=3, color='green', linestyle='--', label='sup $x_n$ / Предел (=3)')
plt.axhline(y=L - eps, color='gray', linestyle=':', label=f'L - eps ({L - eps})')

plt.title(f'Пункт 3: Подпоследовательность при $n \geq n_0$ ($\epsilon = {eps}$)')
plt.xlabel('Номер $n$')
plt.ylabel('$x_n$')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()