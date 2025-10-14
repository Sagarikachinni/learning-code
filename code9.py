'''#printing numbers 
count =1
while count <=10 :
    print("count:",count)
    count +=1'''

'''#multiplication table
table=int(input("enter a number:"))
for i in range(1,11):
    print(table,"*",i,"=",table*i)'''

#sum of n numbers
n = int(input("Enter how many numbers: "))
total = 0

for i in range(1, n + 1):
    total += i   # total = total + i

print("The sum is:", total)
