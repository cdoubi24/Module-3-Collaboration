def good():
    return ["Harry", "Ron", "Hermione"]

things = ["mozzarella", "cinderella", "salmonella"]
print(things)

# Capitalize "cinderella"
print(things[1].capitalize())  # Prints "Cinderella"
print(things)  # The list remains unchanged

# Updating the list
things[1] = things[1].capitalize()
print(things)  # Now the list is updated

# Convert "mozzarella" to uppercase
things[0] = things[0].upper()
print(things)  # Now "MOZZARELLA" is uppercase

# Remove "salmonella"
things.remove("salmonella")
print(things)  # "salmonella" is gone

# Define a generator function that yields odd numbers from range(10)
def get_odds():
    for num in range(10):
        if num % 2 != 0:
            yield num

# Find and print the third odd number
gen = get_odds()
for _ in range(2):
    next(gen)  # Skip first two values
print(next(gen))  # Print the third odd number
