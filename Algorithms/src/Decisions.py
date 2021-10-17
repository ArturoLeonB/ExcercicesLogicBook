class Decisions:

#Read an integer number and determine if it is a number that ends in 4 (ex.1)
    def num_ends_with_4(self, num):
        x = num % 10
        return x == 4


#Read a number and determine if have three digits (ex. 2)
    def num_with_three_digits(self, num):
        return 1000 > num and num > 99 or -1000 < num and num < -99


#Read an number and determine if is negative (ex.3)
    def is_this_number_negative(self, num):
        return num < 0


#Read a number and show sum (ex. 4)
    def sum_digits_number(self, num):
        return (num % 10) + (num // 10)


#Read a number and determine if their two digits are pair (ex. 5)
    def two_digits_pair(self, num):
        return (num % 10) % 2 == 0 and (num // 10) % 2 == 0
