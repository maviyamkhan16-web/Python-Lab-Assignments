import pandas as pd

# Step 1: Create sample states data
data = {
    "state": ["Maharashtra", "Gujarat", "Rajasthan", "Kerala", "Punjab"],
    "area": [307713, 196024, 342239, 38863, 50362],   # in sq km
    "population": [123000000, 70000000, 78000000, 35000000, 30000000]
}

df = pd.DataFrame(data)
df.to_csv("states.csv", index=False)   # Creates states.csv file
print("✅ states.csv created successfully!\n")

# Step 2: Read the CSV file
df = pd.read_csv("states.csv")

# a) Complete info
print("\nComplete State Information:")
print(df)

# b) Largest area
largest_area = df.loc[df['area'].idxmax()]
print("\nState with Largest Area:", largest_area['state'])

# c) Largest population
largest_pop = df.loc[df['population'].idxmax()]
print("State with Largest Population:", largest_pop['state'])

# d) Population density
df['density'] = df['population'] / df['area']
print("\nPopulation Density of States:")
print(df[['state', 'density']])

# e) Highest population density
highest_density = df.loc[df['density'].idxmax()]
print("\nState with Highest Population Density:", highest_density['state'])