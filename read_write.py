with open('munaadan.txt', 'r') as file:
    content = file.read()

modified_content = content.upper()

with open('munaadan.txt', 'w') as file:
    file.write(modified_content)

print(modified_content)