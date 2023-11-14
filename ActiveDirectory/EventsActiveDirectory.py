import json
# caution: path[1] is reserved for script path (or '' in REPL)
# caution: path[2] is reserved for script path (or '' in REPL)
# caution: path[3] is reserved for script path (or '' in REPL)
# caution: path[4] is reserved for script path (or '' in REPL)
# caution: path[5] is reserved for script path (or '' in REPL)
# caution: path[6] is reserved for script path (or '' in REPL)
#from Active
#import sys
# caution: path[7] is reserved for script path (or '' in REPL)
# caution: path[8] is reserved for script path (or '' in REPL)
# caution: path[9] is reserved for script path (or '' in REPL)
def createEventRequest(clientName, description, budget, ID):
    eventReq = {
        "ID": ID,
        "clientName": clientName,
        #"eventStartDate": eventStartDate,
        #"eventEndDate": eventEndDate,
        "description": description,
        "budget": budget,
        "SeniorCustomerApproval": "TBD",
        "FinanceManagerFeedback": "TBD",
        "Adminapproval": "TBD",
        "status": "OPEN"
    }
    SaveEventRequestFile(eventReq)
    return
# caution: path[1] is reserved for script path (or '' in REPL)
# caution: path[2] is reserved for script path (or '' in REPL)
# caution: path[3] is reserved for script path (or '' in REPL)
# caution: path[4] is reserved for script path (or '' in REPL)
# caution: path[5] is reserved for script path (or '' in REPL)
# caution: path[6] is reserved for script path (or '' in REPL)

def printEventReq():
    eventReq = ReadEventRequestFile()
    print("The application has created a new event request")
    print("\tName of the customer : ", eventReq["clientName"])
    print("\tID# : ", eventReq["ID"])
    print("\tDetails of the event : ", eventReq["description"])
    print("\tInitial Budget of the event: ", eventReq["budget"])
    # caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
    print("\tApproval by Janet@sep.se (SCS) : ", eventReq["SeniorCustomerApproval"])
    print("\tFeedback by Alice@sep.se (FM) : ", eventReq["FinanceManagerFeedback"])
    print("\tFeedback by Mike@sep.se (AM) : ", eventReq["Adminapproval"])
    print("\tLatest Progress of the event : ", eventReq["status"])
    print("Thanks and have a nice day!")

# caution: path[1] is reserved for script path (or '' in REPL)
# caution: path[2] is reserved for script path (or '' in REPL)
# caution: path[3] is reserved for script path (or '' in REPL)
# caution: path[4] is reserved for script path (or '' in REPL)
# caution: path[5] is reserved for script path (or '' in REPL)
# caution: path[6] is reserved for script path (or '' in REPL)
def SaveEventRequestFile(eventRequest):
    with open('events.json', 'w') as fp:
        json.dump(eventRequest, fp)

def ReadEventRequestFile():
    with open('events.json', 'r') as fp:
        eventRequestDict = json.load(fp)
        return eventRequestDict


def UpdateEventRequest(key, value):
    eventRequest = ReadEventRequestFile()
    eventRequest[key] = value
    SaveEventRequestFile(eventRequest)
#from ActiveDirectory import EmployeeActiveDirectory
# some_file.py
#import sys
#from .ActiveDirectory import EmployeeActiveDirectory
# some_file.py
#import sys
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)
# caution: path[0] is reserved for script path (or '' in REPL)

def getEventRequestStatus():
    eventRequest = ReadEventRequestFile()
    return eventRequest["status"]
