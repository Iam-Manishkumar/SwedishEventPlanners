import json
import os
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#{
   # "python.analysis.extraPaths": 
    #    "./Group26_SEP/Active Directory",
    #    "./Group26_SEP/Additional Requests",
    #    "./Group26_SEP/ActiveDirectory",
      #  "./Group26_SEP/AdditionalRequests"
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
def createExtraBudget(department, amount, description, ID):
    extraBudget = {
        "department": department,
        "amount": amount,
        "description": description,
        "ID": ID,
        "approved": 0
    }
    return extraBudget
#from ActiveDirectory import EmployeeActiveDirectory

# caution: path[1] is reserved for script path (or '' in REPL)
# caution: path[2] is reserved for script path (or '' in REPL)
# caution: path[3] is reserved for script path (or '' in REPL)
#import sys
#import opt
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
def SaveBudgetList(budgetlist):
    with open('additionalBudget.json', 'w') as fp:
        json.dump(budgetlist, fp)

def ReadBudgetFile():
    if os.stat('additionalBudget.json').st_size != 0:
        with open('additionalBudget.json', 'r') as fp:
            budgetList = json.load(fp)
    else:
        budgetList = []
    return budgetList
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
# some_file.py
#from .ActiveDirectory import EmployeeActiveDirectory

def AddBudgetists(listOfBudgets):
    budgetList = ReadBudgetFile()
    SaveBudgetList(budgetList + listOfBudgets)

def UpdateBudgetApproval(budget, index):
    budgetList = ReadBudgetFile()
    budgetList.pop(index)
    budgetList.insert(index, budget)
    SaveBudgetList(budgetList)
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory

# some_file.py
#from .ActiveDirectory import EmployeeActiveDirectory
# some_file.py
#import sys
# caution: path[5] is reserved for script path (or '' in REPL)
# caution: path[6] is reserved for script path (or '' in REPL)
# caution: path[7] is reserved for script path (or '' in REPL)
def getBudgetByID(ID):
    budgetList = ReadBudgetFile()
    index = next((index for (index, d) in enumerate(budgetList) if d["ID"] == ID), None)
    print(index)
    return budgetList[index], index
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory

# some_file.py
#from .ActiveDirectory import EmployeeActiveDirectory
# some_file.py
#import sys
# caution: path[8] is reserved for script path (or '' in REPL)
# caution: path[9] is reserved for script path (or '' in REPL)
# caution: path[10] is reserved for script path (or '' in REPL)
def printBudgetList(department):
    budgetList = ReadBudgetFile()
    if budgetList:
        print("                                                                                         ")
        for item in budgetList:
            if item["department"] == department.lower():
                print("\tDepartment : ", item["department"])
                print("\tAdditional budget? : ", item["amount"])
                print("\tOne Liner Description : ", item["description"])
                print("\tID#? : ", item["ID"])
                print("\tHas it been approved? : ", item["approved"])
                print("                                                                                 ")
        print("                                                                                         ")