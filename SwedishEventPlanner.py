import sys
sys.path.insert(1, '/Users/manish/Desktop/Group 26/SwedishEventPlanners/ActiveDirectory')
sys.path.insert(3, '/Users/manish/Desktop/Group 26/SwedishEventPlanners/AdditionalRequests')

import LandingDashboard as LandingDashboard
import EventsActiveDirectory as EventsActiveDirectory
import MainActiveDirectory as menuActions
import EmployeeActiveDirectory as EmployeeActiveDirectory

login_successful, user_name = LandingDashboard.welcome_user()
print(login_successful)
print(user_name)

if login_successful == 1:
    user_role = EmployeeActiveDirectory.getRole(user_name)
    
    if user_role != "subTeam":
        menu_name = user_role + "Menu"
        menuActions.performMenuActions(menu_name)
    else:
        menuActions.subTeamMenu(user_name)