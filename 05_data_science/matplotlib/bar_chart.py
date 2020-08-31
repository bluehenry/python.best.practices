import matplotlib.pyplot as plt
import numpy as np

divisions = ['Admin', 'Development', 'Lead', 'HR']
salary = [10, 14,20, 12]
age = [28, 30, 45, 32]

index = np.arange(4)
width = 0.3

plt.bar(index, salary, width, color='green', label='Salary')
plt.bar(index+width, age, width, color='blue', label='Age')
plt.title('Divisions Bar Chart')
plt.xlabel('Divisions')
plt.ylabel('NUmber')
plt.xticks(index+width/2, divisions)
plt.legend(loc='best')
plt.show()

