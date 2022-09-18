import pandas as pd
import re
import csv
st = []

## Registering Email
     
def user_name():
    while True:
        email = input('Choose your Username: ')
        pattern = '[A-Za-z][\w._]+@[A-Za-z]+\.[A-Za-z]{2,}[\.]?([A-Za-z]{0}|[A-Za-z]{2,})'
        if re.fullmatch(pattern,email):
            st.append(email)
            break
        else:
            print("Enter a valid username: ")
            
def pass_word():
    while True:
        PW = input("Set your password: ")
        if len(PW) < 5 or len(PW) > 16:
            print("Length of password should be between 5 to 16 characters")
        elif re.search('[0-9]',PW) is None:
            print("Atleast one number should be in password")
        elif re.search('[A-Z]',PW) is None:
             print("Atleast one capital letter should be in password")
        elif re.search('[#.$%^&*@!_]',PW) is None:
              print("Atleast one special character should be in password")
        else:
            st.append(PW)
            break
        
 ##Storing the details of user in the file

def storing():
    rn = open('ASG1.csv','a')
    writer = csv.writer(rn)
    writer.writerow(st)
    rn.close()
    
 ## Login to Email
 
def Login():
    det = 0
    Entry = int(input("Select 1 for Login or any other for Registration: "))
    if Entry == 1:
        Input_1 = input("Enter email ID: ")
        Input_2 = input("Enter password: ")
        df = pd.read_csv('ASG1.csv')
        for j in df.User_ID:
            if j==Input_1:
                det=1
                number = df[df["User_ID"] == Input_1 ].index.values
                if df.at[number[0],"Password"] == Input_2:
                    print("Login is done successfully")
                    det = 2
                    
##Password that you entered is wrong                   
        if det==1:
            Entry = int(input("Your password in incorrect\nPress 1 to Retrieve or any other for reset password: "))
            if Entry == 1:
                for i in df.User_ID:
                    if i == Input_1:
                        a= df[df["User_ID"]==Input_1].index.values
                        print(df.at[a[0],"Password"])
                        
## If User wants to reset password
                        
            else:
                print("Reset Password: ")
                pass_word()
                storing()
                
## If user's input is not in the file,Tell the user to register

        elif det == 0:
            print("This email is not registered\nRegister now")
            user_name()
            pass_word()
            storing()
    else:
        user_name()
        pass_word()
        storing()
    
Login()        
                 
                  
            