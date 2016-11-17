#--------------------------------------------------------------------------------------#
# Title: The Voodoo ToDo or Never Do Program
# Dev:   Gibran D. Washington
# Date:  November 6, 2016
# Desc:  Program creates to do list and writes to text file llowing user updates list
# ChangeLog: Too Many to Keep Track of over the past week!
#--------------------------------------------------------------------------------------#
print('''
                                        Voodoo ToDo

This Program is designed to help end the bad habits of not writing down tasks or completing
tasks based on the level of importance you assign. It stores your task list in a file for portability.

#######################################################################################################
''')

TDL = open("C:\\_PythonClass.\\ToDo1.txt", "r")
#-- Data --#
# declare variables and constants
taskLog =[]
dictList = {}

for items in TDL:
    print(TDL.readlines()[0])
    dictList = {"Pay Bills":"high"}
    for key, value in dictList.items():
        print("\nThis is a sample task in the Voodoo ToDo Program:", key)
        print("\nThis is the corresponding level of priority for the task:", value)
    continue
# close file from read status
TDL.close()

# setup for list dictionary array
taskHeaders = ["Task", "Priority"]
taskLog.insert(0,taskHeaders)
taskLog = [dictList]

#-- Processing --#
# perform task for user menu selection
select = None
while select != "0":

    print(
    '''
    Voodoo ToDo Menu Options:

    Press 0 - Exit Without Saving
    Press 1 - to Add task
    Press 2 - to Remove task
    Press 3 - to Save all tasks to the ToDo1.txt file and exit!
    '''
    )
# -- Presentation (I/O) --#
# get user menu option
    try:
        select = int(input("Please Make a Selection: "))
    except:
        print("You did not enter a valid #0 to 3 from menu\n")
        select = int(input("Please Make a Selection: "))
    # Exit Program Without Saving
    if select == "0":
        print("Exiting the Program!")
    break



# add a new task to the dictionary
    if select == "1":
        addTask = input("\nWhat is the new task to be added?: ")
        if addTask not in dictList:
# allows user to define priority level of new task
            addPriority = input("\nPlease Type the Priority level: \nHigh\nMedium\nLow\n")
            if (addPriority.lower() == "y"):
                dictList[addTask] = addPriority
            print("\n",addTask,"has been added to the list.\n")
        else:
            print("\nThe task is already in list! Use different name for the task.")



# deletes a user selected task from table
    elif select == "2":
        addTask = input("Which Task Would You Like to Remove?"
                        "You must type the complete task name/description!",dictList,"\n")
        if addTask in dictList:
            del dictList[addTask]
            print("\nAlright, The task--",  addTask, "--has been deleted from list")
        else:
            print("\nSorry, there was a problem--",addTask,"--was not found. Please check spelling.")



# Saves all task to file and exits program
    elif select == "3":
        strUserData = input("Press Any Key to Save Task and Exit Program: ")
# opens text file for writing
        TDL = open("C:\\_PythonClass.\\ToDo1.txt", "w")
        print("\nYour Task Data is Saving to ToDo1.txt")
# saves the list dictionary with new task appended
        TDL.write(taskLog, "\n")

# close write file ToDo.txt
TDL.close()