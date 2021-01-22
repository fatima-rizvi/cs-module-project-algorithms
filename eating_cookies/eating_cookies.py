'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)
    # algorithm
    # If there or 0 or 1 cookies
        # Return 1
    # Create a variable called divisor and set it to 1
    # Create a variable called count and set it to zero
    # Create a variable called quotient and set it to 1 to initialize it
    # Create a while loop that runs as long as the quotient is greater than or equal to 1
        # Take n and floor divide it by the divisor. Set this variable to be the quotient
        # Increment the divisor by 1
        # If quotient is greater than or equal to 1
            # Increment count by one
    # Return count

    # if n <= 1:
    #     return 1
    
    # divisor = 1
    # count = 0
    # quotient = 1

    # while quotient >= 1:
    #     quotient = n // divisor
    #     divisor += 1

    #     if quotient >= 1:
    #         count += 1
    
    # return count

    # if n < 0:
    #     return 0
    # if n == 0:
    #     return 1
    # else:
    #     return eating_cookies(n-1)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
