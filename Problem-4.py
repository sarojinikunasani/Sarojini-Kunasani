# Take input from user
a = int(input("Enter a number: "))

# Determine how many odd numbers to generate
if a % 2 == 0:
    count = a - 1  # for even numbers, use previous odd series length
else:
    count = a      # for odd numbers, series length = a
  
# Generate the series of odd numbers
series = [str(2 * i - 1) for i in range(1, count + 1)]

# Print the series with comma
print(", ".join(series))

