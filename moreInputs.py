# again, importing the datetime module 
import datetime

# importing the MonthlyFieldService class from the fieldSvc file
from fieldSvc import MonthlyFieldService

# Creating an instance of the MonthlyFieldService class allows you to use the methods and attributes defined within that class
report = MonthlyFieldService()

# collecting data from the first entry
report.collectingData()

# loop to allow the user the enter more data
while True:
    moreEntries = input("\nDo you want to enter more data? (yes/no): ").lower()

    # if the user enters "no", exit the loop
    if moreEntries == "no":
        break

    # if the user enters "yes", collect more data for the next entry
    elif moreEntries == "yes":
        while True:
            try:
                # get start time from user input in HH:MM format and convert it to datetime object
                startTime = datetime.datetime.strptime(input("\nEnter start time (HH:MM): "), "%H:%M")
                break
            except ValueError:
                print("Invalid input! Please enter a valid time in HH:MM format.")
        
        # # similar loops for collecting other attributes: placements, videos, return visits, and bible studies
        while True:
            try:
                placements = int(input("Enter number of placements: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer for placements.")
        
        while True:
            try:
                videos = int(input("Enter number of videos shown: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer for videos.")
        
        while True:
            try:
                returnVisit = int(input("Enter number of return visit: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer for return visits.")
        
        while True:
            try:
                bibleStudies = int(input("Enter the number of bible studies conducted: "))
                break
            except ValueError:
                print("Invalid input! Please enter a valid integer for bible studies conducted")
        
        # get end time from user input in HH:MM format and convert it to datetime object
        while True:
            try: 
                endTime = datetime.datetime.strptime(input("Enter end time (HH:MM): "), "%H:%M")
                break
            except ValueError:
                print("Invalid input! Please enter a valid time in HH:MM format.")

        # calculating hours spent using the hoursCalculation method
        hoursSpent = report.hoursCalculation(startTime, endTime)

        # updating the total counts with the data collected
        report.totalPlacements += placements
        report.totalHours += hoursSpent
        report.totalVideos += videos
        report.totalReturnVisit += returnVisit
        report.totalBibleStudies += bibleStudies

        # printing hours spent in field service
        print(f"Hours spent in field service: {hoursSpent:.2f} hours")

    # if the enters neither "yes" nor "no", display an error message
    else:
        print("Invalid input! Please enter 'yes' or 'no'.")

# displaying the monthly totals after collecting all the data
report.displayTotals()
