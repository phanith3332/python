first_name=input("enter your name: ")
roll_number=input("enter your roll number: ")
username=first_name.lower() + roll_number[-2:]
print("generated user_name: ", username)

'''OUTPUT:
enter your name: phanith
enter your roll number: 25341A05M2
generated user_name:  phanithM2'''

