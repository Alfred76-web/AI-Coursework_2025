
print("=== Days to Seconds Converter ===")
print()

# Get input from user
# Using int() to convert string input to integer
days = int(input("Enter the number of days: "))

# Calculate seconds in the given days
# Logic: 1 day = 24 hours, 1 hour = 60 minutes, 1 minute = 60 seconds
# Formula: days × 24 × 60 × 60 = total seconds
seconds = days * 24 * 60 * 60

# Display the result with formatting
print()
print(f"Number of seconds in {days} days: {seconds:,}")
print()
print("Calculation: {} days × 24 hours × 60 minutes × 60 seconds = {:,} seconds".format(days, seconds))