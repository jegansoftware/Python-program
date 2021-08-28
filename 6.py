
a=raw_input("Enter Name   :")
b=input("Enter Age  :")
c=raw_input("Have you completed Degree ?")
d=input("Enter Your Mobile No :")

print
print

s="Name  : %s" %a
s1="Age   : %s" %b
s2="Degree: %s" %c
s3="Phone : %s" %d


print("Details have been collected from user")
kk=raw_input("Do you want to display ? ")

if (kk=="Yes") or (kk=="yes") or (kk=="YES"):
    print(s)
    print(s1)
    print(s2)
    print(s3)
else :
    print("Details were stored in Database")


