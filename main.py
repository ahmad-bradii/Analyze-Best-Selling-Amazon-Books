import pandas as pd
import os


current_directory = os.getcwd()
folder_path = f"{current_directory}\\Analyze Best Selling Amazon Books"

df = pd.read_csv(f'{folder_path}\\bestsellers.csv')

# Get the first 5 rows of the spreadsheet
print(df.head())

# Get the shape of the spreadsheet
print(df.shape)

# Get the column names of the spreadsheet Index(['Name', 'Author', 'User Rating', 'Reviews', 'Price', 'Year', 'Genre'], dtype='object')
print(df.columns)


# Get summary statistics for each column
print(df.describe())


# Drop Duplicates
df.drop_duplicates(inplace=True)

# Renaming Columns
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)


# Converting Data Types
df["Price"] = df["Price"].astype(float)

#Analyzing Author Popularity
author_counts = df['Author'].value_counts()
print(author_counts)

print('---------------------------------')


# Average Rating by Genre
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)


# Export top selling authors to a CSV file
author_counts.head(10).to_csv(f'{folder_path}\\top_authors.csv')

# Export average rating by genre to a CSV file
avg_rating_by_genre.to_csv(f'{folder_path}\\avg_rating_by_genre.csv')