correct_password="12345"

while True:
#ask to enter the pass
    user_input=input("Enter the passsword:")
#see if password is correct
    if user_input==correct_password:
        print("Access granted !")
        #exit the loop if pass is correct 
    else:
        print("Incorrect password")   
