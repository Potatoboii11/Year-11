class ToDoTask: #Class initialises attributes of a task
    def __init__(self, task, category, deadline=None):
        self.task = task
        self.category = category
        self.deadline = deadline  

    def __str__(self): #States the task name, what category it is in and its deadline
        return f"Task: {self.task} | Category: {self.category} | Deadline: {self.deadline or 'No deadline'}"


class ToDoManager: # Manages to do list
    def __init__(self):
        self.tasks = {
            'School': {},
            'Home': {}
        }  #Nested Dictionary to make the code shorter 

    def add_task(self, task, category, deadline=None): # Adds new task to a certain category
        if category not in self.tasks:
            raise ValueError(f"Invalid category: {category}")
        if task in self.tasks[category]: #New task won't be add if it is already in the dictionary
            raise ValueError("Task already exists in this category.")
        else:
            self.tasks[category][task] = ToDoTask(task, category, deadline)

    def edit_task(self, task, category, new_task=None, new_deadline=None): #Allows user to change properties of a task including its category and deadline
        if category not in self.tasks or task not in self.tasks[category]:
            raise ValueError("Task not found in this category.")

        task_obj = self.tasks[category][task] #New 

        if new_task and new_task != task:
            del self.tasks[category][task]
            task_obj.task = new_task
            self.tasks[category][new_task] = task_obj

       
        if new_deadline:
            task_obj.deadline = new_deadline

    def remove_task(self, task, category): #Method to remove tasks from the to-do list
        if category not in self.tasks or task not in self.tasks[category]:
            raise ValueError("Task not found in this category.") # Raises error if task is not in the category
        else: 
            del self.tasks[category][task] #Deletes task from 

    def list_tasks(self, category=None): 
        output = [] #The output is printed from a list
        if category is not None: #If the category of the task is not defualt, it will append the task with the task name into the output list
            if category not in self.tasks: #Raised error if the category does not exist
                raise ValueError("Invalid category.") 
            for task_name in self.tasks[category]: 
                task_obj = self.tasks[category][task_name] #setting a single variable as the nested dictionarys
                output.append(str(task_obj)) #Adding it to the output list
        else:
            for cat in self.tasks: #goes
                for task_name in self.tasks[cat]:
                    task_obj = self.tasks[cat][task_name]
                    output.append(str(task_obj))
        return output # Prints entire to-do list and task deadlines


class ToDoListFacade: #Facade to make it seem like the code is simple
    def __init__(self):
        self.manager = ToDoManager() #new way to call method

    def add_task(self, task, category, deadline=None): 
        self.manager.add_task(task, category, deadline)

    def edit_task(self, task, category, new_task=None, new_deadline=None):
        self.manager.edit_task(task, category, new_task, new_deadline)

    def delete_task(self, task, category):
        self.manager.remove_task(task, category)

    def show_tasks(self, category=None): #A method to print the whole to-do list
        print("\nTO-DO LIST") 
        tasks = self.manager.list_tasks(category) #Task is from the list task method
        if not tasks: #If there is no tasks it will print no task found
            print("No tasks found.")
        else:
            for task in tasks: #For each task it will print out in seperate line
                print(task)

if __name__ == '__main__':
    todo = ToDoListFacade()
    
    todo.add_task("english essay", "School", "20/6/25") #Tasks testing
    todo.add_task("Mow lawn", "Home", "19/6/25")
    todo.add_task("Science Notes", "School")
    
    todo.show_tasks() #Displays all tasks
  
    todo.edit_task("english essay", "School", new_task="Complete english Essay", new_deadline="22 June 2025") #Edit an existing task
    todo.delete_task("Mow lawn", "Home") #Deletes task

    todo.show_tasks() #Display all tasks again to show edited task
