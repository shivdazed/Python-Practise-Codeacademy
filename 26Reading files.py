random_file = open("/Users/purnimagebhardt/Downloads/mtcars.csv","r")

print(random_file.readable())

print(random_file.readline())

for line in random_file.readlines():
    print(line,"\n")

random_file.close()
