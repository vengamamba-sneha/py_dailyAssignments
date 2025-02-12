# #find the area of rectangle using type conversion and formatting
len=int(input("enter the length of rectangle"))
width=int(input('enter the width of rectangle'))
area=len*width
print(f'area of rectangle {area}')


erm=int(input('enter a number'))
flag=0
for i in range(2,erm-1):
    if(erm%i==0):
        print(" Not Prime")
        flag+=1
        break
if (flag==0):
    print("Prime")



#login , test user, Password@123- login success, invalid credentials, if attempted 3 times, 
# wait for 2 min User name and password-ivalid password
i=0
while(i<3):
    uname=input("Enter the username")
    password=input("Enter the Password")
    if(uname=="Test user" and password=="Password@123"):
        print("Login success")
        break
    else:
        print("Invalid Credentials")
        
        i+=1
        if(i==3):
           print("wait for 2 minutes")
           break
        


    
#4.calculate the tax based on the salary, if the salary is less than 5 lac per annum, 
# tax is 10 percentage,if its more, then its 20 percentage, gross salary , 
# total salary,net salary and tax amount should be printed to the user.

allow=int(input())
basic=int(input())
gross=allow+basic
if(gross<500000):
    tax=(gross*10)//100
else:
    tax=(gross*20)//100
net=gross-tax
print(f'{tax},{net},{gross}')  

#5.calculate attendance percentage, attendend classes/total classes, if 75 and above, allowed or else not allowed.

total=int(input('enter total classes'))
atten=int(input('enter attendence'))
percent=(atten/total)*100
if(percent>75):
    print("allowed")
else:
    print("not alloweed")