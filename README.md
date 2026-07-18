# amazon-prime-video-sql-analysis
SQL business case study analyzing Amazon Prime Video's content catalog to uncover insights into content distribution, ratings, genres, and global trends.

| Metric                  |                    Value |
| ----------------------- | -----------------------: |
| Total Titles            |                **9,668** |
| Movies                  |               **80.82%** |
| TV Shows                |               **19.18%** |
| Average Movie Runtime   |            **91.31 min** |
| Largest Contributors    | **India, United States** |
| Most Common Movie Genre |                **Drama** |


Amazon Prime Video Catalog Analysis
A SQL Business Case Study
Executive Summary

This project analyzes Amazon Prime Video's content catalog using SQL to uncover trends in catalog composition, geographic distribution, content ratings, runtime characteristics, and genre distribution.

Rather than focusing solely on SQL syntax, this project approaches the dataset from the perspective of a business analyst tasked with summarizing the current state of Amazon Prime Video's catalog for leadership. Through ten business-driven SQL investigations, the analysis demonstrates how SQL can be used to transform raw data into actionable business insights while identifying opportunities to improve data quality and reporting.

Business Problem

Streaming services manage thousands of titles across multiple countries, genres, and audience demographics. Understanding the composition of a content catalog helps stakeholders evaluate content distribution, identify market strengths, and improve future reporting.

The objective of this project was to analyze Amazon Prime Video's catalog using SQL and communicate meaningful findings through an executive-style report.

Dataset
Source: Kaggle – Amazon Prime Movies and TV Shows
Database: SQLite
Language: SQL
Records Analyzed: 9,668 titles
Business Questions

This project answers ten business-focused questions:

How large is Amazon Prime's content catalog?
Is the platform primarily movies or television?
Which countries contribute the most content?
What audiences are represented by the platform's content ratings?
How has the catalog evolved over time?
Which directors appear most frequently?
What are the longest titles available?
What is the average runtime of a movie?
How do countries differ in their Movie versus TV Show contributions?
Which genres are most common across Movies and TV Shows?
Key Findings:

  Amazon Prime is a movie-first platform

Approximately 81% of the catalog consists of movies, while television series represent roughly 19% of available titles.

  India and the United States dominate the catalog

The analysis found that India and the United States contribute the largest number of titles.

However, their catalogs differ:

India's catalog is overwhelmingly movie-focused.
The United States contains a more balanced mix of movies and television.

This suggests different regional content profiles within the platform.

  The catalog emphasizes modern releases

Title counts increase substantially in more recent release years, indicating a catalog largely composed of modern productions while still maintaining older titles.

Because the dataset ends in 2021, this trend should not be interpreted beyond the available data.

  Drama is the most common movie genre

Drama emerged as the dominant movie genre, followed by Comedy and Documentary content.

Because multiple genres are stored within a single field, genre frequencies should be interpreted as combinations rather than fully normalized genre counts.

  Runtime analysis

The average movie runtime is 91.31 minutes, which aligns with a typical feature-length film.

The longest titles were primarily ambient sleep and relaxation videos rather than traditional films, illustrating the importance of validating assumptions before drawing conclusions.

  Data quality observations

Several common data-quality challenges were identified during the analysis:

Multiple rating systems in one dataset
Multiple countries stored in a single field
Multiple genres stored in a single field
Production companies appearing as directors
Invalid metadata entries (for example, "1")

These issues demonstrate the importance of data cleaning before advanced analysis.

SQL Skills Demonstrated

Throughout this project I used SQL to:

Aggregate and summarize data with COUNT() and AVG()
Filter records using WHERE
Group data with GROUP BY
Sort results using ORDER BY
Clean text fields with REPLACE()
Convert data types using CAST()
Format numeric output using ROUND()
Analyze multiple dimensions using multi-column GROUP BY
Limit result sets with LIMIT
Business Recommendations

Based on this analysis, I would recommend:

Continue monitoring regional catalog composition to maintain a balanced global library.
Standardize metadata fields such as ratings, genres, countries, and directors to improve reporting accuracy.
Normalize multi-value fields to enable more detailed genre and country analysis.
Combine catalog metadata with engagement or viewing data in future analyses to better understand audience preferences.
Future Improvements

Future versions of this project could include:

Database normalization for genres and countries
Interactive Power BI dashboard
Tableau dashboard
Genre trends over time
Analysis using date_added
Advanced SQL techniques including CTEs and window functions
