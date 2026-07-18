import os

import matplotlib.pyplot as plt
import pandas as pd


# =====================================================
# Project setup
# =====================================================

# Load the Amazon Prime Video dataset
df = pd.read_csv("Amazon_Prime_Data/amazon_prime_titles.csv")

# Create the images folder if it does not already exist
os.makedirs("images", exist_ok=True)


# =====================================================
# Chart 1: Movies vs TV Shows
# =====================================================

type_counts = df["type"].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(
    type_counts,
    labels=type_counts.index,
    autopct="%1.1f%%",
    startangle=90,
    textprops={"fontsize": 13},
)

plt.title(
    "Amazon Prime Video Catalog Composition",
    fontsize=16,
    fontweight="bold",
)

plt.tight_layout()
plt.savefig(
    "images/movie_vs_tv.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


# =====================================================
# Chart 2: Titles by Release Year
# =====================================================

release_trend = (
    df.groupby("release_year")
    .size()
    .reset_index(name="Number_of_Titles")
    .sort_values("release_year")
)

plt.figure(figsize=(11, 6))
plt.plot(
    release_trend["release_year"],
    release_trend["Number_of_Titles"],
    linewidth=2,
)

plt.title(
    "Amazon Prime Video Titles by Release Year",
    fontsize=16,
    fontweight="bold",
)
plt.xlabel("Release Year", fontsize=12)
plt.ylabel("Number of Titles", fontsize=12)
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig(
    "images/release_trend.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


# =====================================================
# Chart 3: Top 10 Contributing Countries
# =====================================================

top_countries = (
    df["country"]
    .dropna()
    .value_counts()
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))
plt.barh(
    top_countries.index,
    top_countries.values,
)

plt.title(
    "Top 10 Country Entries in the Amazon Prime Catalog",
    fontsize=16,
    fontweight="bold",
)
plt.xlabel("Number of Titles", fontsize=12)
plt.ylabel("Country", fontsize=12)
plt.grid(axis="x", alpha=0.3)

plt.tight_layout()
plt.savefig(
    "images/top_countries.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


# =====================================================
# Chart 4: Most Common Content Ratings
# =====================================================

top_ratings = (
    df["rating"]
    .dropna()
    .value_counts()
    .head(10)
    .sort_values()
)

plt.figure(figsize=(10, 6))
plt.barh(
    top_ratings.index,
    top_ratings.values,
)

plt.title(
    "Most Common Amazon Prime Video Content Ratings",
    fontsize=16,
    fontweight="bold",
)
plt.xlabel("Number of Titles", fontsize=12)
plt.ylabel("Content Rating", fontsize=12)
plt.grid(axis="x", alpha=0.3)

plt.tight_layout()
plt.savefig(
    "images/ratings_distribution.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


# =====================================================
# Chart 5: Most Common Movie Genre Listings
# =====================================================

movie_genres = (
    df.loc[df["type"] == "Movie", "listed_in"]
    .dropna()
    .value_counts()
    .head(10)
    .sort_values()
)

plt.figure(figsize=(11, 7))
plt.barh(
    movie_genres.index,
    movie_genres.values,
)

plt.title(
    "Most Common Movie Genre Listings on Amazon Prime",
    fontsize=16,
    fontweight="bold",
)
plt.xlabel("Number of Titles", fontsize=12)
plt.ylabel("Genre Listing", fontsize=12)
plt.grid(axis="x", alpha=0.3)

plt.tight_layout()
plt.savefig(
    "images/top_genres.png",
    dpi=300,
    bbox_inches="tight",
)
plt.close()


print("All five visualizations were created successfully.")
print("Check the images folder for the PNG files.")