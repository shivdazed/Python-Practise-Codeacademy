def translate(phrase):

    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G\t"
            else:
                translation = translation + "g\t"
        else:
            if letter.isupper():
                translation = translation + "T\t"
            else:
                translation = translation + "t\t"

    return translation


print(translate(input("Enter phrase ----------I:")))

print(translate(input("Enter phrase ---------II:")))