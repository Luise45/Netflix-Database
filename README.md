#  Relational Netflix inspired Database

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

The project covers the complete database development process, from conceptual modeling to data population and querying.
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

<img width="49%" height="420" alt="Python Import Script" src="https://github.com/user-attachments/assets/68898123-be47-4ead-9e3b-ef1cf6b709ee" />

<img width="49%" height="491" alt="Database Population" src="https://github.com/user-attachments/assets/4d4d5b46-381a-4cf6-86a2-90dbed3accf5" />

<img width="49%" height="284" alt="Database Results" src="https://github.com/user-attachments/assets/f6e329fb-5d4b-49bd-b24e-2e8bfcd3c32b" />

---
## Example Queries 

Find all titles featuring a specific actor:

```sql
SELECT t.title
FROM title t
JOIN has_cast hc ON t.id = hc.title_id
JOIN actor a ON hc.actor_id = a.id
WHERE a.name = 'Tom Hanks';
```

Find all movies produced in Germany:

```sql
SELECT title
FROM title
WHERE country = 'Germany';
```
##  Technologies Used

| Category        | Technology     |
| --------------- | -------------- |
| Database        | PostgreSQL     |
| Query Language  | SQL            |
| Data Processing | Python         |
| Data Source     | Kaggle Dataset |
| Modeling        | ER Diagram     |

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

