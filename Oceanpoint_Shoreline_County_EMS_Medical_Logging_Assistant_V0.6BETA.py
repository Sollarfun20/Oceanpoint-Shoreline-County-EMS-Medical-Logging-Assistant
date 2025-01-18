


#Oceanpoint Shoreline County EMS Medical Logging Assistant
#Prototype Version V0.7BETA, internal usage ONLY
#Python 3.9 (64-bit)
#Windows Systems ONLY

#Program designed to make medical logging easier at EMS scenes for Oceanpoint, includes various additonal features. Operates via a terminal interface.

#Created by sollarfun20 :3

#Oceanpoint Shoreline County EMS Medical Logging Assistant © 2025 by Sollarfun20 is licensed under GNU Affero General Public License v3.0
#There is NO WARRANTY on this code and I am not liable for any damages to your system. See the liscence for more details.
#My carrd: https://sollarfun20.carrd.co/#
#My github: https://github.com/Sollarfun20


#PATCH NOTES(EST) 01:15 01/18/2025 - V0.7BETA
#Fixed dissapearing menu
#Re-formatted EMS log to display appropriately
#Added out of index exception prevention for EMS log
#Removed extrenous exceptions

#------------------------------------------------------------------------------------------------------------------------------------------------------

#******************************************************************** Import Modules: *****************************************************************

#------------------------------------------------------------------------------------------------------------------------------------------------------

from itertools import filterfalse
from tkinter import CURRENT
from winsound import PlaySound
import pyfiglet
from pyfiglet import print_figlet
import termcolor
from termcolor import colored, cprint
import os
from os import system, name
import datetime
import time
import playsound
from playsound import playsound
import winsound
import pyperclip
import colorama
from colorama import Fore, Style


#---------------------------------------------------------------------------------------------------------------------------------------------------

#******************************************************************** Variables: ********************************************************************

#---------------------------------------------------------------------------------------------------------------------------------------------------

#Patient Vitals Variables

PatientPulseList = []
#Historical pulses of the patient (integer)

PatientRespirationList = []
#Historical respiration rate of the patient (integer)

PatientSystolicBloodPressureList = []
#Historical systolic blood pressure of the patient (integer)

PatientDiastolicBloodPressureList = []
#Historical diastolic blood pressure of the patient (integer)

PatientBloodOxygenLevelList = []
#Historical blood oxygen level of the patient (integer)

#--------------------------------------------------------------------------------
#Patient Treatments and Injury Variables

PatientInjuriesList = []
#Patient injuries (string)

PatientTreatmentsList = []
#Treatments given to the patient during care (string)

PatientNotesList = []
#Miscellaneous notes from the provider during care (string)


#--------------------------------------------------------------------------------
#Miscellaneous Information

PatientLocation = None
#Patient Location in form of postal code (integer)

PatientName = None
#Patient Name in form of First, Last (string), John/Jane Doe if N/A

ProviderNamesList = []
#Provider Names in the form of usernames (strings)

EventsDescription = None
#Description of events for report (string)

ReportNotes = None
#Additional notes for report (string)

FinalReport = None
#Final Report for copy paste


#--------------------------------------------------------------------------------
#Technical storage Variables

CurrentInput = "Test"
#Stores the last input of the user as a string. Held by test placeholder for debugging.

DuringTreatment = False
#Vital for the Commands Check function, as it keeps the commands check loop running until it is marked as true and treatment is over.
#Marked as false until after the user starts the log in the welcome message function

ListCounter = None
#Used to annotate numbers onto items of data lists for update or removal commands

index = 0
#Global variable used to navigate all lists

StringHolder = None
#Global variable used to temporarily store a string

StringHolderSecond = None
#Global variable used to store a second string (end options usually)

SystolicBloodPressure = None
#Used to temporarily store a specific systolic blood pressure number into a string before it is combined with the diastolic for console printing

DiastolicBloodPressure = None
#Used to temporarily store a specific diastolic blood pressure number into a string before it is combined with the systolic for console printing

EndConfirmation = False
#Used at the end of the proccess of the Command Check usage to ensure the user wants to end transport and go to the end portion of the log. 
#Set as false by default until user confirms they want to continue.

BackupConfirmation = False
#Used for early exit of the logger

ProviderPingList = []
#Stores the providers userids as pings to be put in the final report

ExitConfirmation = False
#Technical variable used by welcome

length = None
#Used to store list length

#--------------------------------------------------------------------------------
#User Commands

#Cmds: Displays list of commands and usage


#---------------------------------------------------------------------------------------------------------------------------------------------------

#******************************************************************** Functions: ********************************************************************

#---------------------------------------------------------------------------------------------------------------------------------------------------
#Secondary Functions (lines of code that are called often and thus are stored and called in a function for ease of use)

#Takes in a string as part of the function parameters, and prints it to the console in the color blue

def PrintBlue(string, endoption):
    print(f'{Style.RESET_ALL}{Fore.BLUE}{string}{Style.RESET_ALL}', end=endoption)

