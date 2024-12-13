user_input = input("Enter filename: ")
with open(user_input, 'r') as file:  # Vulnerable to directory traversal
    content = file.read()
