import pandas as pd

# Step 1: Create sample CSV file
data = {
    "title": ["Book A", "Book B", "Book C", "Book D"],
    "author": ["Author X", "Author Y", "Author X", "Author Z"],
    "edition": ["1st", "2nd", "3rd", "1st"],
    "publication_year": [2018, 2020, 2021, 2019],
    "publishing_house": ["House1", "House2", "House1", "House3"],
    "price": [250, 300, 150, 500]
}

df = pd.DataFrame(data)
df.to_csv("books.csv", index=False)   # Creates books.csv file
print("✅ books.csv created successfully!\n")

# Step 2: Read the CSV file
df = pd.read_csv("books.csv")

# a) Print complete report
print("\nComplete Report of Books:")
print(df.to_string(index=False))

# b) Books by a given author
author = input("\nEnter author name: ")
print(df[df['author'] == author])

# c) Books by a given publishing house
pub_house = input("\nEnter publishing house: ")
print(df[df['publishing_house'] == pub_house])

# d) Cheapest & costliest book
cheapest = df.loc[df['price'].idxmin()]
costliest = df.loc[df['price'].idxmax()]
print("\nCheapest Book:", cheapest['title'])
print("Costliest Book:", costliest['title'])

# e) Sort by year of publication
print("\nBooks Sorted by Year:")
print(df.sort_values(by='publication_year'))