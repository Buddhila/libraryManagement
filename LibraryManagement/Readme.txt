# Library Management Project

This is a simple library management project developed using Django.

## Project Setup

To run this project, please follow the instructions below:

1. Make sure you have Python 3.x installed on your system.
2. Clone this repository to your local machine or download and extract the ZIP file.
3. Open a terminal/command prompt and navigate to the project directory.

### Setting up the Virtual Environment

4. Create a virtual environment by running the following command:

   ```shell
   python3 -m venv venv


Activate the virtual environment:

On macOS/Linux: source venv/bin/activate
On Windows: venv\Scripts\activate


Installing Dependencies
Install the required dependencies by running the following command: pip install -r requirements.txt


Running the Project
Apply the database migrations: python manage.py migrate


Start the development server: python manage.py runserver



Open your web browser and visit http://127.0.0.1:8000/books/ to access the Library Management application.



Project Structure
	The main Django project is located in the LibraryManagement directory.
	The library application is located in the library directory.
	Templates for HTML pages are located in the library/templates directory.
	Static files such as CSS and JavaScript are located in the library/static directory.

Additional Information
	The books_list.txt file contains the data for the books in the library. Each line represents a book entry with comma-separated values.
	The helpers.py file contains helper functions for loading, saving, and manipulating book data from the books_list.txt file.
