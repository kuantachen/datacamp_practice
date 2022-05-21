
# Use the console on the right to compare the number of laureates and prizes using the .count_documents() method on a collection (don't forget to specify an empty filter document as the argument!)

filter = {}
client.nobel.prizes.count_documents(filter)
client.nobel.laureates.count_documents(filter)

# =====================================================

# Our MongoClient object is not actually a dictionary, 
# so we can't call keys() to list the names of accessible databases. 
# The same is true for listing collections of a database. 
# Instead, we can list database names by calling .list_database_names() on a client instance, 
# and we can list collection names by calling .list_collection_names() on a database instance.

# Save a list of names of the databases managed by client
db_names = client.list_database_names()
print(db_names)

# Save a list of names of the collections managed by the "nobel" database
nobel_coll_names = client.nobel.list_collection_names()
print(nobel_coll_names)

# =====================================================

# Connect to the "nobel" database
db = client.nobel

# Retrieve sample prize and laureate documents
prize = db.prizes.find_one()
laureate = db.laureates.find_one()

# Print the sample prize and laureate documents
print(prize)
print(laureate)
print(type(laureate))

# Get the fields present in each type of document
prize_fields = list(prize.keys())
laureate_fields = list(laureate.keys())

print(prize_fields)
print(laureate_fields)

# =====================================================

# The "born" field in a laureate collection document records the date of birth of that laureate.
# Using the query format above, what is the number of laureates born prior to 1800? What about prior to 1700?
# ("$lt" is for "less than")

db.laureates.count_documents({"born": {"$lt": "1800"}})
db.laureates.count_documents({"born": {"$lt": "1700"}})

# =====================================================

# Create a filter for laureates who died in the USA
criteria = {"diedCountry": "USA"}

# Save the count of these laureates
count = db.laureates.count_documents(criteria)
print(count)

# Create a filter for laureates who died in the USA but were born in Germany
criteria = {"diedCountry": "USA", 
            "bornCountry": "Germany"}

# Save the count
count = db.laureates.count_documents(criteria)
print(count)

# Create a filter for laureates who died in the USA but were born in Germany
criteria = {"diedCountry": "USA", 
            "bornCountry": "Germany",
            "firstname": "Albert"}

# Save the count
count = db.laureates.count_documents(criteria)
print(count)

# =====================================================

# we wish to find documents where a field's value matches any of a set of options. We saw that the $in query operator can be used for this purpose
# If we wish to accept all but one option as a value for a field, we can use the $ne (not equal) operator

# Save a filter for laureates born in the USA, Canada, or Mexico
criteria = { "bornCountry": 
                { "$in": ["USA", "Canada", "Mexico"]}
             }

# Count them and save the count
count = db.laureates.count_documents(criteria)
print(count)

# Save a filter for laureates who died in the USA and were not born there
criteria = { "diedCountry": "USA",
               "bornCountry": { "$ne": "USA"}, 
             }

# Count them
count = db.laureates.count_documents(criteria)
print(count)

# =====================================================

# If we want to count the number of laureates born in Austria with a prize affiliation country that is not also Austria, what MongoDB concepts/tools should we use
db.doc.count_documents({"prizes.affiliations.bornCity": {"$ne": "Austria"}})

# =====================================================

# We saw from his laureate document that Walter Kohn's country of birth was "Austria" and that his prize affiliation country was "USA". Count the number of laureates born in Austria with a prize affiliation country that is not also Austria.

# Filter for laureates born in Austria with non-Austria prize affiliation
criteria = {"bornCountry": "Austria", 
              "prizes.affiliations.country": {"$ne": "Austria"}}

# Count the number of such laureates
count = db.laureates.count_documents(criteria)
print(count)

# =====================================================

# Filter for documents without a "born" field
criteria = {"born": {"$exists": False}}

# Save count
count = db.laureates.count_documents(criteria)
print(count)

# =====================================================

# Use a filter document (criteria) to find a document for a laureate with at least three elements in its "prizes" array. In other words, does a third element exist for the array? Remember about the zero-based indexing!

# Filter for laureates with at least three prizes
criteria = {"prizes.2": {"$exists": True}}

# Find one laureate with at least three prizes
doc = db.laureates.find_one(criteria)

# Print the document
print(doc)

# =====================================================

# =====================================================

# =====================================================

# =====================================================

# =====================================================

# =====================================================

# =====================================================