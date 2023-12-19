class ToDoList:
    to_do_list =[]

    def addTask(self):
        task = input("Enter task to add to the to do list : ")

        item = {
                "task": task,
                "status": "not done"
                }
        self.to_do_list.append(item)
        
    def removeTask(self,index):
        self.to_do_list[index]['status'] = "done"
    
    def getAllTask(self):
        return self.to_do_list
    
    def getCompletedTask(self):
        done = []
        for item in self.to_do_list:
            if item["status"] == "done":
                done.append(item)
        return done
                
    def getRemainingTask(self):
        not_done = []
        for item in self.to_do_list:
            if item["status"] == "not done":
                not_done.append(item)
        return not_done

    
def showTasks(tasks):
    if len(tasks) == 0:
        print("No Items in list")
    i = 1
    for item in tasks:
        print(i,item['task'])
        i+=1
 

to_do_list = ToDoList()           
while True:
    user_choice = int(input("""
        what would you like to do:
        press
        1 to add item to the list
        2 to remove item to the list
        3 to see all the tasks
        4 to see completed task
        5 to see remaing task
        """)   ) 

    if user_choice == 1:
        while True:
            to_do_list.addTask()
            more = input("Do you want to add more task?(y/n)")
            if more == "n":
                break

    elif user_choice == 2:
        while True:
            remaing_task_list = to_do_list.getRemainingTask()
            showTasks(remaing_task_list)
            
            remove = int(input("Which task have you comleted enter its SNO : "))
            
            
            for index, item in enumerate(to_do_list.to_do_list):
                if item['task'] == remaing_task_list[remove-1]['task']:
                    print(index)
                    print(remaing_task_list[remove-1]['task'])
                    print(item['task'])
                    to_do_list.removeTask(index)
                    break
            
            more = input("Do you want to remove more task?(y/n)")
            if more == "n":
                break
    elif user_choice == 3:
        tasks = to_do_list.getAllTask()
        print("Tasks in the to do list are :")
        showTasks(tasks)
        
    elif user_choice == 4:
        completed_tasks = to_do_list.getCompletedTask()
        print("Tasks completed from the to do list are :")
        showTasks(completed_tasks)

    elif user_choice == 5:
        print("Tasks remaining in the to do list are :")
        remaining_tasks = to_do_list.getRemainingTask()
        showTasks(remaining_tasks)
        
    else:
        print("exiting system")
        break




    

 
    
