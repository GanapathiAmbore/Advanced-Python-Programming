'''# Python programm to extract mobile number,email from string
string = "Ganapathi's Mobile Number is 9032337137 test@gmail.com" \
         ",address is 1-2-44,testingpro number is 8801091595 is email id abcd@gmail.com" \
         "_123@gmail.com test mobile number is 1234567890"
import re
number = re.findall('[0-9]\d{9}', string)
emails = re.findall('\w[a-zA-Z0-9_.]*@gmail[.]com', string)
#Number validation checking:
for num in number:
    valid_number=re.fullmatch('[6-9]\d{9}',num)
    if valid_number!=None:
        print("Mobile number is valid",num)
    else:
        print("In valid mobile number",num)

#Email validation checking:
for email in emails:
    valid_email=re.fullmatch('\w[a-zA-Z0-9_.]*@gmail[.]com',email)
    if valid_email is not None:
        print("Email is valid",valid_email)
    else:
        print("Invalid Email address!",valid_email)
'''
'''import re
stmt='testingpro is good boy'
output=re.search('@',stmt)
if output!=None:
    print(output)
else:
    print("not found!",output)'''
'''import re
string="hp is good laptop"
output=re.search("good",string)
print("starting position:",output.start())
print("ending position:",output.end())
print("matched word:",output.group())'''

word="ganapthi12345"
import re
print(re.findall('[0-9]',word))
print(re.sub('gan',"@",word))

