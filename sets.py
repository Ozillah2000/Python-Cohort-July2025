#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

set1 = set()
set2 = set()

# Accept user input for the first set
num_elements = int(input("Enter the number of elements for the first set: "))
for i in range(num_elements):
    element = int(input(f"Enter element {i + 1} for the first set: "))
    set1.add(element)

# Accept user input for the second set
num_elements = int(input("Enter the number of elements for the second set: "))
for i in range(num_elements):
    element = int(input(f"Enter element {i + 1} for the second set: "))
    set2.add(element)

# Find the intersection (common elements) of both sets
common_elements = set1.intersection(set2)

print("The common elements in both sets are:", common_elements)