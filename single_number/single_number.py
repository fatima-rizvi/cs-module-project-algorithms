'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# Requirement: O(1) space complexity

def single_number(arr):
    # First pass
    # # Create a counter variable dictionary
    # # Count frequency of numbers 
    # # Search through the counter to find the frequency of 1
    # # Return number that has a frequency of one
    # frequency = {}
    # for num in arr:
    #     # If num is not in the counter dictionary yet, then make it's value 1
    #     if num not in frequency:
    #         frequency[num] = 1
    #     # If num is already in counter, increment count by one
    #     else:
    #         frequency[num] += 1
    
    # for num, count in frequency.items():
    #     if count == 1:
    #         return num

    #Optimized 
    frequency = {}
    for num in arr:
        # If num is already in counter, increment count by one
        if frequency[num]:
            frequency[num] += 1
        # If num is not in the counter dictionary yet, then make it's value 1
        else:
            frequency[num] = 1
    
    for num, count in frequency.items():
        if count == 1:
            return num

    # Optimized (Doc)
    # answer = 0
    # for x in arr:
    #     answer ^= x   #bitwise operator
    #     print(answer)
    # return answer

    # Joanne's Optimized
    # count = {}
    # for num in arr:
    #     if count.get(num):
    #         del count[num]
    #     else:
    #         count[num] = 1
    # return next(iter(count.keys()))

    #Ava's Optimized
    # freq = {}
    
    # for num in arr:
    #     if freq.get(num):
    #         # freq[num] += 1
    #         del freq[num]   # this is faster, if it's in the dictionary it's obvs in there more than once
    #     else:
    #         freq[num] = 1
    
    # return next(iter(freq.keys())) #O(n)

    #Alt
    # Sort Array in place
    # Look check if first 2 match, then check the next two until they don't match
    # If they don't match, return the first number
    # If it's the last item, the loop will complete before it covers the last item, so we return the last item

    #Note: .count() seems to be O(n) for space/time complexity

    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")