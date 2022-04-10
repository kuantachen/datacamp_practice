## Tuple
# Pair up the girl and boy names: pairs
pairs = zip(girl_names, boy_names)

# Iterate over pairs
for idx, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank and names associated with each rank
    print('Rank {}: {} and {}'.format(idx, girl_name, boy_name))

# Create the normal variable: normal
normal = 'simple'

# Create the mistaken variable: error
error = ('trailing comma',)

# Print the types of the variables
print(type(normal))
print(type(error))


## Set
# Find the union: all_names
all_names = baby_names_2011.union(baby_names_2014)

# Print the count of names in all_names
print(len(all_names))

# Find the intersection: overlapping_names
overlapping_names = baby_names_2011.intersection(baby_names_2014)

# Print the count of names in overlapping_names
print(len(overlapping_names))

# Create the empty set: baby_names_2011
baby_names_2011 = set()

# Loop over records and add the names from 2011 to the baby_names_2011 set
for row in records:
    # Check if the first column is '2011'
    if row[0] == '2011':
        # Add the fourth column to the set
        baby_names_2011.add(row[3])

# Find the difference between 2011 and 2014: differences
differences = baby_names_2011.difference(baby_names_2014)

# Print the differences
print(differences)