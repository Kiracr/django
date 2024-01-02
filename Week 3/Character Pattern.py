character = input("\n Enter a character: ")

# Check if the entered character is a single character and not a vowel
if len(character) == 1 and character.lower() not in 'aeiou':
    for i in range(1, 10):
        if i % 2 !=0:
              line = character * i      
              print(line)
else:
    print("Invalid input! Please enter a single consonant character.")