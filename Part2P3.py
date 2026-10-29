import matplotlib.pyplot as plt

x = lambda n: (n / (n + 1)) * (2 + (-1) ** n)

eps = 0.01
L = 3

k = 1
while True:
    n_curr = 2 * k
    if abs(x(n_curr) - L) < eps:
        n0 = n_curr
        break
    k += 1

print(f"Для eps = {eps}: n0 = {n0}")

n_list, x_list = [], []

for n in range(n0, n0 + 200, 2):
    n_list.append(n)
    x_list.append(x(n))

plt.figure(figsize=(10, 5))
plt.scatter(n_list, x_list, color='red', label=f'Подпоследовательность при n >= {n0} (первые 100)')
plt.axhline(y=L, color='green', linestyle='--', label=f'Предел L = {L}')
plt.axhline(y=L - eps, color='gray', linestyle=':', label=f'L - eps ({L - eps})')

plt.title(f'Пункт 3: Подпоследовательность при $n \geq n_0$ ($\epsilon = {eps}$)')
plt.xlabel('Номер $n$')
plt.ylabel('$x_n$')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()