customerService = ["sarah@sep.se"]
seniorCustomerManager = ["janet@sep.se"]
sepHRManagersenior = ["simon@sep.se"]
administratorManager = ["mike@sep.se"]
financeManager = ["alice@sep.se"]
productionManager =["jack@sep.se"]
serviceManager = ["natalie@sep.se"]
audioSubTeam = ["antony@sep.se"]
graphicSubTeam = ["julia@sep.se"]
waitressSubTeam = ["kate@sep.se"]
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory
# caution: path[1] is reserved for script path (or '' in REPL)
# caution: path[2] is reserved for script path (or '' in REPL)
# caution: path[3] is reserved for script path (or '' in REPL)
# caution: path[4] is reserved for script path (or '' in REPL)
# caution: path[5] is reserved for script path (or '' in REPL)
# caution: path[6] is reserved for script path (or '' in REPL)
dictEmp = {
    "customerService" : customerService,
    "seniorCustomerManager" : seniorCustomerManager,
    "sepHRManagersenior" :sepHRManagersenior,
    "administratorManager" : administratorManager,
    "financeManager" : financeManager,
    "productionManager" : productionManager,
    "serviceManager" : serviceManager,
    "subTeam": waitressSubTeam + graphicSubTeam + audioSubTeam
}
#from ActiveDirectory import EmployeeActiveDirectory
#from ActiveDirectory import EmployeeActiveDirectory

#from .ActiveDirectory import EmployeeActiveDirectory
# some_file.py
allEmployees = sum(dictEmp.values(), [])

def getRole(username):
    role = ""
    for role, name in dictEmp.items():
        if username in name:
            print(role)
            break
    return role