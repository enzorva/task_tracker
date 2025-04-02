import pyfiglet
import json


class Task:
    def __init__(self, tasks_dict, id):
        self.tasks_dict = tasks_dict
        self.id = id

    def add_task(self, task_name):
        self.id += 1
        self.tasks_dict["tasks"].append({"task": task_name, "id": self.id})

        with open('tasks.json', 'w') as f:
            json.dump(self.tasks_dict, f, indent=4)


    def view_tasks(self):
        if self.tasks_dict["tasks"] == []:
            print("\nNo tasks found.\n")
        else:
            print("\nTasks:")
            for i, task in enumerate(self.tasks_dict["tasks"], start=1):
                print(f"{i}. {task["task"]}")
            print("\n")
            
    def delete_task(self, id):
        if 0 <= id - 1 < len(self.tasks):
            task_name = self.tasks[id - 1]
            self.tasks.pop(id - 1)
            print(f"\nTask '{task_name}' deleted.\n")
        else:
            print(f"\nTask '{task_name}' not found.\n")



def main():
    f = pyfiglet.Figlet(font='small', width=80)
    print(f.renderText('TaskTracker'))

    try:
        with open('tasks.json', 'r') as f:
            tasks_dict = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks_dict = {"tasks": []}

    id = 0
    task_manager = Task(tasks_dict, id)
    

    
    while(True):
        action = input("Enter '1' to add a task, '2' to view tasks, '3' to delete a task, or '4' to exit: ")
        match action:
            case '1':
                task_name = input("Enter the task name: ")
                task_manager.add_task(task_name)
                task_manager.view_tasks()
            case '2':
                task_manager.view_tasks()
            case '3':
                id = int(input("Enter the task id to delete: "))
                task_manager.delete_task(id)
            case '4':
                print("Exiting...")
                break
            case _:
                print("Invalid option. Please try again.")


main()


