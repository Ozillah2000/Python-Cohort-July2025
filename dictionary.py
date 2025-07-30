#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

myDetails = {}

myDetails["name"] = input("Enter your name: ")
myDetails["age"] = int(input("Enter your age: "))
myDetails["Hobby"] = input("Enter your favorite hobby: ")
myDetails["favorite color"] = input("Enter your favorite color: ")

print("Person Information in dictionary form:")
#for key, value in myDetails.items():
    #print(f"{key}: {value}")
print(myDetails)  # Print a new line for better readability
