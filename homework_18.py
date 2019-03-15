import pandas as pd
df=pd.read_excel("data_tasks.xlsx", sheet_name="task1")

# 1
import matplotlib.pyplot as plt
import numpy as np
line, caps, bars = plt.errorbar(
	[df.values[:, 0]],
	[df.values[:, 1]],
	yerr = [df.values[:, 2]],
	fmt = "bs--",
	linewidth = 3,
	elinewidth = 0.5,
	ecolor = "k",
	capsize = 5,
	capthick = 1
	)

plt.legend(["Standard Deviation of Temperature"], numpoints = 1,
	   loc = ("upper left"))
plt.xlim((0, 10))
plt.xticks(np.linspace(1, 9, 9))
plt.yticks(np.linspace(0, 30, 7))
plt.title("Temperature and Standard Deviation", fontweight = "bold")
plt.xlabel("Time Point (Minute)", fontweight = "bold")
plt.ylabel("Temperature (C)", fontweight = "bold")
plt.savefig("task1_part1.png", dpi = 600)
plt.show()


# 2
x = df.values[:, 0]
temperature = df.values[:, 1]
standDev = df.values[:, 2]
plt.bar(x, temperature, yerr = standDev, align = "center", ecolor = "black",
	capsize = 10)
plt.xticks(x,[1, 2, 3, 4, 5, 6, 7, 8, 9])
plt.yticks(np.linspace(0, 30, 7))
plt.title("Temperature and Standard Deviation", fontweight = "bold")
plt.xlabel("Time Point (Minute)", fontweight = "bold")
plt.ylabel("Temperature (C)", fontweight = "bold")
plt.savefig("task1_part2.png", dpi = 600)
plt.show()


# 3
df=pd.read_excel("data_tasks.xlsx", sheet_name="task2")

line, caps, bars = plt.errorbar(
       [df.values[1:, 0]],
       [df.values[1:, 1]],
       yerr = [df.values[1:, 2]],
       fmt = "rs--",
       linewidth = 3,
       elinewidth = 0.5,
       ecolor = "k",
       capsize = 5,
       capthick = 1
       )
line, caps, bars = plt.errorbar(
       [df.values[1:, 0]],
       [df.values[1:, 3]],
       yerr = [df.values[1:, 4]],
       fmt = "bs--",
       linewidth = 3,
       elinewidth = 0.5,
       ecolor = "k",
       capsize = 5,
       capthick = 1
       )
line, caps, bars = plt.errorbar(
       [df.values[1:, 0]],
       [df.values[1:, 5]],
       yerr = [df.values[1:, 6]],
       fmt = "gs--",
       linewidth = 3,
       elinewidth = 0.5,
       ecolor = "k",
       capsize = 5,
       capthick = 1
       )
plt.legend(["Las Vegas", "Durango", "Denver"], loc = "best")
plt.savefig("task1_part3.png", dpi = 600)
plt.yticks(np.linspace(0, 60, 13))
plt.title("Temperature and Standard Deviation of Cities", fontweight = "bold")
plt.xlabel("Time Point (Hour)", fontweight = "bold")
plt.ylabel("Temperature (C)", fontweight = "bold")
plt.savefig("task1_part3.png", dpi = 600)
plt.show()



# 4
barWidth = 0.25

bars1 = df.values[1:, 1]
bars2 = df.values[1:, 3]
bars3 = df.values[1:, 5]

bars1_err = df.values[1:, 2]
bars2_err = df.values[1:, 4]
bars3_err = df.values[1:, 6]

r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]

plt.bar(r1, bars1, color = "red", width = barWidth, edgecolor = "white",
	label = "Las Vegas", yerr = bars1_err, capsize = 5)
plt.bar(r2, bars2, color = "blue", width = barWidth, edgecolor = "white",
        label = "Durango", yerr = bars2_err, capsize = 5)
plt.bar(r3, bars3, color = "green", width = barWidth, edgecolor = "white",
        label = "Denver", yerr = bars3_err, capsize = 5)

plt.title("Temperature and Standard Deviation of Cities", fontweight = "bold")
plt.ylabel("Temperature (C)", fontweight = "bold")
plt.xlabel("Time Point (Hour)", fontweight = "bold")
plt.xticks([r + barWidth for r in range(len(bars1))], [1, 2, 3, 4, 5, 6, 7, 8, 9])
plt.yticks(np.linspace(0, 60, 13))
plt.legend()
plt.savefig("task1_part4.png", dpi = 600)
plt.show()
