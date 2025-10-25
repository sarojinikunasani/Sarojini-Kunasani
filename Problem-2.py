# Take input from user
a = int(input("Enter a number: "))

# Generate the series of first 'a' odd numbers
series = [str(2*i + 1) for i in range(a)]

# Print the series separated by commas
print(", ".join(series))