#def PrintBlue(string, endoption):
    #cprint(string, 'blue' , None , None , no_color = False , force_color = True, end=endoption)
    #termcolor

#Takes in a string as part of the function parameters, and prints it to the console in the color purple
def PrintPurple(string, endoption):
    print(f'{Style.RESET_ALL}{Fore.MAGENTA}{string}{Style.RESET_ALL}', end=endoption)

#def PrintPurple(string, endoption):
    #cprint(string, 'magenta' , None , None , no_color = False , force_color = True, end=endoption)


#Takes in a string as part of the function parameters, and prints it to the console in the color red
def PrintRed(string, endoption):
    print(f'{Style.RESET_ALL}{Fore.RED}{string}{Style.RESET_ALL}', end=endoption)

#def PrintRed(string, endoption):
    #cprint(string, 'red' , None , None , no_color = False , force_color = True, end=endoption)


#Takes in a string as part of the function parameters, and prints it to the console in the color yellow
def PrintYellow(string, endoption):
    print(f'{Style.RESET_ALL}{Fore.YELLOW}{string}{Style.RESET_ALL}', end=endoption)

#def PrintYellow(string, endoption):
    #cprint(string, 'yellow' , None , None , no_color = False , force_color = True, end=endoption)



#Takes in a string as part of the function parameters, and prints it to the console in the color green
def PrintGreen(string, endoption):
    print(f'{Style.RESET_ALL}{Fore.GREEN}{string}{Style.RESET_ALL}', end=endoption)

#def PrintGreen(string, endoption):
    #cprint(string, 'green' , None , None , no_color = False , force_color = True, end=endoption)

#Clears all variables
def AllVariableClear():
    #Sets all variables to be treated globally
    global PatientPulseList
    global PatientRespirationList
    global PatientSystolicBloodPressureList
    global PatientDiastolicBloodPressureList
    global PatientBloodOxygenLevelList
    global PatientInjuriesList
    global PatientTreatmentsList
    global PatientNotesList
    global PatientLocation 
    global PatientName
    global ProviderNamesList
    global EventsDescription
    global ReportNotes
    global FinalReport
    global CurrentInput
    global DuringTreatment
    global ListCounter
    global index
    global StringHolder
    global SystolicBloodPressure
    global DiastolicBloodPressure
    global EndConfirmation
    global ProviderPingList

    #Clears all variables/resets to default states
    PatientPulseList.clear()
    PatientSystolicBloodPressureList.clear()
    PatientDiastolicBloodPressureList.clear()
    PatientRespirationList.clear()
    PatientBloodOxygenLevelList.clear()
    PatientInjuriesList.clear()
    PatientTreatmentsList.clear()
    PatientNotesList.clear()
    PatientLocation = None
    PatientPulseCheck = None
    ProviderNamesList.clear()
    EventsDescription = None
    ReportNotes = None
    FinalReport =  None
    CurrentInput = "Cleared."
    DuringTreatment = False
    ListCounter = None
    index = 0
    StringHolder = None
    SystolicBloodPressure = None
    ProviderPingList.clear()
    DiastolicBloodPressure = None


#---------------------------------------------------------------------------------------------------------------------------------------------------
#Patient Vitals-Related Function

#Queries user for the patient's pulse and appends input to pulse lit
def PatientPulseCheck():
    global CurrentInput
    print("Please enter the patient's pulse, a normal level is 60-100.")
    while True:
        try:
            CurrentInput = int(input())
            break
        except ValueError:
            PrintRed("Value Error: Please enter the patient's pulse as a valid number, a normal level is 60-100.", '\n')
    PatientPulseList.append(CurrentInput)
    PrintGreen("Patient pulse updated successfully.", '\n')


#Queries user for the patient's respiration rate and appends input to respiration list
def PatientRespirationCheck():
    global CurrentInput
    print("Please enter the patient's respiration rate or RR, a normal level is 12-20.")
    while True:
        try:
            CurrentInput = int(input())
            break
        except ValueError:
            PrintRed("Value Error: Please enter the patient's respiration rate as a valid number, a normal level is 12-20.", '\n')
    PatientRespirationList.append(CurrentInput)
    PrintGreen("Patient respiration rate updated successfully.", '\n')


#Queries user for the patient's systolic and diastolic BP's and appends to their respective lists
def PatientBloodPressureCheck():
    global CurrentInput
    print("Please enter the patient's systolic blood pressure or the top BP number, a normal level is about 120.")
    while True:
        try:
            CurrentInput = int(input())
            break
        except ValueError:
            PrintRed("Value Error: Please enter the patient's systolic blood pressure as a valid number, a normal level is about 120.", '\n')
    PatientSystolicBloodPressureList.append(CurrentInput)
    print("Please enter the patient's diastolic blood pressure or the bottom BP number, a normal level is about 80.")
    while True:
        try:
            CurrentInput = int(input())
            break
        except ValueError:
            PrintRed("Value Error: Please enter the patient's diastolic blood pressure as a valid number, a normal level is about 80.", '\n')
    PatientDiastolicBloodPressureList.append(CurrentInput)
    PrintGreen("Patient blood pressure updated successfully.", '\n')


