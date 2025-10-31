import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Create connection to MySQL
engine = create_engine("mysql+mysqlconnector://salesuser:StrongPassword123@localhost/salesdb")

# Query: total revenue by region
query = "SELECT region, SUM(total_price) AS revenue FROM orders GROUP BY region;"
df = pd.read_sql(query, engine)

# Display data in terminal
print("Revenue by Region:")
print(df)

# Visualization
plt.bar(df['region'], df['revenue'])
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.show()
