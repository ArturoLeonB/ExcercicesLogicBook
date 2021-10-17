class Loops:
# Read a number and show all numbers between 1 and their. (ex. 1)

    def read_all_numbers_to_num(self, num):
        if num < 1:
            for i in range (num, 1+1):
                return i
        else:
            for i in range(1, num+1):
                return i

 # Read an integer number and show all pair between. (ex. 2)
    def pair_list(self, num):
        aux = 2

        if num > 0:
            for i in range (aux, num+1, 2):
                return i
        else:
            for i in range (aux, num-1, -2):
                return i

#Read a number and show all divisors between 1 and num. (ex. 3)

    def all_submultiples(self, num):
        for i in range(1, num+1):
            if (num % i) == 0:
                return i

#Reed two numbers and show all int between (ex. 4).

    def all_int_between(self, num1, num2):
        for i in range(num2, num1):
            return i
        for i in range(num1, num2):
            return i

#Read two numbers and show all number ending in 4 between their. (ex. 5)

    def all_numbers_ends_4(self, num1, num2):
        for i in range(num2, num1):
            return i % 10 == 4

        for i in range(num1, num2):
            return i % 10 == 4
