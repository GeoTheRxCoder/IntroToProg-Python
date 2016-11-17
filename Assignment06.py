#--------------------------------------------------------------------------------------#
# Title: Voodoo ToDo Program
# Dev:   Gibran D. Washington
# Date:  November 12, 2016
# Desc:  Program creates to do list and writes to text file allowing user updates list
# ChangeLog:(Who, When, What)
#   GDW, modification and edit of the 11/06/16 assignment along with parts from RRoot assignment 5 solution.
#   Program has been re-written implementing functions/methods and errors removed.
#--------------------------------------------------------------------------------------#
print('''
#######################################################################################################
                                        Voodoo ToDo

This Program is designed to help end the bad habits of not writing down tasks or completing
tasks based on the level of importance you assign. It stores your task list in a file for portability.

#######################################################################################################
''')
objTDLog = "C:\\_PythonClass\\ToDo.txt"
#-- Data --#
# declare variables and constants
# strData = A row of text data from the file
strData = ""
# dictList = A row of data separated into elements of a dictionary {Task,Priority}
dictList = {}
# taskRow = A dictionary that acts as a 'table' of rows
taskRow = []


# objTDL = An object that represents a file
objTDL = open(objTDLog, "r")
for line in objTDL:
    strData = line.split(",") # readline() reads a line of the data into 2 elements
    dictList = {"Task":strData[0].strip(), "Priority":strData[1].strip()}
    taskRow.append(dictList)
objTDL.close()

#  Display a menu of choices to the user
def menuChoice():
    '''function displays the menu options for users throughout the script'''
    print(
        """
        Voodoo ToDo Menu Options:

        Press 0 - Exit without saving.
        Press 1 - Add a new task.
        Press 2 - Remove an existing task.
        Press 3 - Save tasks to file and exit!
        Press 4 - Show current task
        """)

# a class for the methods that correspond to menu selection 1, 2, and 4
class TaskOrganizer():
    '''This class has 3 methods for editing the ToDo table list based on the menu selections'''

    # define method 1, add a task to table
    @staticmethod
    def AddTask():
        ''' this method allows user to add to the task list, appending to the dictionary'''
        strTask = str(input("What is the task? - ")).strip()
        strPriority = str(input("What is the priority? [high|medium|low] - ")).strip()
        dictList = {"Task": strTask, "Priority": strPriority}
        taskRow.append(dictList)

    # define method 2, remove a task from table
    @staticmethod
    def RemoveTask():
        '''removes a task selected through looking at every task and matching with user input'''
        strKeyToRemove = input("Which Task Would You Like to Remove? : ")
        blnItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        while (intRowNumber < len(taskRow)):
            # the values function creates a list!
            if (strKeyToRemove == str(list(dict(taskRow[intRowNumber]).values())[1])):
                del taskRow[intRowNumber]
                blnItemRemoved = True
            # end if
            intRowNumber += 1
        if blnItemRemoved == True:
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")
        print("******* The current task in ToDo are: *****")

    # function shows the list of current task
    @staticmethod
    def ShowAllTask():
        '''function shows all of the task that are currenly in the dictionary table'''
        for row in taskRow:
            print(row["Task"] + "(" + row["Priority"] + ")")



# -- Input/Output --#
while(True):
    # Display a menu of choices to the user
    menuChoice()
    # strSelect = Capture the user option selection
    strSelect = int(input("Please Make a Selection to begin [0 to 4]: "))

    #-- Processing --#
    # Show the current items in the table
    if strSelect == 4:
        print("******* The current task in ToDo are: *****")
        TaskOrganizer.ShowAllTask()
        print("*******************************************")

    # Add a new item to the list/Table
    elif strSelect == 1:
        TaskOrganizer.AddTask()
        print("Current task in table after adding data are:")
        TaskOrganizer.ShowAllTask()
        print("*******************************************")

    # remove item from the list/table
    elif strSelect == 2:
        TaskOrganizer.RemoveTask()
        print("******* The current task in ToDo are: *****")
        TaskOrganizer.ShowAllTask()
        print("*******************************************")
        # Display a menu of choices to the user
        menuChoice()


    # Show the current items in the table
    elif strSelect == 3:
        print("******* The current task in ToDo are: *****")
        TaskOrganizer.ShowAllTask()
        print("*******************************************")
        # Ask if they want save that data
        if ("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            objTDL = open(objTDLog, "a")
            for dicRow in taskRow:
                objTDL.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objTDL.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
            # Display a menu of choices to the user
        continue

    elif strSelect == 0:
        # Exit the program
        break