#Queries user for the patient's blood oxygen level and appends the input to the oxygen level
def PatientBloodOxygenCheck():
    global CurrentInput
    print("Please enter the patient's blood oxygen level or SPO2 as a number without a percent, a normal level is above 94%")
    while True:
        try:
            CurrentInput = int(input())
            break
        except ValueError:
            PrintRed("Value Error: Please enter the patient's blood oxygen level as a valid number without a percent, a normal level is about 94%.", '\n')
    PatientBloodOxygenLevelList.append(CurrentInput)
    PrintGreen("Patient blood oxygen updated successfully.", '\n')

#---------------------------------------------------------------------------------------------------------------------------------------------------
#Vital Color Coding-Related Functions


#A function that takes a string in as transfer, checks the pulse list at the index against set parameter numbers, and sends the transfer string to be printed in the according color
def PulseColorCode(transfer, transfer2):
      if PatientPulseList[index] > 100:
            PrintPurple(transfer, transfer2)
      elif 0 < PatientPulseList[index] < 60:
            PrintRed(transfer, transfer2)
      elif 0 == PatientPulseList[index]:
            PrintBlue(transfer, transfer2)
      elif 60 <= PatientPulseList[index] <= 70:
            PrintBlue(transfer, transfer2)
      elif 90 <= PatientPulseList[index] < 100:
            PrintYellow(transfer, transfer2)
      else:
            PrintGreen(transfer, transfer2)


#A function that takes a string in as transfer, checks the respiration list at the index against set parameter numbers, and sends the transfer string to be printed in the according color
def RespirationColorCode(transfer, transfer2):
      #Color code the respiration rate of the patent
        if PatientRespirationList[index] > 20:
             PrintPurple(transfer, transfer2)
        elif 0 < PatientRespirationList[index] < 12:
             PrintRed(transfer, transfer2)
        elif 0 == PatientRespirationList[index]:
             PrintBlue(transfer, transfer2)
        elif 12 <= PatientRespirationList[index] <= 14:
            PrintYellow(transfer, transfer2)
        elif 18 <= PatientRespirationList[index] <= 20:
            PrintYellow(transfer, transfer2)
        else:
            PrintGreen(transfer, transfer2)


#A function that takes a string in as transfer, checks the blood pressure list at the index against set parameter numbers, and sends the transfer string to be printed in the according color
def BloodPressureColorCode(transfer, transfer2):
 #Color code the blood pressure of the patient
        if PatientSystolicBloodPressureList[index] != 120 or PatientDiastolicBloodPressureList[index] != 80:
            PrintYellow(transfer, transfer2)
        else:
            PrintGreen(transfer, transfer2)
      
            
#A function that takes a string in as transfer, checks the blood oxygen level list at the index against set parameter numbers, and sends the transfer string to be printed in the according color
def BloodOxygenColorCode(transfer, transfer2): 
  #Color code SPo2 level of patient
        if PatientBloodOxygenLevelList[index] <= 10:
             PrintBlue(transfer, transfer2)
        elif PatientBloodOxygenLevelList[index] <= 80:
             PrintRed(transfer, transfer2)
        elif PatientBloodOxygenLevelList[index] <= 90:
             PrintYellow(transfer, transfer2)
        elif PatientBloodOxygenLevelList[index] < 96:
             PrintYellow(transfer, transfer2)
        else:
             PrintGreen(transfer, transfer2) 


#Function that allows user to view the most recently entered set of vitals
def RecentVitalsPrintOut():
    index = -1

    StringHolder = f"Pulse: {PatientPulseList[index]}"
    PulseColorCode(StringHolder, '/n')

    StringHolder = f"RR: {PatientRespirationList[index]}"
    RespirationColorCode(StringHolder, '/n')

    SystolicBloodPressure = str(PatientSystolicBloodPressureList[index])
    DiastolicBloodPressure = str(PatientDiastolicBloodPressureList[index])
    StringHolder = f"BP: {SystolicBloodPressure}/{DiastolicBloodPressure}"
    BloodPressureColorCode(StringHolder, '/n')

    StringHolder = f"SPO2: {PatientBloodOxygenLevelList[index]}%"
    BloodOxygenColorCode(StringHolder, '/n')
   
    
