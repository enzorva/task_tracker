import pyfiglet
# import json


class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(task_name)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
            
    def delete_task(self, task_name):
        if task_name in self.tasks:
            self.tasks.remove(task_name)
            print(f"Task '{task_name}' deleted.")
        else:
            print(f"Task '{task_name}' not found.")



def main():
    f = pyfiglet.Figlet(font='small', width=80)
    print(f.renderText('TaskTracker'))

    task_manager = Task()

    
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
                delete_task_name = input("Enter the task name to delete: ")
                task_manager.delete_task(delete_task_name)
            case '4':
                print("Exiting...")
                break
            case _:
                print("Invalid option. Please try again.")


main()


