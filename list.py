#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

integer = int(input("Enter the number of integers you want to add to the list: "))
integers = []

for i in range(integer):
    value = int(input(f"Enter integer {i + 1}: ")) # Accept user input for each integer
    integers.append(value )

sum_of_integers = sum(integers)
print("The integers in the list are:", integers)
print("The sum of all integers in the list is:", sum_of_integers)