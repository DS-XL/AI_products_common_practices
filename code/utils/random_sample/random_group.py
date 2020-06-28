import numpy as np


def select_student_groups(group_list, size, probability):
    probability = np.divide(probability, sum(probability))
    choice = np.random.choice(group_list, size=size, replace=True, p=probability)
    return choice


def print_format(text):
    print(" ")
    print("=start=" * 20)
    print(text)
    print("=end=" * 20)
    print(" ")

if __name__ == "__main__":
    # Set up
    group_list = [1, 2, 3, 4]
    size = 2
    probability = [1] * len(group_list) # [1, 1, 1, 1]

    # Select
    choice = select_student_groups(group_list, size, probability)

    # Output
    text = """
    choice of the group:
    {0}
    """.format(choice)
    print_format(text)


