
def number_0f_ones(n):
    n, factors, count, remainder = num, 1, 0, 0
   # The function initializes variables n, factors, count, and remainder based on the input value num.


    while n > 0:
        temp = factors
        #For each digit position, it calculates the remainder based on three cases: if the digit is 0, > 1, or == 1
        if n % 10 == 0:
            remainder = 0
        elif n % 10 > 1:
            remainder = temp
        elif n % 10 == 1:
            remainder = (num% temp) + 1

        factors *= 10  
        #The factors variable is incremented to move to the next digit position (tens, hundreds, etc.).


        count += (num // factors) * temp + remainder
        #The count is updated based on the calculated remainder and the number of occurrences of '1' at the current digit position.
        n //= 10

    return count
num = int(input("enter  the number"))
print(number_0f_ones(num))

