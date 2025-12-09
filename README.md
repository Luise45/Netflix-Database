# Mini Netflix-Database

**Netflix Datenbank** Is a small relational PostgreSQL database that stores information about different Netflix movies and Series. It allows users to explore movies by title, actor, director, country of production, movie length or genre. 
It is intended to be used by Netflix customers, wanting to more specific search and filtering options. 
  
---

##  Features

**ER Diagram** 

<img width="517" height="484" alt="Screenshot 2025-12-09 at 13 39 45" src="https://github.com/user-attachments/assets/71a67dda-cc8d-478e-acb2-3fe1dda1b957" />

---

**Entities** 
- TITLE – Stores movie details.
- ACTOR - Stores actor information.
- DIRECTOR - Stores director information.
  
**Relations** 
- has_cast (TITLE ↔ ACTOR) – Many-to-many relationship connecting movies and their actors.
- directs (DIRECTOR ↔ TITLE) – Many-to-many relationship connecting directors and movies.

---

**DDL SCRIPT**

<img width="400" height="300" alt="Screenshot 2025-12-09 at 13 43 40" src="https://github.com/user-attachments/assets/c055b912-9524-4c5d-b402-9dd867cdcf6e" />

<img width="400" height="300" alt="Screenshot 2025-12-09 at 13 43 19" src="https://github.com/user-attachments/assets/f6f1ef26-cae4-4023-bfa9-0de129af14eb" />

---

**DML SCRIPT** 

- Data from Kaggel: https://www.kaggle.com/datasets/rahulvyasm/netflix-movies-and-tv-shows/data ( used < 150 entries)
- Inseritng data from the csv file into tables in SQL Server database using python.

<img width="720" height="520" alt="Screenshot 2025-12-09 at 13 51 39" src="https://github.com/user-attachments/assets/68898123-be47-4ead-9e3b-ef1cf6b709ee" />


<img width="777" height="591" alt="Screenshot 2025-12-09 at 13 52 05" src="https://github.com/user-attachments/assets/4d4d5b46-381a-4cf6-86a2-90dbed3accf5" />


<img width="489" height="384" alt="Screenshot 2025-12-09 at 13 52 40" src="https://github.com/user-attachments/assets/f6e329fb-5d4b-49bd-b24e-2e8bfcd3c32b" />


---



### Author

Luise Tabatt