#Function that allows the user to view out all historical patient vitals, color coded
def FullVitalsPrintOut():
    StringHolderSecond = " "
    index = 0
    length = len(PatientPulseList) - 1
    for items in PatientPulseList:
        if index == 0:
            StringHolder = f"Pulse: {PatientPulseList[index]} ->"
        elif index == length:
            StringHolder = f"{PatientPulseList[index]}"
        else:
            StringHolder = f"{PatientPulseList[index]} ->"
        PulseColorCode(StringHolder, StringHolderSecond)
        index = index + 1

    print("\n")
    index = 0
    length = len(PatientRespirationList) - 1
    for items in PatientRespirationList:
        if index == 0:
            StringHolder = f"RR: {PatientRespirationList[index]} ->"
        elif index == length:
            StringHolder = f"{PatientRespirationList[index]}"
        else:
            StringHolder = f"{PatientRespirationList[index]} ->"
        RespirationColorCode(StringHolder, StringHolderSecond)
        index = index + 1

    print("\n")
    index = 0
    length = len(PatientSystolicBloodPressureList) - 1
    for items in PatientSystolicBloodPressureList:
        SystolicBloodPressure = str(PatientSystolicBloodPressureList[index])
        DiastolicBloodPressure = str(PatientDiastolicBloodPressureList[index])
        if index == 0:
            StringHolder = f"BP: {SystolicBloodPressure}/{DiastolicBloodPressure} ->"
        elif index == length:
            StringHolder = f"{SystolicBloodPressure}/{DiastolicBloodPressure}"
        else:
            StringHolder = f"{SystolicBloodPressure}/{DiastolicBloodPressure} ->"
        BloodPressureColorCode(StringHolder, StringHolderSecond)
        index = index + 1

    print("\n")
    index = 0
    length = len(PatientBloodOxygenLevelList) - 1
    for items in PatientBloodOxygenLevelList:
        if index == 0:
            StringHolder = f"SPO2: {PatientBloodOxygenLevelList[index]}% ->"
        elif index == length:
            StringHolder = f"{PatientBloodOxygenLevelList[index]}%"
        else:
            StringHolder = f"{PatientBloodOxygenLevelList[index]}% ->"
        BloodOxygenColorCode(StringHolder, StringHolderSecond)

        index = index + 1
    print("\n")


#Function that allows the user to update all patient vitals
def UpdateVitals():
    PatientPulseCheck()
    PatientRespirationCheck()
    PatientBloodPressureCheck()
    PatientBloodOxygenCheck()


#---------------------------------------------------------------------------------------------------------------------------------------------------
#Patient Injury-Related Functions

#Queries user for the patient's injuries and appends the inputs to the Patient Injuries List
def PatientInjuryCheck():
   global CurrentInput
   CurrentInput == "clear"
   while CurrentInput != "end":
        CurrentInput = input('Please enter the patient\'s injuries one at a time seperated by different instances of enter, type "end" when done.')
        if CurrentInput == "cancel":
            PrintRed("Proccess aborted.", '\n')
            return
        elif CurrentInput != "end":
            PatientInjuriesList.append(CurrentInput)
        else:
            PrintGreen("Patient injuries updated successfully.", '\n')
            return


#Function that allows the user to see all patient injures in a numbered list, enter the according number of one of the injuries, and then replace the injury's entry
def UpdateInjuries():
    global CurrentInput
    index=0
    for items in PatientInjuriesList:
        ListCounter = index + 1
        print(f"{ListCounter}. {PatientInjuriesList[index]}")
        index = index + 1
    print("Please enter the number of the injury you wish to update.")
    while True:
        try:
            CurrentInput = int(input())
            break
        except ValueError:
            PrintRed("Value Error: Please enter the number of the injury you wish to update as a valid number.", '\n')
    index = CurrentInput - 1
    CurrentInput = input('Please type the update for the specified injury, press the enter key when done. Type "cancel" to cancel.')
    if CurrentInput == "cancel":
        PrintRed("Proccess aborted.", '\n')
        return
    PatientInjuriesList[index] = CurrentInput
    PrintGreen("Entry updated successfully.", '\n')


#Function that allows the user to see all patient injuries in a numbered list, enter the according number of one of the injuries, which will then be removed from the patient injuries list
def RemoveInjury():
    global CurrentInput
    index=0
    for items in PatientInjuriesList:
        ListCounter = index + 1
        print(f"{ListCounter}. {PatientInjuriesList[index]}")
        index = index + 1
    print("Please enter the number of the injury you wish to delete.")
    while True:
        try:
            CurrentInput = int(input())
            break
        except ValueError:
            PrintRed("Value Error: Please enter the number of the injury you wish to delete as a valid number.", '\n')
    index = CurrentInput - 1
    PatientInjuriesList.pop(index)
    PrintGreen("Entry successfully removed.", '\n')


#Function that allows the user to see all of the patient injuries
def ViewInjury():
    print(PatientInjuriesList)


#---------------------------------------------------------------------------------------------------------------------------------------------------
#Patient Notes-Related Functions

#Function that allows the user to add a patient note, which will be appended to the patient notes list
def AddNote():
    CurrentInput = input("Enter your patient note, press the enter key when done.")
    PatientNotesList.append(CurrentInput)
    PrintGreen("Entry added successfully.", '\n')


#Function that allows the user to see all patient notes in a numbered list, and remove any of them by entering the number of the note they wish to delete
def RemoveNote():
    global CurrentInput
    index=0
    for items in PatientNotesList:
        ListCounter = index + 1
        print(f"{ListCounter}. {PatientNotesList[index]}")
        index = index + 1
    print("Please enter the number of the note you wish to delete.")
    while True:
        try:
            CurrentInput = int(input())
            break
        except ValueError:
            PrintRed("Value Error: Please enter the number of the note you wish to delete as a valid number.", '\n')
    index = CurrentInput - 1
    PatientNotesList.pop(index)
    PrintGreen("Entry successfully removed.", '\n')


