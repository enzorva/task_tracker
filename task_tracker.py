import pyfiglet
import json


class Task:
    def __init__(self, tasks_dict):
        self.tasks_dict = tasks_dict

    def add_task(self, task_name):
        id =  len(self.tasks_dict["tasks"]) + 1
        self.tasks_dict["tasks"].append({"task": task_name, "id": id, "status": "todo"})

        with open('tasks.json', 'w') as f:
            json.dump(self.tasks_dict, f, indent=4)


    def view_tasks(self):
        if self.tasks_dict["tasks"] == []:
            print("\nNo tasks found.\n")
        else:
            print("\nTasks:")
            for task in self.tasks_dict["tasks"]:
                print(f"{task["id"]}. {task["task"]} - {task["status"]}")
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
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks_dict, f, indent=4)

    def update_status(self, id, status):
        match status:
            case "todo":
                self.tasks_dict["tasks"][id - 1]["status"] = "todo"
            case "progress":
                self.tasks_dict["tasks"][id - 1]["status"] = "progress"
            case "done":
                self.tasks_dict["tasks"][id - 1]["status"] = "done"

    def id_getter(self):
        try:
            id = int(input("Enter the task id: "))
        except ValueError:
            print("Invalid id. Please enter a number.")
            return self.id_getter()
        
        if 0 <= id - 1 < len(self.tasks_dict["tasks"]):
            return id
        else:   
            print(f"Task with id '{id}' not found.")
            return self.id_getter()
        
    def status_getter(self):
        status = input("Enter the task status (todo, progress, done): ").lower()
        if status not in ["todo", "progress", "done"]:
            print("Invalid status. Please enter 'todo', 'progress', or 'done'.")
            return self.status_getter()
        return status



def main():
    f = pyfiglet.Figlet(font='small', width=80)
    print(f.renderText('TaskTracker'))

    try:
        with open('tasks.json', 'r') as f:
            tasks_dict = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks_dict = {"tasks": []}

    task_manager = Task(tasks_dict)    
    
    while(True):
        action = input("Enter '1' to add a task, '2' to view tasks, '3' to delete a task, '4' to update a task name, '5' to update a task status, or '6' to exit: ")
        match action:
            case '1':
                task_name = input("Enter the task name: ")
                task_manager.add_task(task_name)
                task_manager.view_tasks()
            case '2':
                task_manager.view_tasks()
            case '3':
                task_manager.view_tasks()
                id = task_manager.id_getter()
                task_manager.delete_task(id)
                task_manager.view_tasks()
            case '4':
                task_manager.view_tasks()
                id = task_manager.id_getter()
                new_name = input("Enter the new task name: ")
                task_manager.update_task(id, new_name)
                task_manager.view_tasks()
            case '5':
                task_manager.view_tasks() # Lembrar de expecificar qual lista deseja fazer o view (todom, progress, done)
                id = task_manager.id_getter()
                status = task_manager.status_getter()
                task_manager.update_status(id, status)
                task_manager.view_tasks()
            case '6':
                print("Exiting...")
                break
            case _:
                print("Invalid option. Please try again.")


main()


