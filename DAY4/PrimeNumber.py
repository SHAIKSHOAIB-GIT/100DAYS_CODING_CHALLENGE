#Write your code below this line 👇
def prime_checker(number):
    for i in range(2, number - 1):
        if n % number == 0:
            print(f"{n} not a prime number")
        else:    
            print(f"{n} prime number")
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
