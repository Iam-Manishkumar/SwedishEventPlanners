import json
import os
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory

#from .ActiveDirectory import EmployeeActiveDirectory
# some_file.py
#import sys
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[1] is reserved for script path (or '' in REPL)
# caution: path[2] is reserved for script path (or '' in REPL)
def createAdditionalstaff(department, jobTitle, description, ID):
    additionalStaff = {
        "department": department,
        "jobTitle": jobTitle,
        "description": description,
        "ID": ID,
        "approved": 0
    }
    return additionalStaff
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

def SaveStaffList(stafflist):
    with open('additionalStaff.json', 'w') as fp:
        json.dump(stafflist, fp)
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory

def ReadStaffFile():
    if os.stat('additionalStaff.json').st_size != 0:
        with open('additionalStaff.json', 'r') as fp:
            staffList = json.load(fp)
    else:
        staffList = []
    return staffList

#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#ed for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
def AddStaffists(listOfStaff):
    print("listOfStaff : ", listOfStaff)
    staffList = ReadStaffFile()
    SaveStaffList(staffList + listOfStaff)


def UpdateStaffApproval(staff, index):
    staffList = ReadStaffFile()
    staffList.pop(index)
    staffList.insert(index, staff)
    SaveStaffList(staffList)

#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
#from .ActiveDirectory import EmployeeActiveDirectory

#import sys
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
def getStaffByID(ID):
    staffList = ReadStaffFile()
    index = next((index for (index, d) in enumerate(staffList) if d["ID"] == ID), None)
    print(index)
    return staffList[index], index

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
def printStaffList(department):
    staffList = ReadStaffFile()
    print("stafflist : in print: ", staffList)
    if staffList:
        print("                                                                                    ")
        for item in staffList:
            if item["department"] == department.lower():
                print("\tName of the department : ", item["department"])
                print("\tWhat is the Job Title? : ", item["jobTitle"])
                print("\tIs there an eventID? : ", item["ID"])
                print("\tHas it been approved? 1=Yes, 0=no : ", item["approved"])
                print("                                                                             ")
        print("                                                                             ")