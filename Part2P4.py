import matplotlib.pyplot as plt
from Part2P1 import draw_graphics

x = lambda n: (n / (n + 1)) * (2 + (-1) ** n)

# sup который мы нашли аналитически
sup_x = 3
eps = 0.01

m = 1

# Перебираем номера, пока не найдем m, удовлетворяющий условию
while True:
    if x(m) > sup_x - eps:
        break

    m += 1

# На графике из 5.1 снова рисуем точки. m + 50 штук 
draw_graphics(m+50)
plt.scatter(
    m,
    x(m),
    color='magenta',
    s=100,
    zorder=5,
    label=f'Точка m = {m} ($x_m$ > sup - eps)',
)

plt.title(f'Пункт 4: Проверка критерия точной грани ($\epsilon = {eps}$)')
plt.xlabel('Номер $n$')
plt.ylabel('$x_n$')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()