import EmployeeActiveDirectory as EmployeeAD

def login_user():
    login_status = 1
    print("Hello and welcome to the SEP system! Please provide your credentials.")
    entered_username = input("UserID: ").lower()
    entered_password = input("Key: ").lower()
    
    if entered_username not in EmployeeAD.allEmployees:
        print("Invalid Creds")
        login_status = 0
    elif entered_username != entered_password:
        print("Invalid Creds")
        login_status = 0
    else:
        print("Credentials match the AD. Welcome to SEP!")
    
    return login_status, entered_username
# caution: path[7] is reserved for script path (or '' in REPL)
def welcome_user():
    success_login, username = login_user()
    retry_count = 1

    while success_login != 1:
        if retry_count > 1:
            print("Account is locked.")
            break
        print("Retry attempt " + str(retry_count) + " of 2")
        success_login, username = login_user()
        retry_count += 1

    return success_login, username

if __name__ == "__main__":
    login_success, user_name = welcome_user()
    if login_success == 1:
        print("Welcome, " + user_name + "!")
    else:
        print("Failed Login.")
