import time
import webbrowser
type_break=input("Enter the type for break in format of  'M' for minutes and 'H' for hours : ")
breaks=int(input("Enter the no of breaks : "))
time_breaks=int(input("Enter no of minutes or hours after the break : "))
URL_link=input("Enter the youtube link : ")

for i in range(breaks):

    if type_break.lower()=='m':
        time.sleep(time_breaks*60) 
        webbrowser.open(URL_link,new=2)
        print("The link is opened...........")
    else: 
        time.sleep(time_breaks*60*60)
        webbrowser.open(URL_link,new=2)
        print("The link is opened...........")