#Function that will print ouf all of the patients notes, one line after another, seperated by one line in between each.
def ViewNotes():
    global CurrentInput
    index=0
    for items in PatientNotesList:
        print(f"{PatientNotesList[index]}")
        print("\n")
        index = index + 1
    print("End of patient notes.")


#---------------------------------------------------------------------------------------------------------------------------------------------------
#Patient Treatment-Related Functions

#Function that allows the user to add as many patient treatments as desired, which will be appended to the list, unti they type "end"
def AddTreatment():
    global CurrentInput
    CurrentInput = "Cleared."
    while CurrentInput != "end":
        CurrentInput = input('Please enter the given treatments one at a time seperated by different instances of enter, type "end" when done.')
        if CurrentInput == "cancel":
            PrintRed("Proccess aborted successfully.", '\n')
            return
        elif CurrentInput != "end":
            PatientTreatmentsList.append(CurrentInput)
        else:
            PrintGreen("Patient Treatments updated succesfully.", '\n')
            return


#Function that allows the user to see all patient treatments in a numbered list, input the according number of the treatment to change, and to replace that treatment in the list
def UpdateTreatment():
    global CurrentInput
    index=0
    for items in PatientTreatmentsList:
        ListCounter = index + 1
        print(f"{ListCounter}. {PatientTreatmentsList[index]}")
        index = index + 1
    print("Please enter the number of the treatment you wish to update.")
    while True:
        try:
            CurrentInput = int(input())
            break
        except ValueError:
            PrintRed("Value Error: Please enter the number of the treatment you wish to update as a valid number.", '\n')
    index = CurrentInput - 1
    CurrentInput = input('Please type the update for the specified treatment, press the enter key when done. Type "cancel" to cancel.')
    if CurrentInput == "cancel":
       PrintRed("Proccess aborted successfully.", '\n')
       return
    else:
        PatientTreatmentsList[index] = CurrentInput
        PrintGreen("Entry updated successfully.", '\n')


#---------------------------------------------------------------------------------------------------------------------------------------------------
#Miscellaneous Command Functions

#Set a timer for the AED for 3 minutes, when done play a sound and print a text letting them know the AED timer is completed.
def AEDTimer():
    TimeRemaining = 180                                       #Sets time remaining to 180 seconds (3 minutes)
    while TimeRemaining > 0:                                  #Keeps running until time remaining is at 0 (3 minutes up)
        timer = datetime.timedelta(seconds = TimeRemaining)   #Sets timer to time remaining
        print (timer, end="\r")                               #Prints time left on timer
        time.sleep(1)                                         #Pauses program for 1 second
        TimeRemaining = TimeRemaining - 1                     #Reduces time remaining by 1 second
        


    i = 0
    print("3 Minute AED timer has completed, please check the AED.")  #Prints Alert Text in Console
    while i <= 4:                                                     #Play a sound via windows speakers at a frequency of 2000hz for .25 seconds, with .1 second in between, 4 times.
        winsound.Beep(2000,250)
        time.sleep(.1)
        i = i +1


#---------------------------------------------------------------------------------------------------------------------------------------------------
#Primary, Critical Program Functions

