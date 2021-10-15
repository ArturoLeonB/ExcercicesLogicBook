# Read a int number and show all pair numbers between.

def AllExactDivisors(num):
    if num < 0:
        num = num * -1
    
    def is_divisor(num, divisor):
        return num % divisor == 0
   
    for i in range (1, num+1):
        if is_divisor (num, i):
            print (f"{i},", end="")
AllExactDivisors(-8)