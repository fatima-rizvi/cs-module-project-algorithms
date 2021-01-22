'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # algo
    # Create a pointer to keep track of our current index
    # Create an array to hold the products
    # Create a product variable to temporarily hold each product. Initialize to 1.
    # Iterate through the array
        # Iterate through the array again
            # If the item is at our current index
                # pass
            # Else
                # Multiple our product variable by the current number
        # Append the product to the products array
        # Increment the current index
        # Reset product to one

    current_i = 0
    all_products = []
    product = 1

    for num in arr:
        for i in range(len(arr)):
            if current_i == i:
                pass
            else:
                product *= arr[i]
        all_products.append(product)
        current_i += 1
        product = 1
    
    return all_products


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
