last_num  = int(input("Enter the last number of fibonacci series:"))
print("The fibonacci series is")
a = 0
b = 1
while(b < last_num):
    print(b,end=" ")
    a, b= b, a+b
   

