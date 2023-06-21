#Count frequency of character in  a string

string = input("Enter a sentence to count the characters : ")

character_count = {}
for char in string:
    if char in character_count:
        character_count[char] += 1
    else:
        character_count[char] = 1

print("Character frequency: ")

for char, count in character_count.items():
    print(char, ":", count)