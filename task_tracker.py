import pyfiglet
import json
import time
from prettytable import PrettyTable
import sys

class Task:
    def __init__(self, tasks_dict):
        self.tasks_dict = tasks_dict

    def add_task(self, task_name):
        id =  len(self.tasks_dict["tasks"]) + 1
        self.tasks_dict["tasks"].append({"task": task_name, "id": id, "status": "todo", "created_at": time.strftime("%Y-%m-%d %H:%M:%S"), "updated_at": time.strftime("%Y-%m-%d %H:%M:%S")})

        with open('tasks.json', 'w') as f:
            json.dump(self.tasks_dict, f, indent=4)


    def view_tasks(self, status=None):
        table = PrettyTable()
        table.field_names = ["ID", "Task", "Status", "Created At", "Updated At"]

        if not self.tasks_dict["tasks"]:  
            print("\nNo tasks available.\n")
            return

        if status is None: 
            print("\nAll tasks:")
            for task in self.tasks_dict["tasks"]:
                table.add_row([task['id'], task['task'], task['status'], task['created_at'], task['updated_at']])
        else:  
            filtered_tasks = [task for task in self.tasks_dict["tasks"] if task["status"] == status]
            if not filtered_tasks:  
                print(f"\nNo tasks found with status '{status}'.\n")
                return
            print(f"\nTasks with status '{status}':")
            for task in filtered_tasks:
                table.add_row([task['id'], task['task'], task['status'], task['created_at'], task['updated_at']])

        print(table)
        print("\n")
            
    def delete_task(self, id):
        if 0 <= id - 1 < len(self.tasks_dict["tasks"]):
            task_name = self.tasks_dict["tasks"].pop(id - 1)["task"]
            print(f"\nTask '{task_name}' deleted.\n")

            for id, task in enumerate(self.tasks_dict["tasks"], start=1):
                task["id"] = id

            with open('tasks.json', 'w') as f:
                json.dump(self.tasks_dict, f, indent=4)
        else:
            print(f"\nTask '{task_name}' not found.\n")

    def update_task(self, id, new_task_name):
        self.tasks_dict["tasks"][id - 1]["task"] = new_task_name
        print(f"\nTask '{id}' updated to '{new_task_name}'.\n")
        self.tasks_dict["tasks"][id - 1]["updated_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks_dict, f, indent=4)

    def update_status(self, id, status):
        self.tasks_dict["tasks"][id - 1]["updated_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
        match status:
            case "todo":
                self.tasks_dict["tasks"][id - 1]["status"] = "todo"
            case "progress":
                self.tasks_dict["tasks"][id - 1]["status"] = "progress"
            case "done":
                self.tasks_dict["tasks"][id - 1]["status"] = "done"

        with open('tasks.json', 'w') as f:
            json.dump(self.tasks_dict, f, indent=4)

    def action_getter(self):

        if sys.argv[1] == "add":
            task_name = sys.argv[2]
            self.add_task(task_name)
            self.view_tasks()
        elif sys.argv[1] == "delete":
            try:
                id = int(sys.argv[2])
                self.delete_task(id)
                self.view_tasks()
            except ValueError:
                print("Invalid id. Please enter a number.")
        elif sys.argv[1] == "update":
            try:
                id = int(sys.argv[2])
                new_task_name = sys.argv[3]
                self.update_task(id, new_task_name)
                self.view_tasks()
            except ValueError:
                print("Invalid id. Please enter a number.")
        elif sys.argv[1] == "mark-in-progress":
            try:
                id = int(sys.argv[2])
                self.update_status(id, "progress")
                self.view_tasks()
            except ValueError:
                print("Invalid id. Please enter a number.")
        elif sys.argv[1] == "mark-done":
            try:
                id = int(sys.argv[2])
                self.update_status(id, "done")
                self.view_tasks()
            except ValueError:
                print("Invalid id. Please enter a number.")
        elif sys.argv[1] == "list":
            if len(sys.argv) == 2:
                self.view_tasks()
            elif len(sys.argv) == 3:
                status = sys.argv[2]
                if status not in ["todo", "progress", "done"]:
                    print("Invalid status. Please enter 'todo', 'progress', or 'done'.")
                else:
                    self.view_tasks(status)
        else:
            print("Invalid action. Please enter 'add', 'delete', 'update', 'mark-in-progress', 'mark-done', or 'list'.")
           
    

    

def main():
    f = pyfiglet.Figlet(font='small', width=80)
    print(f.renderText('TaskTracker'))

    try:
        with open('tasks.json', 'r') as f:
            tasks_dict = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks_dict = {"tasks": []}

    task_manager = Task(tasks_dict)    
    
    task_manager.action_getter()


main()


