import matplotlib.pyplot as plt
import pandas as pd

# convert dictionary to a series
grades = {"John": 87, "Steve": 86, "Laura":92, "Edwin": 89}
new_grades = pd.Series(grades)
print(new_grades)

# convert arrays to series
s = pd.Series([['Red', 'Green', 'White'], ['White', 'Green'], ['Yellow']])

# iterating over rows in a DataFrame
data = [{'Name': 'Lesego', 'score': 55}, {'Name': 'Barati', 'score': 65.0}, {'Name': 'Lesego', 'score': 78.90}]
df = pd.DataFrame(data)
for index, row in df.iterrows():
    print(row['Name'], row['Score'])

# EXERCISE 1
# Activity 4: Commenting on each line

# The file containing the data
df = pd.read_csv("alphabet_stock_data.csv")

# Declaring the start date of the execution
start_date = pd.to_datetime('2020-4-1')

# Declaring the end date of the execution
end_date = pd.to_datetime('2020-09-30')
df['Date'] = pd.to_datetime(df['Date'])
new_df = (df['Date'] >= start_date) & (df['Date'] <= end_date)
df1 = df.loc[new_df]
df2 = df1.set_index('Date')

# The grid size
plt.figure(figsize = (5, 5))

# The title of the graph
plt.suptitle('Stock prices of Alphabet Inc., \n01-04-2020 to 30-09-2020', fontsize = 18, color = 'black')

# labelling the x-axis and color
plt.xlabel("Date", fontsize = 16, color = 'black')

# labelling the y-axis and color
plt.ylabel("$ price", fontsize = 16, color = 'black')

df['close'].plot(color = 'green')
plt.show()