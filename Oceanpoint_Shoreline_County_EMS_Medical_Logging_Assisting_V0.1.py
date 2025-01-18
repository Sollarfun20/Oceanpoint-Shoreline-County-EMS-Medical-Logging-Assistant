#Medical Logging Assistant Software

#Program designed to make medical logging easier at EMS scenes


#Import Modules
from re import L
from tkinter import CURRENT
import pyfiglet
from pyfiglet import print_figlet
import termcolor
from termcolor import colored
import os

#--------------------------------------------------------------------------------
#Variables


#Vital Variables

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
#Technical Variables

CurrentInput = "Test"

DuringTreatment = False

OutputColor = None

ListCounter = None

index = 0

StringHolder = None

SystolicBloodPressure = None

DiastolicBloodPressure = None


#Current User Input


#--------------------------------------------------------------------------------
#User Commands

#Cmds: Displays list of commands and usage



#Functions:
#--------------------------------------------------------------------------------

#Queries user for the patient's pulse and appends input to pulse lit
def PatientPulseCheck():
    CurrentInput = int(input("Please enter the patient's pulse, a normal level is 60-100."))
    PatientPulseList.append(CurrentInput)


#Queries user for the patient's respiration rate and appends input to respiration list
def PatientRespirationCheck():
    CurrentInput = int(input("Please enter the patient's respiration rate or RR, a normal level is 12-20."))
    PatientRespirationList.append(CurrentInput)

#Queries user for the patient's systolic and diastolic BP's and appends to their respective lists
def PatientBloodPressureCheck():
    CurrentInput = int(input("Please enter the patient's systolic blood pressure or the top BP number, a normal level is about 120."))
    PatientSystolicBloodPressureList.append(CurrentInput)
    CurrentInput = int(input("Please enter the patient's diastolic blood pressure or the bottol BP number, a normal level is about 80."))
    PatientDiastolicBloodPressureList.append(CurrentInput)

#Queries user for the patient's blood oxygen level and appends the input to the oxygen level
def PatientBloodOxygenCheck():
    CurrentInput = int(input("Please enter the patient's blood oxygen level or SPO2 as a number without a percent, a normal level is above 94%."))
    PatientBloodOxygenLevelList.append(CurrentInput)

#Queries user for the patient's injuries and appends the inputs to the Patient Injuries List
def PatientInjuryCheck():
    CurrentInput = input('Please enter the patient\'s injuries one at a time seperated by different instances of enter, type "end" when done.')
    PatientInjuriesList.append(CurrentInput)
    while CurrentInput != "end":
        CurrentInput = input('Please enter the patient\'s injuries one at a time seperated by different instances of enter, type "end" when done.')
        if CurrentInput != "end":
            PatientInjuriesList.append(CurrentInput)
            print("Patient injuries updated successfully.")




def PrintBlue(string):
    print(colored(string, 'blue' , None , None , no_color = False , force_color = True))

def PrintPurple(string):
    print(colored(string, 'magenta' , None , None , no_color = False , force_color = True))

def PrintRed(string):
    print(colored(string, 'red' , None , None , no_color = False , force_color = True))

def PrintYellow(string):
    print(colored(string, 'yellow' , None , None , no_color = False , force_color = True))

def PrintGreen(string):
    print(colored(string, 'green' , None , None , no_color = False , force_color = True))

#transfer is a string to be sent out to be printed
def PulseColorCode(transfer):
      if PatientPulseList[index] > 100:
            PrintPurple(transfer)
      elif 0 < PatientPulseList[index] < 60:
            PrintRed(transfer)
      elif 0 == PatientPulseList[index]:
            PrintBlue(transfer)
      elif 60 <= PatientPulseList[index] <= 70:
            PrintYellow(transfer)
      elif 90 <= PatientPulseList[index] < 100:
            PrintYellow(transfer)
      else:
            PrintGreen(transfer)

#transfer is a string to be sent out to be printed
def RespirationColorCode(transfer):
      #Color code the respiration rate of the patent
        if PatientRespirationList[index] > 20:
             PrintPurple(transfer)
        elif 0 < PatientRespirationList[index] < 12:
             PrintRed(transfer)
        elif 0 == PatientRespirationList[index]:
             PrintBlue(transfer)
        elif 12 <= PatientRespirationList[index] <= 14:
            PrintYellow(transfer)
        elif 18 <= PatientRespirationList[index] <= 20:
            PrintYellow(transfer)
        else:
            PrintGreen(transfer)

