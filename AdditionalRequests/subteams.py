import json
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory

#from .ActiveDirectory import EmployeeActiveDirectory
# some_file.py
#import sys
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
def createTask(department, subteam, name, details):
    task = {
        "department": department,
        "subteam": subteam,
        "employeeName": name,
        "details": details,
        "plan": "TBD",
        "comment": "TBD",
        "additionalBudget": 0
    }
    return task
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#from .ActiveDirectory import EmployeeActiveDirectory

#import sys
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
def printTaskList(department):
    tasklist = ReadTasksFile()
    print(".........................................................................................")
    for task in tasklist:
        if task["department"] == department.lower():
            print("\tName of the department : ", task["department"])
            print("\tName of the subteam : ", task["subteam"])
            print("\tName of the employee : ", task["employeeName"])
            print("\tElaborate the Task : ", task["details"])
            print("\tWhat are the plans? : ", task["plan"])
            print("\tDo you have any comments : ", task["comment"])
            print("\tDo you require any additional budgets : ", task["additionalBudget"], "\n......................................")
    print("...................................................................................")

def SaveTaskList(tasklist):
    with open('subteamtask.json', 'w') as fp:
        json.dump(tasklist, fp)
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory

#from .ActiveDirectory import EmployeeActiveDirectory
# some_file.py
#import sys
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
def ReadTasksFile():
    with open('subteamtask.json', 'r') as fp:
        tasklist = json.load(fp)
        return tasklist

def AddTaskLists(listOfTasks):
    tasklist = ReadTasksFile()
    SaveTaskList(tasklist + listOfTasks)

def UpdateTaskByName(task, index):
    tasklist = ReadTasksFile()
    tasklist.pop(index)
    tasklist.insert(index, task)
    SaveTaskList(tasklist)
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#from .ActiveDirectory import EmployeeActiveDirectory
# some_file.py
#	new file:   Group26_SEP/build/bdist.macosx-10.9-universal2/python3.9-standalone/app/collect/asyncio/base_events.pyc
#	new file:   Group26_SEP/build/bdist.macosx-10.9-universal2/python3.9-standalone/app/collect/asyncio/base_futures.pyc
#	new file:   Group26_SEP/build/bdist.macosx-10.9-universal2/python3.9-standalone/app/collect/asyncio/base_subprocess.pyc
#	new file:   Group26_SEP/build/bdist.macosx-10.9-universal2/python3.9-standalone/app/collect/asyncio/base_tasks.pyc
#	new file:   Group26_SEP/build/bdist.macosx-10.9-universal2/python3.9-standalone/app/collect/asyncio/constants.pyc
#	new file:   Group26_SEP/build/bdist.macosx-10.9-universal2/python3.9-standalone/app/collect/asyncio/coroutines.pyc
#	new file:   Group26_SEP/build/bdist.macosx-10.9-universal2/python3.9-standalone/app/collect/asyncio/events.pyc
#	new file:   Group26_SEP/build/bdist.macosx-10.9-universal2/python3.9-standalone/app/collect/asyncio/exceptions.pyc
#	new file: 

#from .ActiveDirectory import EmployeeActiveDirectory
# some_file.py
#import sys
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
def getTaskByName(name):
    tasklist = ReadTasksFile()
    index = next((index for (index, d) in enumerate(tasklist) if d["employeeName"].lower() == name.lower()), None)
    print(index)
    return tasklist[index], index
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#from .ActiveDirectory import EmployeeActiveDirectory
# some_file.py
#from .ActiveDirectory import EmployeeActiveDirectory
# some_file.py
#import sys
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
def printTaskByName(task):
    print("                                                                             ")
    print("\tName of the department : ", task["department"])
    print("\tName of the subteam : ", task["subteam"])
    print("\tName of the employee : ", task["employeeName"])
    print("\tElaborate the Task : ", task["details"])
    print("\tWhat are the plans? : ", task["plan"])
    print("\tDo you have any comments : ", task["comment"])
    print("\tDo you require any additional budgets : ", task["additionalBudget"])
    print("                                                                             ")
