import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5, 6, 7, 8, 9]
temp = [40, 36, 45, 30, 33, 44, 40, 30, 37]

plt.xlabel('Days')
plt.ylabel('Temperature')

plt.title('Weather')

plt.plot(days, temp, 'go:')

plt.show()