#transfer is a string to be sent out to be printed
def BloodPressureColorCode(transfer):
 #Color code the blood pressure of the patient
        if PatientSystolicBloodPressureList[index] != 120 or PatientDiastolicBloodPressureList[index] != 80:
            PrintYellow(transfer)
        else:
            PrintGreen(transfer)
       
#transfer is a string to be sent out to be printed
def BloodOxygenColorCode(transfer): 
  #Color code SPo2 level of patient
        if PatientBloodOxygenLevelList[index] <= 10:
             PrintBlue(transfer)
        elif PatientBloodOxygenLevelList[index] <= 80:
             PrintRed(transfer)
        elif PatientBloodOxygenLevelList[index] <= 90:
             PrintYellow(transfer)
        elif PatientBloodOxygenLevelList[index] < 96:
             PrintYellow(transfer)
        else:
             PrintGreen(transfer) 

def RecentVitalsPrintOut():
    index = -1

    StringHolder = PatientPulseList[index]
    PulseColorCode(StringHolder)

    StringHolder = PatientRespirationList[index]
    RespirationColorCode(StringHolder)

    SystolicBloodPressure = str(PatientSystolicBloodPressureList[index])
    DiastolicBloodPressure = str(PatientDiastolicBloodPressureList[index])
    StringHolder = SystolicBloodPressure + "/" + DiastolicBloodPressure
    BloodPressureColorCode(StringHolder)

    StringHolder = PatientBloodOxygenLevelList[index]
    BloodOxygenColorCode(StringHolder)
   
    

def FullVitalsPrintOut():
    index = 0
    for items in PatientPulseList:
        StringHolder = str(PatientPulseList[index]) + " -> "
        PulseColorCode(StringHolder)

        StringHolder = str(PatientRespirationList[index]) + " -> "
        RespirationColorCode(StringHolder)

        SystolicBloodPressure = str(PatientSystolicBloodPressureList[index])
        DiastolicBloodPressure = str(PatientDiastolicBloodPressureList[index])
        StringHolder = SystolicBloodPressure + "/" + DiastolicBloodPressure + " -> "
        BloodPressureColorCode(StringHolder)

        StringHolder = PatientBloodOxygenLevelList[index]
        BloodOxygenColorCode(StringHolder)

        index = index + 1


def UpdateVitals():
    PatientPulseCheck
    PatientRespirationCheck
    PatientBloodPressureCheck
    PatientBloodOxygenCheck








def UpdateInjuries():
    index=0
    for items in PatientInjuriesList:
        ListCounter = index + 1
        print(f"{ListCounter}. {PatientInjuriesList[index]}")
        index = index + 1
    CurrentInput = int(input("Please select the number of the injury you wish to update."))
    index = CurrentInput - 1
    CurrentInput = input("Please type the update for the specified injury, press the enter key when done.")
    PatientInjuriesList[index] = CurrentInput
    print("Entry updated successfully.")


def RemoveInjury():
    index=0
    for items in PatientInjuriesList:
        ListCounter = index + 1
        print(f"{ListCounter}. {PatientInjuriesList[index]}")
        index = index + 1
    CurrentInput = int(input("Please select the number of the injury you wish to delete."))
    index = CurrentInput - 1
    PatientInjuriesList.pop(index)
    print("Entry successfully removed.")



def ViewInjury():
    print(PatientInjuriesList)

def AddNote():
    CurrentInput = input("Enter your patient note, press the enter key when done.")
    PatientNotesList.append(CurrentInput)
    print("Entry added successfully.")


def RemoveNote():
    index=0
    for items in PatientNotesList:
        ListCounter = index + 1
        print(f"{ListCounter}. {PatientNotesList[index]}")
        index = index + 1
    CurrentInput = int(input("Please select the number of the note you wish to delete."))
    index = CurrentInput - 1
    PatientNotesList.pop(index)
    print("Entry successfully removed.")

def ViewNotes():
    index=0
    for items in PatientNotesList:
        print(f"{PatientNotesList[index]}")
        index = index + 1
    print("End of patient notes.")

