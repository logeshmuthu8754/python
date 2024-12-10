name=input()
age=input()
my_adress=input()
print("my name is:",name)
print("my age is:",age)
print("my adress is:",my_adress)


#for loop
for i in range(1,10):
    print(i)


#wile loop
i=1
while (i<10):
    print(i)
    i=i+1

#FizzBuzz 
def FizzBuzz(n):
    for i in range(1,n+1):
        if n<0:
            break
        elif(i%3==0 and i%5==0):
            print("FizzBuzz")
        elif(i%3==0):
            print("Fizz")
        elif(i%5==0):
            print("Buzz")
        else:
            print(i)
FizzBuzz(0)