//UW Programming competition N. Numerology
//https://codeforces.com/group/CByQ2cxyiu/contest/563409/problem/N
import math

# Function to check if a number is a perfect square
def is_perfect_square(num):
    sqrt = math.isqrt(num)
    return sqrt * sqrt == num

# Read the input integer N
N = int(input())

# Initialize variables to store the lexicographically smallest (a, b)
smallest_a = None
smallest_b = None

# Limit for b (upper bound chosen to handle large numbers efficiently)
# This limit can be adjusted based on practical tests
limit = int(1e6)

# Iterate over possible values of b starting from 1
for b in range(1, limit + 1):
    # Calculate S(b) = b(b + 1)(2b + 1) / 6
    sum_of_squares = b * (b + 1) * (2 * b + 1) // 6
    
    # If the sum of squares exceeds N, break out of the loop
    if sum_of_squares > N:
        break
    
    # Check if N is divisible by the sum of squares
    if N % sum_of_squares == 0:
        a_squared = N // sum_of_squares
        
        # Check if a_squared is a perfect square
        if is_perfect_square(a_squared):
            a = math.isqrt(a_squared)
            
            # Check if this (a, b) is the lexicographically smallest pair
            if smallest_a is None or a < smallest_a or (a == smallest_a and b < smallest_b):
                smallest_a = a
                smallest_b = b

# Print the result if a solution is found
if smallest_a is not None:
    print("YES")
    print(smallest_a, smallest_b)
else:
    print("NO")

#time complexity = O(limit× N^(1/2))
#space complexity = O(1)

        
        
