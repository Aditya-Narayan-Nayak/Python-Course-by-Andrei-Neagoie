username = input("what is your name ?")
password = input("what is your password ?")

password_lenght = len(password)
hidden_password = '*' * password_lenght

print(f'{username}, your password {hidden_password}  is {len(password)} letters long')
