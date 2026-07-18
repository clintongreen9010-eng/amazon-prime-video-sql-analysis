--------------------------------------------------------
-- What Does Amazon Prime Look Like?
--Query 1
-- Business Question:
-- How many total titles are available on Amazon Prime?
--------------------------------------------------------

SELECT COUNT(*) AS Total_Titles
FROM amazon_prime_titles;

--------------------------------------------------------
-- Query 2
-- Business Question:
-- What percentage of the Amazon Prime catalog consists
-- of Movies versus TV Shows?
--------------------------------------------------------

SELECT
    type,
    COUNT(*) AS Number_of_Titles,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM amazon_prime_titles),
        2
    ) AS Percentage
FROM amazon_prime_titles
GROUP BY type;

--------------------------------------------------------
-- Query 3
-- Business Question:
-- Which countries contribute the most content to
-- Amazon Prime Video?
--------------------------------------------------------

SELECT
    country,
    COUNT(*) AS Number_of_Titles
FROM amazon_prime_titles
WHERE country IS NOT NULL
GROUP BY country
ORDER BY Number_of_Titles DESC;

--------------------------------------------------------
-- Query 4
-- Business Question:
-- What are the most common content ratings
-- on Amazon Prime Video?
--------------------------------------------------------

SELECT
    rating,
    COUNT(*) AS Number_of_Titles
FROM amazon_prime_titles
WHERE rating IS NOT NULL
GROUP BY rating
ORDER BY Number_of_Titles DESC;


--------------------------------------------------------
-- Query 5
-- Business Question:
-- How has the release of titles changed over time?
--------------------------------------------------------

SELECT
    release_year,
    COUNT(*) AS Number_of_Titles
FROM amazon_prime_titles
GROUP BY release_year
ORDER BY release_year;


--------------------------------------------------------
-- Query 6
-- Business Question:
-- Which directors appear most frequently in the
-- Amazon Prime Video catalog?
--------------------------------------------------------

SELECT
    director,
    COUNT(*) AS Number_of_Titles
FROM amazon_prime_titles
WHERE director IS NOT NULL
GROUP BY director
ORDER BY Number_of_Titles DESC
LIMIT 10;


--------------------------------------------------------
-- Query 7
-- Business Question:
-- What are the longest movies available
-- on Amazon Prime Video?
--------------------------------------------------------

SELECT
    title,
    director,
    duration
FROM amazon_prime_titles
WHERE
    type = 'Movie'
    AND duration IS NOT NULL
ORDER BY CAST(REPLACE(duration, ' min', '') AS INTEGER) DESC
LIMIT 10;


--------------------------------------------------------
-- Query 8
-- Business Question:
-- What is the average runtime of movies
-- on Amazon Prime Video?
--------------------------------------------------------

SELECT
    ROUND(
        AVG(CAST(REPLACE(duration, ' min', '') AS INTEGER)),
        2
    ) AS Average_Runtime_Minutes
FROM amazon_prime_titles
WHERE
    type = 'Movie'
    AND duration IS NOT NULL;
		
	
	--------------------------------------------------------
-- Query 9
-- Business Question:
-- Which countries contribute the largest number
-- of Movies versus TV Shows?
--------------------------------------------------------

SELECT
    country,
    type,
    COUNT(*) AS Number_of_Titles
FROM amazon_prime_titles
WHERE country IS NOT NULL
GROUP BY country, type
ORDER BY Number_of_Titles DESC
LIMIT 20;


--------------------------------------------------------
-- Query 10
-- Business Question:
-- Which genres are most common among
-- Movies versus TV Shows?
--------------------------------------------------------

SELECT
    type,
    listed_in,
    COUNT(*) AS Number_of_Titles
FROM amazon_prime_titles
WHERE listed_in IS NOT NULL
GROUP BY type, listed_in
ORDER BY Number_of_Titles DESC
LIMIT 20;

