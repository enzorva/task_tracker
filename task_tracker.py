import pyfiglet
# import json


class Task:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        if (task_name != 4):
            self.tasks.append(task_name)
        else:
            return

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
        else:
            print("\n")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
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
                delete_task_id = int(input("Enter the task id to delete: "))
                task_manager.delete_task(delete_task_id)
            case '4':
                print("Exiting...")
                break
            case _:
                print("Invalid option. Please try again.")


main()


