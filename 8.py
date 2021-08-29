p=input("Could you please enter Principal Amount ?:")
n=input("Enter No.of Years  :")
r=input("Rate of interest :")

c=p*n*r/float(100)

s="Principal Amount : %d Number of years  :%d  Rate Of interest : %d" %(p,n,r)

s1="Answer Is : %.2f"%c
print(s)

print(s1)
