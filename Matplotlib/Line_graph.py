import matplotlib.pyplot as plt
days = [1, 2, 3, 4, 5, 6, 7, 8, 9]
max_t = [40, 36, 45, 30, 33, 44, 40, 30, 37]
min_t = [20, 25, 21, 23, 19, 12, 13, 15, 20]
avg_t = []
for i in range(len(max_t)):
    avg_t.append((max_t[i] + min_t[0])/2)


plt.xlabel('Days')
plt.ylabel('Temperature')

plt.plot(days, max_t, label="Max")
plt.plot(days, min_t, label="Min")
plt.plot(days, avg_t, label="Avg")

plt.legend(loc="best", shadow=True)

plt.show()



