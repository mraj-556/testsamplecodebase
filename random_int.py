import random

# Generate a random integer between a specified range (inclusive)
# Example: a random integer between 1 and 10 (inclusive)
random_integer = random.randint(1, 10)
print(f"Random integer between 1 and 10: {random_integer}")

# Generate a random floating-point number between 0.0 and 1.0 (exclusive of 1.0)
random_float = random.random()
print(f"Random float between 0.0 and 1.0: {random_float}")

# Generate a random floating-point number within a specified range
# Example: a random float between 1.0 and 5.0
random_uniform = random.uniform(1.0, 5.0)
print(f"Random float between 1.0 and 5.0: {random_uniform}")

# Select a random element from a list
my_list = ['apple', 'banana', 'cherry', 'date']
random_item = random.choice(my_list)
print(f"Random item from list: {random_item}")

# Shuffle a list in place
random.shuffle(my_list)
print(f"Shuffled list: {my_list}")

# Generate a list of unique random elements from a sequence
# Example: select 3 unique random elements from range(10)
random_sample = random.sample(range(10), 3)
print(f"Random sample of 3 unique elements from range(10): {random_sample}")

# --- New functionality: Generate a random float with user-specified precision ---
print("\n--- Generating a random float with user-defined precision ---")
try:
    precision_input = input("Enter desired number of decimal places for the random float (e.g., 2, 3): ")
    precision = int(precision_input)

    if precision < 0:
        print("Warning: Precision cannot be negative. Using 0 decimal places (integer).")
        precision = 0

    # Generate a random float within a specified range (e.g., 0.0 to 100.0)
    # The range can be adjusted as needed, but 0-100 provides a good demonstration.
    random_float_with_precision = random.uniform(0.0, 100.0)
    
    # Round the generated float to the specified number of decimal places
    rounded_float = round(random_float_with_precision, precision)
    
    print(f"Original random float (0.0 to 100.0): {random_float_with_precision}")
    print(f"Random float rounded to {precision} decimal places: {rounded_float}")

except ValueError:
    print("Invalid input for precision. Please enter an integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