#Function that continously checks for commands, triggers reponses, and finalizes report
def CommandsCheck():
    global CurrentInput
    global DuringTreatment
    while DuringTreatment == True:
        CurrentInput = input()

    #LAST/RECENT VITALS Command, gives most recent set of all vitals taken
        if CurrentInput in ["lastvitals", "lstvitals", "lvt"]:
            RecentVitalsPrintOut()

    #ALL/HISTORICAL VITALS command, gives all historical vitals color coded
        elif CurrentInput in ["allvitals", "vitalhistory", "vitalshistory", "hstvitals", "hvt"]:
            FullVitalsPrintOut()

    #UPDATE ALL VITALS command, allows the user to update all vitals with new values
        elif CurrentInput in ["updatevitals", "updvitals", "uvt"]:
            UpdateVitals()

    #UPDATE PULSE command, allows the user to update the patient's pulse with a new value
        elif CurrentInput in ["updatepulse", "updpulse", "upl"]:
            PatientPulseCheck()
    
    #UPDATE RESPIRATION RATE command, allows the user to update the patient's respiration rate with a new value
        elif CurrentInput in ["updaterr", "updresp", "updrr", "updaterespiration", "updrespiration", "urr"]:
            PatientRespirationCheck()

    #UDATE BLOOD PRESSURE command, allows the user to update the patient's blood pressure with a new value
        elif CurrentInput in ["updatebp", "updbp", "updatebloodpressure", "updbloodpressure", "ubp"]:
            PatientBloodPressureCheck()

    #UDATE SPO2/BLOOD OXYGEN command, allows the user to update the patient's spo2 level with a new value
        elif CurrentInput in ["updatespo2", "updateoxygen", "updspo2", "updoxygen", "updoxy", "uspo2"]:
            PatientBloodOxygenCheck()

    #ADD PATIENT INJURIES command, allows the user to add additional injuries to the patient's list of injuries
        elif CurrentInput in ["addinjury", "addinj", "ainj"]:
            PatientInjuryCheck()

    #UPDATE PATIENT INJURIES command, allows the user to replace one of the patient injuries from the patient injuries list with a new value
        elif CurrentInput in ["updateinjury", "updinjury", "updinj", "uinj"]:
            UpdateInjuries()

    #REMOVE PATIENT INJURY command, allows the user to remove one of the patient injuries from the patient injuries list
        elif CurrentInput in ["removeinjury", "rmvinjury", "rmvinj", "rinj"]:
            RemoveInjury()

    #VIEW PATIENT INJURIES command, allows the user to view all of the patient injuries in the patient injuries list
        elif CurrentInput in ["viewinjury", "vwinjury", "vwinj", "vinj"]:
            ViewInjury()

    #ADD NOTE command, allows the user to add a new patient note to the patient notes list
        elif CurrentInput in ["addnote", "addnt", "adnote", "ant"]:
            AddNote()
    
    #REMOVE NOTE command, allows the user to remove a patient note from the patient notes list
        elif CurrentInput in ["removenote", "rmvnote", "removent", "rmvnt", "rnt"]:
            RemoveNote()
    
    #VIEW NOTES command, allows the user to view all the patient notes in the patient notes list
        elif CurrentInput in ["viewnotes", "viewnote", "vwnote", "vwnotes", "viewnt", "vnt"]:
            ViewNotes()

    #ADD TREATMENT command, allows the user to add treatments to the patient treatments list
        elif CurrentInput in ["addtreatment", "addtrm", "adtreatment", "atrm"]:
            AddTreatment()

    #UPDATE TREATMENT command, allows the user to update a specific treatment from the patient treatments list with a new value
        elif CurrentInput in ["updatetreatment", "updtreatment", "updatetrm", "utrm"]:
            UpdateTreatment()

    #END LOG/TREATMENT command, initiates the end of the patient treatment functionality and gets final information and printout of medical log
        elif CurrentInput in ["endlog", "endtreatment", "endtreat"]:
            global EndConfirmation
            print("Are you sure you want to end treatment functionality and move on to report finalization? y/n")
            PrintRed("Please note: All patient data, information, and notes will be finalized after this point into the report.", "\n")

            while EndConfirmation == False: #Keeps on looping the function until the user has confirmed that they want to end treatment or cancel the action
                CurrentInput=input()

                if CurrentInput == "y":            #Checks if the user input affirmed they want to end the treatment section
                    DuringTreatment = False        #Ends the in-treatment functionality loop

                    CurrentInput = input('Please enter the approximate postal code of the scene in the form "P1234".')
                    PatientLocation = CurrentInput #Writes the user input to the patient location variable

                    CurrentInput = input('Please enter the patient\'s username. Enter "John Doe"(male) or "Jane Doe"(female) if it is unknown.')
                    PatientName = CurrentInput     #Writes the user input to the patient name variable
                    CurrentInput = "Cleared."      #Clears the current input with a placeholder to ensure no conflicts

                    while CurrentInput != "end":   #Keeps looping the function until the user has stated they want to stop entering providers
                         print('Please enter the discord user ids of the care providers at the scene, seperating each entry with the enter key. Type "end" when done.')
                         CurrentInput = input()
                         if CurrentInput != "end":  #Appends the user input to the provider names list if it doesn't state "end"
                            ProviderNamesList.append(CurrentInput)
                            index = 0
                            for items in ProviderNamesList:
                                ProviderPingList.append(f'<@{ProviderNamesList[index]}>')
                                index = index + 1

                    CurrentInput = input("Please type a description of events for the log. Press the enter key when done.")
                    EventsDescription = CurrentInput #Writes the user input to the events description variable

                    CurrentInput = input('Please enter any additional notes for the log (ex: Had to stage prior, etc...), state "N/A" if not applicable. Press the enter key when done.')
                    ReportNotes = CurrentInput       #Writes the user input to the report notes variable

                    #Exception due to no entry preventer
                    if len(PatientSystolicBloodPressureList) == 0:
                        PatientSystolicBloodPressureList.append("N/A")
                    if len(PatientDiastolicBloodPressureList) == 0:
                        PatientDiastolicBloodPressureList.append("N/A")
                    if len(ProviderPingList) == 0:
                        ProviderPingList.append("N/A")
                    if len(PatientBloodOxygenLevelList) == 0:
                        PatientBloodOxygenLevelList.append("N/A")
                    if len(PatientTreatmentsList) == 0:
                        PatientTreatmentsList.append("N/A")

                    #Place all variables into final report variable as a multi-line string
                    FinalReport = f""":emslogo:   **EMS Call Log**
:emsline::emsline::emsline::emsline::emsline::emsline::emsline::emsline::emsline::emsline::emsline::emsline::emsline::emsline::emsline::emsline::emsline::emsline::emsline:
**EMS Providers Involved: {ProviderPingList} **
**Approx. Postal: {PatientLocation} **
                    
**Initial Patient Condition/Injuries: {PatientInjuriesList} **
**Patient Vitals(Initial -> Final):**
> **Pulse:** {PatientPulseList[0]} ** -> ** {PatientPulseList[-1]}
> **Respiration Rate:** {PatientRespirationList[0]} ** -> ** {PatientRespirationList[-1]}
> **Blood Pressure:** {PatientSystolicBloodPressureList[0]}/{PatientDiastolicBloodPressureList[0]} ** -> ** {PatientSystolicBloodPressureList[-1]}/{PatientDiastolicBloodPressureList[-1]}
> **Blood Oxygen Level:** {PatientBloodOxygenLevelList[0]} ** -> ** {PatientBloodOxygenLevelList[-1]}
**Interventions + Medications Administered:** {PatientTreatmentsList}
                    
**Description of Events:** {EventsDescription}
**Other Notes (Ex. Units had to stage before entry):** {ReportNotes}"""
               
                    #Allows while loop for end confirmation to be ended
                    EndConfirmation = True

                    #Copies final report to clipboard and prints it into the terminal
                    pyperclip.copy(FinalReport)
                    print(FinalReport)
                    print("\n")
                    print('Final report copied to your clipboard, if this does not work, copy the report above and paste it into the channel. Type "done" when complete and press enter.')

                    CurrentInput = "Cleared."
                    while CurrentInput != "done":
                        CurrentInput = input()
                        if CurrentInput != "done":
                            PrintRed('Command not recognized. Type "done" when complete.')
                        else: 
                            #Clears the interface to start fresh again
                            print("Patient Treatment Complete, refreshing terminal...")
                            time.sleep(1)
                            i = 0
                            while i < 30:
                                print("\n")
                                i = i + 1
                            #Calls variable clearer
                            AllVariableClear()
                            colors = "244;5;5:"
                            print_figlet("M E D", font = "5lineoblique", justify = "center", width = 130, colors=colors)
                            print_figlet("L O G G E R", font = "5lineoblique", justify = "center", width = 130, colors=colors)
                            print_figlet("A S S I S T A N T", font = "5lineoblique", justify = "center", width = 130, colors=colors)
                            return

                elif CurrentInput == "n": #Checks if the user canceled the proccess
                    print("Cancelled.")   
                    EndConfirmation = True #Changes EndConfirmation to true, ending the loop

                else: #Catch all for any inputs that don't match "y" or "n"
                    print('Command not recognized, please type "y" to confirm treatment and transport completion or "n" to cancel')
                    EndConfirmation = False


    #AED TIMER command, starts a timer for 3 minutes for the user for AED analyzation, will play a sound and display text when 3 minutes are up
        elif CurrentInput in ["aedtimer", "aedtm"]:
            AEDTimer()
            
    #CANCEL command, exits and goes back to the start menu
        elif CurrentInput in ["cancelpatient", "cancelpt", "cnclpatient", "cnclpt", "cpt"]:
            print('Are you sure you want to cancel the patient log? Type "y" to confirm or "n" to abort.')
            BackupConfirmation = False
            while BackupConfirmation != True:
                CurrentInput = input()
                if CurrentInput == "y":
                    BackupConfirmation = True
                    print("Cancelling patient log...")
                    time.sleep(1)
                    i = 0
                    while i < 30:
                        print("\n")
                        i = i + 1
                    AllVariableClear()
                    colors = "244;5;5:"
                    print_figlet("M E D", font = "5lineoblique", justify = "center", width = 130, colors=colors)
                    print_figlet("L O G G E R", font = "5lineoblique", justify = "center", width = 130, colors=colors)
                    print_figlet("A S S I S T A N T", font = "5lineoblique", justify = "center", width = 130, colors=colors)
                    print(colored('Welcome to the SCEMS Med Logger Assistant, type in "start" to start a log' , 'red' , None , None , no_color = False , force_color = True))

                    return
                elif CurrentInput == "n":
                    print("Patient log cancellation aborted.")
                    BackupConfirmation = True
                else:
                    print('Command not recognized, please type "y" to confirm patient log cancellation or "n" to abort.')
    #COMMAND LIST command, lists all commands
        elif CurrentInput in ["commandslist", "commandlist", "cmdlist", "commandlst", "cmdlst", "command", "commands", "cmd", "cmds"]:
            print("""List of commands:

            Commands List ("commandslist", "commandlist", "cmdlist", "commandlst", "cmdlst", "command", "commands", "cmd", "cmds"):
            Displays the full list of available commands.

            Last Vitals ("lastvitals", "lstvitals", "lvt"):
            Displays the most recent entered set of patient vitals(pulse, RR, BP, SPo2), color coded.

            All Vitals ("allvitals", "vitalhistory", "vitalshistory", "hstvitals", "hvt")
            Displays the full vital history of the patient(pulse, RR, BP, Spo2), color coded.

            Update All Vitals ("updatevitals", "updvitals", "uvt")
            Prompts to update all patient vitals (pulse, RR, BP, SPo2) with the most recent vitals.

            Update Pulse ("updatepulse", "updpulse", "upl")
            Prompts to update the patient's pulse with the most recent reading.

            Update Respiration Rate("updaterr", "updresp", "updrr", "updaterespiration", "updrespiration", "urr")
            Prompts to update the patient's respiration rate with the most recent reading.

            Update Blood Pressure("updatebp", "updbp", "updatebloodpressure", "updbloodpressure", "ubp")
            Prompts to update the patient's blood pressure with the most recent reading.

            Update Blood Oxygen Level("updatespo2", "updateoxygen", "updspo2", "updoxygen", "updoxy", "uspo2")
            Prompts to update the patient's blood oxygen level(SPO2) with the most recent reading.

            Add Patient Injuries ("addinjury", "addinj", "ainj")
            Prompts to add addtional patient injuries to injury list. Type "cancel" to abort this proccess.

            Update Patient Injuries ("updateinjury", "updinjury", "updinj", "uinj")
            Displays numbered list of all patient injuries and prompts to select a number. The selected entry can then be overwritten/updated, can be aborted with cancel.

            Remove Patient Injury ("removeinjury", "rmvinjury", "rmvinj", "rinj")
            Displays numbered list of all patient injuries and prompts to select a number. The selected entry will then be deleted.

            View Patient Injuries ("viewinjury", "vwinjury", "vwinj", "vinj")
            Displays all patient injuries.

            Add Patient Note ("addnote", "addnt", "adnote", "ant")
            Prompts to type a patient note, and press the enter key when done. Typed note will be saved and viewable with the view patient notes command.

            Remove Patient Note ("removenote", "rmvnote", "removent", "rmvnt", "rnt")
            Displays numbered list of all patient notes and prompts to select a number. The selected entry will then be deleted.

            View Patient Notes ("viewnotes", "viewnote", "vwnote", "vwnotes", "viewnt", "vnt")
            Displays all patient notes.

            Add Patient Treatment ("addtreatment", "addtrm", "adtreatment", "atrm")
            Prompts to add additional patient patient treatments to the treatment list. Type "cancel" to abort this proccess.

            Update Patient Treatment ("updatetreatment", "updtreatment", "updatetrm", "utrm")
            Displays numbered list of all patient treatments and prompts to select a number. The selected entry can then be overwritten/updated, type "cancel" to cancel.

            AED Timer ("aedtimer", "aedtm")
            Sets a 3 minute timer for AED rythym analyzation. Will play a sound and prompt on display when timer is done.

            End Log/Patient Treatment ("endlog", "endtreatment", "endtreat")
            Allows finalization of log and will exit the treatment phase of the application. Can be aborted, please note if confirmed all vitals and other patient information will be finalized into the log.

            Cancel Patient Treatment ("cancelpatient", "cancelpt", "cnclpatient", "cnclpt", "cpt")
            Alows to cancel current log and return to main menu.

            Start New Patient Log ("start")
            Starts a new patient log
            """)

        else:
            PrintRed('Command not recognized. Please see the documentation or type "cmd" for a list of all valid commands, their usage, and shorthand means of referencing them.', "\n")


