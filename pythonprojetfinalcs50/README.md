# ## Title of Project : Task Manager Project
### Video Demo : https://youtu.be/62tUMAnQw2c
#### Description:
This project is a simple task management application written in Python. 
It allows users to add, view, and delete tasks through a command-line interface.
### project file

-**project.py**: Contains the main application code, including the `main`, `add_task`, `display_tasks` and `delete_task` functions.
- **test_project.py**: Contains unit tests for the `add_task`, `display_tasks` and `delete_task` functions using `pytest`.
- **requirements.txt**: Lists the dependencies needed to run the tests, in this case, `pytest`.

### functionality

1. **Add task**: User can add a new task to the list.
2. **View Tasks**: User can view all tasks currently in the list.
3. **Delete a task**: User can delete a specific task from the list by entering its number.

### design choice

-**Simplicity**: The project is designed to be simple and easy to understand, with a command line user interface.
- **Modularity**: Functions are separated to facilitate testing and maintenance.
- **Unit Tests**: Unit tests are included to ensure that each function works as expected.
