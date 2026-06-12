#  Relational Netflix inspired Database

![Database](https://img.shields.io/badge/PostgreSQL-blue)
![DDl & DML Skript](https://img.shields.io/badge/Python-orange)
![Databse Diagram ](https://img.shields.io/badge/ERDiagram-red)

A relational database project built with **PostgreSQL** that models a version of Netflix's content catalog.

The database stores information about movies and TV shows, including titles, actors, directors, genres, countries of production, and runtime details. It enables advanced searching and filtering capabilities that go beyond standard browsing options.

---

##  Project Overview

The goal of this project was to design and implement a normalized relational database that allows users to efficiently explore Netflix content through multiple search criteria.
Users can query content by:

*  Actor
*  Director
*  Country of Production
*  Genre
*  Runtime
* Title


---
##  Database Design

### Entity Relationship Diagram

The database schema was first designed using an Entity Relationship (ER) model to define entities, attributes, and relationships.

<img width="417" height="384" alt="ER Diagram" src="https://github.com/user-attachments/assets/71a67dda-cc8d-478e-acb2-3fe1dda1b957" />

---

## Database Structure

### Core Entities

| Entity       | Description                                  |
| ------------ | -------------------------------------------- |
| **TITLE**    | Stores information about movies and TV shows |
| **ACTOR**    | Stores actor details                         |
| **DIRECTOR** | Stores director details                      |

### Relationships

| Relationship | Description                                            |
| ------------ | ------------------------------------------------------ |
| **has_cast** | Many-to-many relationship between titles and actors    |
| **directs**  | Many-to-many relationship between directors and titles |

This structure allows a title to have multiple actors and directors while supporting efficient querying and filtering.

---
## Architecture
<img width="220" height="202" alt="Screenshot 2026-06-04 at 09 37 12" src="https://github.com/user-attachments/assets/231d9bfe-0454-4461-8446-559704a23203" />



---
##  Database Implementation

### DDL (Data Definition Language)

The database schema was implemented in PostgreSQL using SQL DDL scripts to create tables, primary keys, foreign keys, and relationships.

<img width="49%" height="300" alt="DDL Script 1" src="https://github.com/user-attachments/assets/c055b912-9524-4c5d-b402-9dd867cdcf6e" />

<img width="49%" height="300" alt="DDL Script 2" src="https://github.com/user-attachments/assets/f6f1ef26-cae4-4023-bfa9-0de129af14eb" />

---

##  Data Population (DML)

To populate the database, a subset of the Netflix Movies and TV Shows dataset from Kaggle was used.

### Dataset

* Source: Netflix Movies and TV Shows Dataset (Kaggle)
* Records Imported: ~150 entries

The raw CSV data was processed and inserted into the database using Python scripts.

### ETL Workflow

1. Load data from CSV files
2. Clean and transform relevant fields
3. Insert records into relational tables
4. Establish entity relationships through junction tables

Example of actor and casts:
```
actor_id_map = {}
next_actor_id = 1

actor_insert = """
INSERT INTO Actor (actor_id, actor_name)
VALUES (%s, %s)
"""
casts_insert = """
INSERT INTO Casts (actor_id, show_id)
VALUES (%s, %s)
"""

for _, row in df.iterrows():
    if pd.isna(row["cast"]):
        continue
    actors = [a.strip() for a in row["cast"].split(",")]
    for a in actors:
        if a not in actor_id_map:
            actor_id_map[a] = next_actor_id
            cursor.execute(
                actor_insert,
                (next_actor_id, a)
            )
            next_actor_id += 1
        cursor.execute(
            casts_insert,
            (actor_id_map[a], row["show_id"])
        )
```
---
## Example Queries 

JOIN + SORTING: Which actors appear in which shows? Sorted by show title.

```sql
SELECT a.actor_name, a.id, t.titel, t.show_id
FROM actor a
JOIN casts  h ON a. actor_id = h. actor_id
JOIN title ON t.show_id = h.show_id
ORDER BY t.titel ASC;
```
Aggregate function + GROUP BY: How many shows are there per release year?

```sql
SELECT 
    release_year,
    COUNT(*) AS number_of_shows
FROM Titel
GROUP BY release_year
ORDER BY release_year;
```
Aggregation + HAVING clause:  Show all years in which more than 2 shows were released.

```sql
SELECT 
    release_year,
    COUNT(*) AS count_shows
FROM Titel
GROUP BY release_year
HAVING COUNT(*) > 2;
```
Cartesian Product (CROSS JOIN): All possible combinations of show titles and genres (theoretical combinations).

```sql
SELECT 
    T.titel,
    G.main_genre
FROM Titel T
CROSS JOIN Genre G
ORDER BY T.titel, G.main_genre;
```

##  Technologies Used

| Category        | Technology     |
| --------------- | -------------- |
| Database        | PostgreSQL     |
| Query Language  | SQL            |
| Data Processing | Python         |
| Data Source     | Kaggle Dataset |
| Modeling        | ER Diagram     |

### Data Source: https://www.kaggle.com/datasets/rahulvyasm/netflix-movies-and-tv-shows/data
---

## Technical Skills Applied

* Relational Database Design
* Entity Relationship Modeling
* Database Normalization
* SQL DDL & DML
* Primary and Foreign Keys
* Many-to-Many Relationships
* Data Import and ETL Processes
* PostgreSQL Database Development

---
##  Future Improvements

* Expand the dataset beyond 150 entries
* Add user ratings and reviews
* Implement advanced search procedures
* Create database views for common queries
* Develop a frontend application for user interaction
* Add indexing and query optimization

---

