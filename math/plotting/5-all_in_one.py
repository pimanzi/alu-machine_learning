# first way 
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Data generation
y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Create a 3x2 grid of subplots
plt.figure(figsize=(10, 8))

# 1st Plot (Scatter Plot)
plt.subplot(3, 2, 1)
plt.scatter(x1, y1, color='magenta')
plt.xlabel("Height (in)", fontsize='x-small')
plt.ylabel("Weight (lbs)", fontsize='x-small')
plt.title("Men's Height vs Weight", fontsize='x-small')

# 2nd Plot (Exponential Decay)
plt.subplot(3, 2, 2)
plt.plot(x2, y2)
plt.yscale("log")
plt.xlabel("Time (years)", fontsize='x-small')
plt.ylabel("Fraction Remaining", fontsize='x-small')
plt.title("Exponential Decay of C-14", fontsize='x-small')

# 3rd Plot (Exponential Decay for two different constants)
plt.subplot(3, 2, 3)
plt.plot(x3, y31, label="5730 years", color='blue')
plt.plot(x3, y32, label="1600 years", color='red')
plt.xlabel("Time (years)", fontsize='x-small')
plt.ylabel("Fraction Remaining", fontsize='x-small')
plt.title("Exponential Decay Comparison", fontsize='x-small')
plt.legend()

# 4th Plot (Histogram of Student Grades)
plt.subplot(3, 2, 4)
plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
plt.xlabel("Grades", fontsize='x-small')
plt.ylabel("Number of Students", fontsize='x-small')
plt.title("Project A", fontsize='x-small')

# 5th Plot (Line Plot of Cubes)
plt.subplot(3, 2, (5, 6))  # Span two columns
plt.plot(y0)
plt.xlabel("Index", fontsize='x-small')
plt.ylabel("Cubed Value", fontsize='x-small')
plt.title("Cubic Growth", fontsize='x-small')

# Overall figure title
plt.suptitle("All in One", fontsize='x-small')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the figure
plt.show()

# second way 
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Data generation
y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Create a 3x2 grid of subplots using plt.subplots()
fig, axes = plt.subplots(3, 2, figsize=(10, 8))

# Flatten the axes array for easier iteration
axes = axes.flatten()

# 1st Plot (Scatter Plot)
axes[0].scatter(x1, y1, color='magenta')
axes[0].set_xlabel("Height (in)", fontsize='x-small')
axes[0].set_ylabel("Weight (lbs)", fontsize='x-small')
axes[0].set_title("Men's Height vs Weight", fontsize='x-small')

# 2nd Plot (Exponential Decay)
axes[1].plot(x2, y2)
axes[1].set_yscale("log")
axes[1].set_xlabel("Time (years)", fontsize='x-small')
axes[1].set_ylabel("Fraction Remaining", fontsize='x-small')
axes[1].set_title("Exponential Decay of C-14", fontsize='x-small')

# 3rd Plot (Exponential Decay for two different constants)
axes[2].plot(x3, y31, label="5730 years", color='blue')
axes[2].plot(x3, y32, label="1600 years", color='red')
axes[2].set_xlabel("Time (years)", fontsize='x-small')
axes[2].set_ylabel("Fraction Remaining", fontsize='x-small')
axes[2].set_title("Exponential Decay Comparison", fontsize='x-small')
axes[2].legend()

# 4th Plot (Histogram of Student Grades)
axes[3].hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
axes[3].set_xlabel("Grades", fontsize='x-small')
axes[3].set_ylabel("Number of Students", fontsize='x-small')
axes[3].set_title("Project A", fontsize='x-small')

# 5th Plot (Line Plot of Cubes)
axes[4].plot(y0)
axes[4].set_xlabel("Index", fontsize='x-small')
axes[4].set_ylabel("Cubed Value", fontsize='x-small')
axes[4].set_title("Cubic Growth", fontsize='x-small')

# 6th Plot (Empty placeholder for the last plot)
fig.delaxes(axes[5])  # Remove this axis since we don't need it

# Overall figure title
plt.suptitle("All in One", fontsize='x-small')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Show the figure
plt.show()
