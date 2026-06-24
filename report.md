###  report.md

# Library Management System Report

## Introduction

This project is a simple Library Management System developed using Python and SQLite. The main goal of the project is to manage books in a small library.

## Project Objective

The objective of this project is to create a basic system that allows users to add, view, borrow, return, and delete books.

## Tools and Technologies

- Python
- SQLite
- GitHub

## Database Design

The database contains one table called `books`.

### Books Table

| Column | Type | Description |
|---|---|---|
| id | INTEGER | Unique book ID |
| title | TEXT | Book title |
| author | TEXT | Book author |
| year | INTEGER | Publication year |
| available | INTEGER | Book availability status |

## System Features

1. Add Book  
2. View Books  
3. Borrow Book  
4. Return Book  
5. Delete Book  

## How the System Works

When the program starts, it creates the database table automatically if it does not already exist. The user can choose an option from the menu to manage books.

## Conclusion

This project helped me understand how to use Python with SQLite to create a simple database management system.
