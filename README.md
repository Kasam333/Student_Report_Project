Student Report Project
Overview
The Student Report Project is a web-based application developed using Django. This project provides an easy-to-use interface for managing student information, searching student records, and displaying detailed reports. It includes advanced features like pagination, search functionality, and dynamic navigation.

Features :-
Add, view, and manage student details.
Search students by name, department, or ID.
Paginated table view for better data management.
Individual student report navigation.
Responsive UI with Bootstrap for a modern, attractive look.

Technologies Used :-
Backend: Django Framework
Frontend: HTML, CSS, Bootstrap 5
Database: SQLite (default Django database)

Django Functionalities Used :- 
Models (django.db.models):
Used to define the Student model, which represents the student data structure with fields like student_id, department, student_name, etc.

Views (django.shortcuts):

render: To render HTML templates with context data.
get_object_or_404: To retrieve individual student records securely.
Pagination (django.core.paginator):

Paginator: For dividing student data into manageable pages.
Page: To display data for a specific page.
Django Templates:

Template tags like {% for %} and {% if %} for looping and conditional rendering.
url tag for dynamic URL generation.
Forms (django.forms):
Used for the search form to accept input from users.

Django URL Routing (django.urls):

path: For defining URL patterns.
name: For reverse URL resolution.
Static Files Management:
Utilized django.contrib.staticfiles to manage static files like CSS and images.

Snapshots :- 

![Screenshot (19)](https://github.com/user-attachments/assets/65b1e863-81fa-449c-b278-ec646126e5a1)
![Screenshot (20)](https://github.com/user-attachments/assets/555a046f-2ac8-4663-b0d4-6c99c2bc0eba)
![Screenshot (23)](https://github.com/user-attachments/assets/7095db1a-8578-4522-948f-01ad0d58befd)
![Screenshot (21)](https://github.com/user-attachments/assets/dbf124f3-46e1-4db5-9b6a-83bb4a8543ca)
![Screenshot (22)](https://github.com/user-attachments/assets/890af9f6-d4b5-462a-9e68-60238c6bae86)
