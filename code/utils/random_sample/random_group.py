import numpy as np

group_list = [1, 2, 3]
size = 1
probability = [1, 1, 1]
probability = np.divide(probability, sum(probability))

choice = np.random.choice(group_list, size=size, replace=True, p=probability)
print(" ")
print("=start=" * 20)
print("choice of the group:")
print(choice)
print("=end=" * 20)
print(" ")