#Function that makes the welcome screen of the logger, and waits for the user to input "start" to start a log
def WelcomeMessage():
    time.sleep(2)
    global CurrentInput
    #Welcome Message, and start prompter
    colors = "244;5;5:"
    print_figlet("M E D", font = "5lineoblique", justify = "center", width = 130, colors=colors)
    print_figlet("L O G G E R", font = "5lineoblique", justify = "center", width = 130, colors=colors)
    print_figlet("A S S I S T A N T", font = "5lineoblique", justify = "center", width = 130, colors=colors)

    print(colored('Welcome to the SCEMS Med Logger Assistant, type in "start" to start a log' , 'red' , None , None , no_color = False , force_color = True))
    while ExitConfirmation == False:
        CurrentInput = input()
        if CurrentInput == "start":
            global DuringTreatment
            PrintGreen("New patient log started.", '\n')
            PatientPulseCheck()
            PatientRespirationCheck()
            PatientInjuryCheck()
            print("Initial information complete, for further information notation and access please use the commands, type cmds for a list of commands.")
            DuringTreatment = True
            ExitConfirmation == True
            CommandsCheck()

        else: #command not recognized/start not typed
            print(colored('Command not recognized.' , 'red' , None , None , no_color = False , force_color = True))


#--------------------------------------------------------------------------------

#Keep running code indefinitely
while 1 == 1:
    WelcomeMessage()
    EndConfirmation = False
    ExitConfirmation == False

#---------------------------------------------------------------------------------------------------------------------------------------------------

#End of code, hope you found this program useful, reminder all code is liscenced under GNU Affero General Public License v3.0 (please see top for liscence details)
