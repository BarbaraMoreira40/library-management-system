📚 Library Management System (Python + SQL Server)
A simple command-line application to manage a book catalog using Python and SQL Server.
This project demonstrates basic CRUD operations (Create, Read, Update, Delete) in a real database.

📌 Features
Add a new book to the catalog

List all books

Update book details

Delete a book

Interactive terminal menu

🛠️ Technologies Used
Python 3

SQL Server

pyodbc (Python package for database connection)

⚙️ Setup Instructions
1. Clone the repository
2. Install Python dependencies
Make sure you have Python installed. Then run:

nginx

Copiar

Editar

pip install pyodbc

3. Create the Database and Table
   
Open SQL Server Management Studio (SSMS) and run the following SQL script:

pgsql
Copiar
Editar
CREATE DATABASE BibliotecaDB;
GO
USE BibliotecaDB;
GO
CREATE TABLE Livros (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    Titulo NVARCHAR(255) NOT NULL,
    Autor NVARCHAR(255) NOT NULL,
    Ano_Publicacao INT NOT NULL,
    Genero NVARCHAR(100) NOT NULL
);

4. Configure the database connection in Python
   
The connection settings in biblioteca.py should look like this:

python
Copiar
Editar
import pyodbc

def conectar():
    return pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=localhost;"
        "DATABASE=BibliotecaDB;"
        "Trusted_Connection=yes;"
    )
    
Make sure the SERVER and DATABASE match your environment.

▶️ How to Run the Application

Open the terminal and run:

nginx
Copiar
Editar
python biblioteca.py
You will see a menu like this:

markdown
Copiar
Editar
--- Library Management ---
1. Add Book
2. List Books
3. Update Book
4. Delete Book
5. Exit
Choose an option by entering the corresponding number.

💡 Example
Adding a Book:

yaml
Copiar
Editar
Title: The Alchemist  
Author: Paulo Coelho  
Year: 1988  
Genre: Fiction
Listing Books:

yaml
Copiar
Editar
ID: 1, Title: The Alchemist, 
Author: Paulo Coelho,
Year: 1988,
Genre: Fiction

🧠 Author
Bárbara Moreira

📄 License
This project is licensed under the MIT License.
