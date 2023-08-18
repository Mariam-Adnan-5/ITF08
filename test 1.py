number=int(input("Cheak\n1-palindrome number\n 2- even or odd \n enter choice"))
num=int(input("Enter your number"))
if number==1:
    oeigin=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(oeigin==rev):
        print("palindrome")
    else:
        print("not palindrome")
else:
    if num%2==0:
        print("even")
    else:
        print("odd")