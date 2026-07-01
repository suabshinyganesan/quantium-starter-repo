import pandas as pd

# Read the CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine the data
df = pd.concat([df1, df2, df3], ignore_index=True)

# Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Remove the $ sign from price
df["price"] = df["price"].replace("[$]", "", regex=True).astype(float)

# Create sales column
df["sales"] = df["quantity"] * df["price"]

# Keep only required columns
df = df[["sales", "date", "region"]]

# Save the output
df.to_csv("formatted_sales_data.csv", index=False)

print("Task Completed!")