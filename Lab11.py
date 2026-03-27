import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Create sample sales data
data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "face_cream": [2500, 2600, 3000, 2800, 3500, 4000],
    "face_wash": [1500, 1600, 1700, 1800, 2000, 2200],
    "toothpaste": [5200, 5100, 4800, 5000, 5300, 5500],
    "shampoo": [4200, 4300, 4400, 4500, 4600, 4700],
    "total_profit": [20000, 22000, 25000, 24000, 26000, 28000]
}

df = pd.DataFrame(data)

# a) Line plot of total profit
plt.plot(df["month"], df["total_profit"], marker="o")
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# b) Multiline plot of all product sales
plt.plot(df["month"], df["face_cream"], label="Face Cream")
plt.plot(df["month"], df["face_wash"], label="Face Wash")
plt.plot(df["month"], df["toothpaste"], label="Toothpaste")
plt.plot(df["month"], df["shampoo"], label="Shampoo")
plt.title("Product Sales Data")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

# c) Bar chart for face cream & face wash
plt.bar(df["month"], df["face_cream"], label="Face Cream")
plt.bar(df["month"], df["face_wash"], bottom=df["face_cream"], label="Face Wash")
plt.title("Face Cream & Face Wash Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

# d) Pie chart of total sales per product
total_sales = [
    df["face_cream"].sum(),
    df["face_wash"].sum(),
    df["toothpaste"].sum(),
    df["shampoo"].sum()
]
products = ["Face Cream", "Face Wash", "Toothpaste", "Shampoo"]

plt.pie(total_sales, labels=products, autopct="%1.1f%%")
plt.title("Total Sales Distribution")
plt.show()