def AddTreatment():
    CurrentInput = input('Please enter additional patient treatments one at a time seperated by different instances of enter, type "end" when done.')
    PatientTreatmentsList.append(CurrentInput)
    while CurrentInput != "end":
        CurrentInput = input('Please enter the patient\'s injuries one at a time seperated by different instances of enter, type "end" when done.')
        if CurrentInput != "end":
            PatientTreatmentsList.append(CurrentInput)
            print("Patient Treatments updated succesfully.")

#--------------------------------------------------------------------------------
#Welcome Message, and start prompter
colors = "244;5;5:"
print_figlet("M E D", font = "5lineoblique", justify = "center", width = 130, colors=colors)
print_figlet("L O G G E R", font = "5lineoblique", justify = "center", width = 130, colors=colors)
print_figlet("A S S I S T A N T", font = "5lineoblique", justify = "center", width = 130, colors=colors)

print(colored('Welcome to the SCEMS Med Logger Assistant, type in "start" to start a log' , 'red' , None , None , no_color = False , force_color = True))
CurrentInput = input()

if CurrentInput == "start":

    print("New patient log started")
    PatientPulseCheck()
    PatientRespirationCheck()
    PatientInjuryCheck()
    print("Initial information complete, for further information notation and access please use the commands, type cmds for a list of commands.")
    DuringTreatment = True

else: #command not recognized/start not typed
    print(colored('Command not recognized.' , 'red' , None , None , no_color = False , force_color = True))

while DuringTreatment == True:
    CurrentInput = input()
    #Last Vitals Command, gives most recent set of all vitals taken
    if CurrentInput == "lastvitals" or CurrentInput == "lstvitals" or CurrentInput == "lvt":
       RecentVitalsPrintOut()

    #All Vitals command, gives all vitals color coded
    elif CurrentInput == "allvitals" or CurrentInput == "vitalhistory" or CurrentInput == "hstvitals" or CurrentInput == "hvt":
       FullVitalsPrintOut()
       

    elif CurrentInput == "updatevitals" or CurrentInput == "updvitals" or CurrentInput == "uvt":
       UpdateVitals()

    elif CurrentInput == "updatepulse" or CurrentInput == "updpulse" or CurrentInput == "upl":
       PatientPulseCheck()

    elif CurrentInput == "updaterr" or CurrentInput == "updresp" or CurrentInput == "updrr" or CurrentInput == "updaterespiration" or CurrentInput == "updrespiration" or CurrentInput == "urr":
       PatientRespirationCheck()

    elif CurrentInput == "updatebp" or CurrentInput == "updbp" or CurrentInput == "updatebloodpressure" or CurrentInput == "updbloodpressure" or CurrentInput == "ubp":
       PatientBloodPressureCheck()

    elif CurrentInput == "updatespo2" or CurrentInput == "updateoxygen" or CurrentInput == "updspo2" or CurrentInput == "updoxygen" or CurrentInput == "updoxy" or CurrentInput == "uspo2":
       PatientBloodOxygenCheck()

    elif CurrentInput == "addinjury" or CurrentInput == "addinj" or CurrentInput == "ainj":
        PatientInjuryCheck()

    elif CurrentInput == "updateinjury" or CurrentInput == "updinjury" or CurrentInput == "updinj" or CurrentInput == "uinj":
        UpdateInjuries()

    elif CurrentInput == "removeinjury" or CurrentInput == "rmvinjury" or CurrentInput == "rmvinj" or CurrentInput == "rinj":
        RemoveInjury()

    elif CurrentInput == "viewinjury" or CurrentInput == "vwinjury" or CurrentInput == "vwinj" or CurrentInput == "vinj":
        ViewInjury()

    elif CurrentInput == "addnote" or CurrentInput == "addnt" or CurrentInput == "adnote" or CurrentInput == "ant":
        AddNote()
    
    elif CurrentInput == "removenote" or CurrentInput == "rmvnote" or CurrentInput == "removent" or CurrentInput == "rmvnt" or CurrentInput == "rnt":
        RemoveNote()

    elif CurrentInput == "viewnotes" or CurrentInput == "viewnote" or CurrentInput == "vwnote" or CurrentInput == "vwnotes" or CurrentInput == "viewnt" or CurrentInput == "vnt":
        ViewNotes()

    elif CurrentInput == "addtreatment" or CurrentInput == "addtrm" or CurrentInput == "adtreatment" or CurrentInput == "atrm":
        AddTreatment()

    #elif CurrentInput == "updatetreatment" or CurrentInput == 