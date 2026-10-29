import matplotlib.pyplot as plt

x = lambda n: (n / (n + 1)) * (2 + (-1) ** n)

n_odd, x_odd = [], []
n_even, x_even = [], []

for i in range(1, 101):
    val = x(i)
    
    if i % 2 == 0:
        n_even.append(i)
        x_even.append(val)
    else:
        n_odd.append(i)
        x_odd.append(val)

plt.scatter(n_odd, x_odd, color='blue', label='Нечётные точки')
plt.scatter(n_even, x_even, color='red', label='Чётные точки')

plt.axhline(y=3, color='green', linestyle='--', label='sup $x_n$ / Предел (=3)')
plt.axhline(y=1, color='orange', linestyle='--', label='Предел (=1)')
plt.axhline(y=0.5, color='purple', linestyle='--', label='inf $x_n$ (=0.5)')

plt.title('График последовательности')
plt.xlabel('Номер $n$')
plt.ylabel('$x_n$')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()