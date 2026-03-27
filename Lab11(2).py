import matplotlib.pyplot as plt
import pandas as pd

# Step 1: Create sample recruitment data
data = {
    "company": ["Microsoft", "Google", "Amazon", "IBM", "Deloitte", "Capgemini", "ATOS Origin", "Amdocs"],
    "recruits": [120, 150, 180, 90, 100, 110, 70, 85]
}

df = pd.DataFrame(data)

# a) Bar chart
plt.bar(df["company"], df["recruits"])
plt.title("New Recruitments")
plt.xlabel("Company")
plt.ylabel("Recruits")
plt.xticks(rotation=45)
plt.show()

# b) Pie chart
plt.pie(df["recruits"], labels=df["company"], autopct="%1.1f%%")
plt.title("Recruitment Distribution")
plt.show()

# c) Customized Pie chart
colors = ["skyblue", "lightgreen", "pink", "orange", "purple", "yellow", "red", "cyan"]
plt.pie(df["recruits"], labels=df["company"], autopct="%1.1f%%", colors=colors, startangle=90)
plt.title("Customized Recruitment Pie Chart")
plt.show()

# d) Doughnut chart (pie chart with a hole)
plt.pie(df["recruits"], labels=df["company"], autopct="%1.1f%%", wedgeprops=dict(width=0.4))
plt.title("Recruitment Doughnut Chart")
plt.show()

# Compare IBM & Amdocs
ibm = df[df["company"] == "IBM"]["recruits"].values[0]
amdocs = df[df["company"] == "Amdocs"]["recruits"].values[0]

plt.bar(["IBM", "Amdocs"], [ibm, amdocs], color=["blue", "green"])
plt.title("IBM vs Amdocs Recruitments")
plt.ylabel("Recruits")
plt.show()