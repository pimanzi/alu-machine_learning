import numpy as np
import matplotlib.pyplot as plt
np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
fruit_labels = ['Apples', 'Bananas', 'Oranges', 'Peaches']
people_labels = ['Farrah', 'Fred', 'Felicia']
fig, ax = plt.subplots()
ax.bar(people_labels, fruit[0], color=colors[0], label=fruit_labels[0], width=0.5)
ax.bar(people_labels, fruit[1], color=colors[1], label=fruit_labels[1], width=0.5, bottom=fruit[0])
ax.bar(people_labels, fruit[2], color=colors[2], label=fruit_labels[2], width=0.5, bottom=fruit[0] + fruit[1])
ax.bar(people_labels, fruit[3], color=colors[3], label=fruit_labels[3], width=0.5, bottom=fruit[0] + fruit[1] + fruit[2]) 
ax.set_ylabel('Quantity of Fruit')
ax.set_title('Number of Fruit per Person')
ax.set_ylim(0, 80)
ax.set_yticks(np.arange(0, 81, 10))
ax.legend()
plt.show()
