'''#Register form
import re
name=input("Enter your Name:")
email=input("Enter your email address:")
password=input("Enter your password:")
confirmpassword=input("Enter confirm password:")
mobilenumber=input("Enter your number:")
if name:
    print("Entered Name:",name)
valid_email = re.fullmatch('\w[a-zA-Z0-9_.]*@gmail[.]com', email)
if valid_email is not None:
    print("Email is valid", valid_email)
else:
    print("Invalid Email address!", valid_email)

if password==confirmpassword:
    print("password matched!",password)
else:
    print("password are not matched!")
valid_number = re.fullmatch('[6-9]\d{9}', mobilenumber)
if valid_number != None:
    print("Mobile number is valid", mobilenumber)
else:
    print("In valid mobile number", mobilenumber)'''

'''#output={G:1,o:1,p:1,i:1,S:1,u:1,n:1,d:1,e:1,r:1}
#output={R:1,e:1,d:2,y:1}
name=input("Enter any name:")
output={}
for char in name:
    output[char]=name.count(char)
print(output)

count={char:name.count(char) for char in name}
print(type(count))
'''
