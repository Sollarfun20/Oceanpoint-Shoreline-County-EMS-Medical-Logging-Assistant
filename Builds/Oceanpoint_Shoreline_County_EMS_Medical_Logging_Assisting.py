#Medical Logging Assistant Software

#Program designed to make medical logging easier at EMS scenes


#Import Modules
from re import L
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
    CurrentInput = input('Please enter the patient\'s injuries one at a time seperated by different instances of enter, type "end".')
    PatientInjuriesList.append(CurrentInput)
    while CurrentInput != "end":
        CurrentInput = input('Please enter the patient\'s injuries one at a time seperated by different instances of enter, type "end".')
        if CurrentInput != "end":
            PatientInjuriesList.append(CurrentInput)



#Note: Even though StringHolder has a value before hitting the functions, for some reason when it gets called in the functions it resets to none
def PrintBlue():
    global StringHolder
    print(colored(StringHolder, 'blue' , None , None , no_color = False , force_color = True))
    print(StringHolder)

def PrintPurple():
    global StringHolder
    print(colored(StringHolder, 'magenta' , None , None , no_color = False , force_color = True))
    print(StringHolder)

def PrintRed():
    global StringHolder
    print(colored(StringHolder, 'red' , None , None , no_color = False , force_color = True))
    print(StringHolder)

def PrintOrange():
    global StringHolder
    print(colored(StringHolder, 'cyan' , None , None , no_color = False , force_color = True))
    print(StringHolder)

def PrintYellow():
    global StringHolder
    print(colored(StringHolder, 'yellow' , None , None , no_color = False , force_color = True))
    print(StringHolder)

def PrintGreen():
    global StringHolder
    print(colored(StringHolder, 'green' , None , None , no_color = False , force_color = True))
    print(StringHolder)

def PulseColorCode():
      if PatientPulseList[index] > 100:
            PrintPurple()
      elif 0 < PatientPulseList[index] < 60:
            PrintRed()
      elif 0 == PatientPulseList[index]:
            PrintBlue()
      elif 60 <= PatientPulseList[index] <= 70:
            PrintYellow()
      elif 90 <= PatientPulseList[index] < 100:
            PrintYellow()
      else:
            PrintGreen()


def RespirationColorCode():
      #Color code the respiration rate of the patent
        if PatientRespirationList[index] > 20:
             PrintPurple()
        elif 0 < PatientRespirationList[index] < 12:
             PrintRed()
        elif 0 == PatientRespirationList[index]:
             PrintBlue()
        elif 12 <= PatientRespirationList[index] <= 14:
            PrintYellow()
        elif 18 <= PatientRespirationList[index] <= 20:
            PrintYellow()
        else:
            PrintGreen()

def BloodPressureColorCode():
 #Color code the blood pressure of the patient
        if PatientSystolicBloodPressureList[index] != 120 or PatientDiastolicBloodPressureList[index] != 80:
            PrintYellow()
        else:
            PrintGreen()
       

def BloodOxygenColorCode(): 
  #Color code SPo2 level of patient
        if PatientBloodOxygenLevelList[index] <= 10:
             PrintBlue()
        elif PatientBloodOxygenLevelList[index] <= 80:
             PrintRed()
        elif PatientBloodOxygenLevelList[index] <= 90:
             PrintOrange()
        elif PatientBloodOxygenLevelList[index] < 96:
             PrintYellow()
        else:
             PrintGreen() 

def RecentVitalsPrintOut():
    index = -1

    StringHolder = PatientPulseList[index]
    PulseColorCode()

    StringHolder = PatientRespirationList[index]
    RespirationColorCode()

    SystolicBloodPressure = str(PatientSystolicBloodPressureList[index])
    DiastolicBloodPressure = str(PatientDiastolicBloodPressureList[index])
    StringHolder = SystolicBloodPressure + "/" + DiastolicBloodPressure
    BloodPressureColorCode()

    StringHolder = PatientBloodOxygenLevelList[index]
    BloodOxygenColorCode()
   
    

def FullVitalsPrintOut():
    index = 0
    for items in PatientPulseList:
        global StringHolder
        StringHolder = str(PatientPulseList[index]) + " -> "
        print(StringHolder)
        PulseColorCode()

        StringHolder = str(PatientRespirationList[index]) + " -> "
        print(StringHolder)
        RespirationColorCode()

        SystolicBloodPressure = str(PatientSystolicBloodPressureList[index])
        print(SystolicBloodPressure)
        DiastolicBloodPressure = str(PatientDiastolicBloodPressureList[index])
        print(DiastolicBloodPressure)
        StringHolder = SystolicBloodPressure + "/" + DiastolicBloodPressure + " -> "
        print(StringHolder)
        BloodPressureColorCode()

        StringHolder = PatientBloodOxygenLevelList[index]
        print(StringHolder)
        BloodOxygenColorCode()

        index = index + 1


def UpdateVitals():
    PatientPulseCheck
    PatientRespirationCheck
    PatientBloodPressureCheck
    PatientBloodOxygenCheck






#def UpdatePulse():



#def UpdateInjuries():
   # index=0
   # for items in PatientInjuriesList:
   #     ListCounter = index +1
  #      print(ListCounter + ". " + PatientInjuriesList[index])
  #      index = index + 1
  #  CurrentInput = input("Please select a number of whic")








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
       StrinngHolder = 1+1

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

    #elif CurrentInput == "addinjury" or "addinj" or 