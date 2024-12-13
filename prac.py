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
FizzBuzz(20)

#factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5)) 



#even number
def is_even(num):
    return num % 2 == 0

print(is_even(10))  
print(is_even(7)) 



#factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))



#celsius
def celsius(celsius):
    return (celsius * 9/5) + 32

print(celsius(25))


#largest of three
def largest_of_three(a, b, c):
    return max(a, b, c)

print(largest_of_three(5, 10, 7))


#positive or negative
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(-5))

#swap sum
def swap_numbers(a, b):
    a, b = b, a
    return a, b

print(swap_numbers(3, 7))

#prime number
def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(prime(17)) 
print(prime(18))



def count_word_occurrences(str1,tstr):
    arr=list(str1)
    count=str1.count(tstr)
    print(count)
count_word_occurrences("logesh muthu playing the game","the") 



def maxInArray(arr):
    if arr is  None:
        print("")
    elif len(arr)==0:
        print("")
    else:
        print(max(arr))
	
maxInArray([6,1,3,15,2,0])