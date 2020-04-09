import math

def isPrime(n):
    if n<2:
        print("{} is not prime number.".format(n))
        return n
    else:    
        for i in range(2,int(math.sqrt(n))+1):
            if n%i==0:
                print("{} is not prime number.".format(n))
                return i        

            elif n%1!=0 and i==int(math.sqrt(n)):
                print("{} is prime number.".format(n))

    print("{} is prime number.".format(n))
            
        

a=int(input('input number: '))
isPrime(a)
