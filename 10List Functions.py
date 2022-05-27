
lucky_numbers = [4, 8, 15, 16, 23, 42]

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

friends.extend(lucky_numbers)

print(friends)

friends.append("Creed")

print(friends)

friends.insert(1, "kelly")
print(friends)

friends.remove("Karen")
print(friends)

friends.clear()
print(friends)

friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
friends.pop()
print(friends)

print(friends.index("Jim"))

print(friends.count("Jim"))

friends.sort()
print(friends)

friends.reverse()
print(friends)

friends2 = friends.copy()
print(friends2)