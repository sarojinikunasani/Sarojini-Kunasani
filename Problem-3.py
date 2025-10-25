# Take input from user
a = int(input("Enter a number: "))

# Determine the count of odd numbers to print
if a % 2 == 0:
    count = a - 1  # for even a, use previous odd number
else:
    count = a      # for odd a, use a itself
    
# Generate the series
series = [str(2*i + 1) for i in range(count)]

# Print the series separated by commas
print(", ".join(series))
