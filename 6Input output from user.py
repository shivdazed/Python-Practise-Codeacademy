name =input("Enter your name : ")
print("Hello "+name+"\n")

age = int(input("Enter your age please:\n"))

if age >=18:
    print("Records indicate that you are an adult of legal age:-",age)
elif age<18:
    print("Sorry you are not old enough;age:-",age)
else:
    print("Please enter a valid input")
