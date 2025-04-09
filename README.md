# 📚 Analyze-Best-Selling-Amazon-Books

This project analyzes the best-selling Amazon books dataset using Python and pandas. It provides insights such as top authors by the number of books listed, average ratings by genre, and basic data exploration.

## ✨ Features

1. **📊 Data Loading and Exploration**:

   - Load the dataset from a CSV file.
   - Display the first 5 rows of the dataset.
   - Show the shape and column names of the dataset.
   - Provide summary statistics for numerical columns.

2. **🛠️ Data Cleaning**:

   - Remove duplicate entries.
   - Rename columns for better readability (e.g., "Name" to "Title", "Year" to "Publication Year", "User Rating" to "Rating").
   - Convert the "Price" column to a float data type.

3. **📈 Analysis**:

   - Identify the most popular authors by counting the number of books they have listed.
   - Calculate the average rating for each genre.

4. **💾 Export Results**:
   - Save the top 10 most popular authors to a CSV file (`top_authors.csv`).
   - Save the average rating by genre to a CSV file (`avg_rating_by_genre.csv`).

## 📂 Files

- **main.py**: Contains the Python script for data analysis.
- **bestsellers.csv**: The dataset of best-selling Amazon books (not included in this repository).
- **top_authors.csv**: Output file containing the top 10 authors by the number of books listed.
- **avg_rating_by_genre.csv**: Output file containing the average rating by genre.

## 🛠️ Requirements

- Python 3.x
- pandas library

## ▶️ How to Run

1. Clone the repository and navigate to the project directory.
2. Place the `bestsellers.csv` file in the `Analyze Best Selling Amazon Books` folder.
3. Run the `main.py` script:
   ```bash
   python main.py
   ```
4. Check the output files (`top_authors.csv` and `avg_rating_by_genre.csv`) in the same folder.
