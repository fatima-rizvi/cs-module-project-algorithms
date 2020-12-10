'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Pseudo code, algorithm
    # Make a left & right pointer
    # Iterate through arr
        # Continue while left <= right
    # if num at pointer is not 0, move it to the front of array
        # Pop and push it
        # But a better solution would be to swap it
    # If num is a 0, leave it in place
        # Decrement right pointer if it's a zero
    # Increment left pointer in both if's
    # Return arr

    # Doc's solution
    # def moving_zeroes(arr):
    left = 0    # Left pointer points at the start
    right = len(arr) - 1    # Right pointer at the the end
    while left <= right:    # While the pointers haven't crossed each other
        if arr[left] == 0 and arr[right] != 0:  # If the left num is 0 and right num is not 0
            arr[left], arr[right] = arr[right], arr[left] # Swap them (Unpacking/destructuring)
            left += 1   # Increment the left pointer up by one
            right -= 1  # Decrement the right pointer down by one
        else:   # If the condition on line 23 isn't met 
            if arr[left] != 0:  # If the left num is NOT zero
                left += 1   # Increment the left pointer up by one
            if arr[right] == 0: # If the right num is NOT zero
                right -= 1  # Increment the right pointer down by one
    return arr  # Return the array, all of the zeroes should now be on the right

    # Harry's solutions (2):
    # O(n) space and O(n) time, non-destructive
    # def moving_zeros_o_n(array):
    #     new_array = []
    #     for number in array:
    #         if number != 0:
    #             new_array.append(number)
    #     return new_array + [0] * (len(array) - len(new_array))
    # # O(n) space O(n) time using a list comprehension, non-destructive
    # def moving_zeros_o_n_comprehension(array):
    #     new_array = [x for x in array if x != 0]
    #     return new_array + [0] * (len(array) - len(new_array))

    # THE SOLUTION BELOW DIDN'T WORK
    # left_index = 0
    # right_index = len(arr) - 1

    # while left_index <= right_index:
    #     # if arr[left_index] == 0 and arr[right_index] != 0:
    #     #     arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
    #     if arr[left_index] != 0:
    #         arr[left_index], arr[0] = arr[0], arr[left_index]

    #         #Long version of line 24 for clarity
    #         # temp = arr[left_index]
    #         # arr[left_index] = arr[0]
    #         # arr[0] = temp

    #         # JavaScript version
    #         # (arr[left_index], arr[0]) = (arr[0], arr[left_index])

    #     left_index += 1
    #     # This will break if I swap them, I need to only move it to the front,not potentially move another non-zero number to this position.
    #     # There was a misunderstanding what I thought I could do while swapping. Back to pop/push
    #     if arr[right_index] != 0:
    #         arr[right_index], arr[0] = arr[0], arr[right_index]



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")