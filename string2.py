#validate user input exercise
    # user name is no more than 12 characters
    # username must not contains space
    # username must not contains digits

username = input("enter your username : ")
if len(username) > 12 and username.find(" ") == 0 and username.isdigit() == True :
    print("Your username is not valid")
else :
    print(f"Welcome {username}")