def sayhi():
    print("Hello User")

def say_hi(n,a):
    name = str(n)
    age = int(a)
    print("Your name is "+name+" and you are",age)

sayhi()
say_hi(input("Enter your name:"),int(input("and also enter your age:")))