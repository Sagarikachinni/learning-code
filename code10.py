#functions

'''#creating and calling function
def greet():
    print("hello people!")
greet()'''

'''#function with parameters
def nenu(name):
    print("hi" , name + "!")
nenu("sagarika")
nenu("nandhu")'''

'''#function with return value
def addition(a,b):
    return a+b
sum=addition(2,4)
print("sum is:", sum)'''

'''#check even or odd
def num(number):
    if number %2==0:
      print("it is even")
    else:
       print("it is odd")
num(2)'''

#multiplication table using functions
def tables(num):
    for i in range(1,11):
        print(num,"*",i,"=",num*i)
tables(2)