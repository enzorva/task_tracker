# Task Tracker

Task Tracker is a command-line application for managing tasks. It allows you to add, view, delete, and update tasks, as well as mark tasks as "in progress" or "done."

## Features
- Add new tasks
- View all tasks or filter tasks by status (e.g., "todo", "progress", "done")
- Delete tasks by ID
- Update task names
- Update task statuses

## Requirements
- Python 3.7+
- Required Python packages:
  - `pyfiglet`
  - `prettytable`

## Prerequisites
- Python 3.7 or higher
  - To check your Python version, run:
    ```bash
    python --version
    ```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd task_tracker
   ```
2. Install the required Python packages:
   ```bash
   pip install pyfiglet prettytable
   ```

## Usage
Run the script with the following commands:

### Add a Task
```bash
python task_tracker.py add "Task Name"
```

### View All Tasks
```bash
python task_tracker.py list
```

### View Tasks by Status
```bash
python task_tracker.py list <status>
```
- `<status>` can be `todo`, `progress`, or `done`.

### Delete a Task
```bash
python task_tracker.py delete <task_id>
```
- `<task_id>` is the ID of the task to delete.

### Update a Task Name
```bash
python task_tracker.py update <task_id> "New Task Name"
```

### Mark a Task as In Progress
```bash
python task_tracker.py mark-in-progress <task_id>
```

### Mark a Task as Done
```bash
python task_tracker.py mark-done <task_id>
```

### Help
For usage instructions:
```bash
python task_tracker.py help
```

## Example Commands
Here are some example commands to help you get started:

### Add a Task
```bash
python task_tracker.py add "Buy groceries"
```
This will add a task named "Buy groceries" to the task list.

### View Tasks by Status
```bash
python task_tracker.py list todo
```
This will display all tasks with the status "todo."

### Delete a Task
```bash
python task_tracker.py delete 1
```
This will delete the task with ID 1.

### Update a Task Name
```bash
python task_tracker.py update 1 "Buy vegetables"
```
This will update the name of the task with ID 1 to "Buy vegetables."

## Testing
This project includes unit tests written with `pytest`. To run the tests:
```bash
pytest test_task_tracker.py
```

## File Structure
- `task_tracker.py`: Main script for the Task Tracker application.
- `tasks.json`: JSON file used to store tasks.
- `test_task_tracker.py`: Test file for the Task Tracker application.

## Contributing
Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.

## Known Issues
- The application currently does not support task prioritization.
- Tasks are stored in a single JSON file, which may not scale well for large datasets.

## Changelog
### Version 1.0.0 (April 7, 2025)
- Initial release with the following features:
  - Add, view, delete, and update tasks
  - Mark tasks as "in progress" or "done"
  - Filter tasks by status
  - Command-line interface for task management

## License
This project is licensed under the MIT License.