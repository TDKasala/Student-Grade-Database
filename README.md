# Student Grade Database

This Python script demonstrates how to create and manipulate a simple SQLite database to store student data, including their names and grades.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Database Structure](#database-structure)
- [Contributing](#contributing)

## Prerequisites

Before you run the script, ensure you have Python installed on your system.

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/student-grade-database.git
   ```

2. Navigate to the project directory:

   ```bash
   cd student-grade-database
   ```

3. Run the script:

   ```bash
   python student_grade_database.py
   ```

## Usage

The script performs the following tasks:

1. It creates an SQLite database called `python_programming.db` and defines a table named `students` to store student information, including an `id` (primary key), `name`, and `grade`.

2. It inserts five sample student records into the database.

3. It retrieves and prints the information of two students based on their `id`.

4. It updates the grade of one student.

5. It deletes one student record from the database.

6. Finally, it commits the changes and closes the database connection.

## Database Structure

The database has a single table named `students` with the following structure:

- `id` (Primary Key): An integer representing the unique identifier for each student.
- `name`: A text field to store the student's name.
- `grade`: An integer representing the student's grade.

## Contributing

Contributions are welcome! If you have any improvements or suggestions for this project, please open an issue or a pull request.
