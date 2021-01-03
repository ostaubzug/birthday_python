#birthday reminder project


#suche nach betimmmten Namen soll auch möglich sein
#Liste abändern falls etwas nicht mehr stimmt am Anfang eine Art menü wo man auswählen kann was man machen will
#musik player der so klassische musik hat

#evt öffnet das python skript einfach den groove musikplayer , auf einen Ordner mit klassischer musik verlinkt? Mit Flutter kann ich diese app dann nochmals viel besser bauen.

#DIE DATENBANK FUNKTIONIERT NICHT RICHTIG ES LÖSCHT IMMER DEN nAMEN IRGENDWIE ZU NAN   OHH MANNN WTF
#bei mehrfachem adden speichtert er immer nur die letzte Eingabe ?!?!




import datetime
import pandas as pd


def startup():

    try:
        #open csv and import as dataframe
        df = pd.read_csv('birthdaycsv.csv',index_col = [0])
        print("found database")
    except:   
        #if there is no csv create one
        df = pd.DataFrame()
        df.to_csv('birthdaycsv.csv')
        print("created new database")
        
    return df

def dateinput():
   try:
       name = input("type in the name surname, name: ")
       day = int (input("type in the day (no zero if single digit) : "))
       month = int(input("type in the month (no zero if single digit) : "))
       year = int(input("type in the year he/she was born (if unknown: 1): "))
       comment = input ("type in any comments: ")       
       birthdate = datetime.date(year, month, day)

       print("name: ", name ,"\nbirthday: ", birthdate,  "\ncomments: ", comment ,"\nis the following info correct ? [Y/N] ")
       x = input("\n")

       if x  == "Y" or x == "y":
           print("if triggered")
           safe(name,birthdate,comment)
      
       else:

           print("try again")
           dateinput()

   except:
       print("except triggered")
       print("try again")
       dateinput()
       


       
       
       
def safe(name,birthdate,comment):
    df = startup()
    new_row = [[name,birthdate,comment]]
    df2 = pd.DataFrame(new_row, columns=["Name", "Birthdate", "Comments"])
    df3 = df.append(df2, ignore_index=True)
    df3.to_csv('birthdaycsv.csv',index = False)   
    print("saved to csv")
 
 
 
 
def menue():
    menueinput = input("Type 'add' to add a new person, 'edit' to edit, 'search' to search 'print' to print df and 'music' to play music \n")
    if menueinput == "add":
            dateinput()
            menue()
            
    elif menueinput == "edit":
            print("error")
            menue()
    
    elif menueinput == "search":
        print("error")
        menue()
            
    elif menueinput == "music":
            print("error")
            menue()
            
    elif menueinput == "print":
        df = startup()
        print(df)      
        menue()
    else:
        print("oops something went wrong")
        menue()





menue()
