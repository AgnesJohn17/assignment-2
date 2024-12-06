# Enter input values
values = list(map(int, input("Enter the values: ").split()))

# Calculating the average
average = sum(values) / len(values)

# Counting values above or equal to average and below average
above_or_equal = 0
below = 0

for value in values:
    if value >= average:
        above_or_equal += 1
    else:
        below += 1

# Counting occurrences of each value
occurrences = {}
for value in values:
    if value in occurrences:
        occurrences[value] += 1
    else:
        occurrences[value] = 1

# Print results
print(f"Average is {average}")
print(f"Number of values above the average {above_or_equal}")
print(f"Number of values below the average {below}")

# Iterate over the occurrences
for value, count in occurrences.items():
   
    if count == 1:
        time_word = "time"
    else:
        time_word = "times"
   
    # Printing the result
    print(f"{value} occurs {count} {time_word}")