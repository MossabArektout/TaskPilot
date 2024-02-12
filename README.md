
# TaskPilot : Your Task Management Companion

CS, python, flask, flask web framework, web development

This is a Task Manager Web application

## What you can do ?
* Create a task by giving a title and description to it
* View all the existing tasks
* Update a task
* Delete a task
## Languages, Libraries and Tools used
* Flask
* Jinja
* sqlite
* Html
* css
* Javascript
* Bootstrap

## About
TaskPilot is a task manager web application designed to help you stay organized and on top of your tasks. With TaskPilot, you can manage your tasks efficiently with features such as creating, viewing, updating, deleting.
## Features
### 1. Create Tasks
Task creation in TaskPilot is straightforward and user-friendly. Users can simply provide a title and description for the task they wish to add. This minimalist approach ensures that adding tasks is quick and hassle-free, enabling users to capture their thoughts and responsibilities with ease.
### 2. View All Tasks
askPilot provides users with a centralized dashboard where they can view all their existing tasks at a glance. This feature enables users to gain a comprehensive overview of their workload, facilitating better planning and prioritization of tasks.
### 3. Update Tasks
Flexibility is key in task management, and TaskPilot offers users the ability to update tasks as needed. Whether it's modifying the task title, description, or other details, users can easily make changes to their tasks to reflect evolving requirements or new information.
### 4. Delete Tasks
Task cleanup is essential for maintaining an organized task list, and TaskPilot simplifies this process with its delete task functionality. Users can effortlessly remove unwanted tasks from their list, keeping their task management environment clutter-free and efficient.

## Project Structure
### 1. User Authentication
TaskPilot ensures secure access to user accounts through robust authentication mechanisms. Users can create an account using the signup functionality or log in using existing credentials. This feature provides a personalized experience and ensures data privacy.
### 2. Task Managemenet
The add.html file contains the HTML code for creating new tasks in the TaskPilot application. It presents users with a form where they can input the title and description of the task they wish to add. Upon submission, the form data is sent to the server via a POST request to the "/addtask" endpoint, initiating the task creation process. Additionally, the page displays a table showcasing all existing tasks, if any, providing users with a comprehensive view of their task list. Each task entry in the table includes options to update or delete the respective task, facilitating seamless task management.

Conversely, the update.html file serves as the interface for updating existing tasks in TaskPilot. It features a form similar to that of the add.html page, pre-filled with the details of the task being updated. Users can modify the task title and description as needed and submit the changes via a POST request to the "/update/{{todo[0]}}" endpoint. This triggers the update process on the server, ensuring that the task details are promptly adjusted according to the user's input.
### 3. Backend Implementation
The app.py file contains the backend logic and routing configurations for TaskPilot. It utilizes a Python-based web framework (e.g., Flask or Django) to handle HTTP requests, manage user sessions, and interact with the database. app.py serves as the backbone of TaskPilot, orchestrating the application's functionality and ensuring seamless user experiences.



"# TaskPilot" 
"# TaskPilot" 
"# TaskPilot" 

