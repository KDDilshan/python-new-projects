# the funtios of the alarm
alrm_funtions={
    1:"Set alarm",
    2:"View alarms",
    3:"Delete alarms",
    4:"Exit"
}

# the list used to store the alrm times user input
alarms=[]
# use to confrem the user input alrm in 24H format
def conferm_alarm(alarm_hour,alarm_minites):
    if alarm_hour in range(0,24) and alarm_minites in range(0,60):
        alarm_time=(f"{alarm_hour:02d}:{alarm_minites:02d}")
        alarms.append(alarm_time)
    else:
        print("enter itms in vaid range😤")
    print("\n")
# use to show the alarm funtios
def showing():
    print("//Alarm///")
    for i in alrm_funtions:
        print(f"{i}.{alrm_funtions[i]}")
    print("\n")
# set alarm time of user
def set_time():
    print("Enter time in 24 hour format⏰")
    alarm_hour=int(input("hours(0-23): "))
    alarm_minites=int(input("Minutes(0-59): "))
    conferm_alarm(alarm_hour,alarm_minites)
# view thw alarm time enetr by user
def view():
    # cheak whether the programme is empty
    if not bool(alarms):
        print("set the time first")
    else:
        print("Alarms")
        for i in range(len(alarms)):
            print(f"{i+1} . {alarms[i]}")
        print("\n")
# delete alrm time enterd by user
def delete():
    delete_alarm=input("what alarm you want to delete😒: ")
    if delete_alarm in alarms:
        alarms.remove(delete_alarm)
        
    else:
        print("first set the time⏰")
    print("\n")

while True:
    showing()
    # cheak the user only input the integer values for valid feilds
    try:
        #cheak the alrm option that user want to input
        alarm_option=int(input("what opertion you want to do 🕰️: "))
        if alarm_option in alrm_funtions:
            if alarm_option==1:
                set_time()
            if alarm_option==2:
                view()
            if alarm_option==3:
                delete()
            if alarm_option==4:
                # wheather user input is simple or captial the funtion works
                Exit_programme=input("Do you want to exit(Y/N): ").strip().upper()
                if Exit_programme=="Y":
                    break
                elif Exit_programme!="N":
                    print("enter valid commonds only")
        else:
            print("Enter the values in valid range❌\n")
    except ValueError:
        print("Enter integer values only❌\n")
            
       
