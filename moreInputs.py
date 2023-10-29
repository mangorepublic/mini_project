import datetime
from fieldSvc import MonthlyFieldService

report = MonthlyFieldService()

report.collectingData()

while True:
    moreEntries = input("\nDo you want to enter more data? (yes/no): ").lower()
    if moreEntries == "no":
        break
    elif moreEntries == "yes":
        while True:
            try:
                startTime = datetime.datetime.strptime(input("\nEnter start time (HH:MM): "), "%H:%M")
                break
            except ValueError:
                print("Invalid input! Please enter a valid time in HH:MM format.")
        
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
        
        while True:
            try: 
                endTime = datetime.datetime.strptime(input("Enter end time (HH:MM): "), "%H:%M")
                break
            except ValueError:
                print("Invalid input! Please enter a valid time in HH:MM format.")

        hoursSpent = report.hoursCalculation(startTime, endTime)

        report.totalPlacements += placements
        report.totalHours += hoursSpent
        report.totalVideos += videos
        report.totalReturnVisit += returnVisit
        report.totalBibleStudies += bibleStudies

        print(f"Hours spent in field service: {hoursSpent:.2f} hours")

    else:
        print("Invalid input! Please enter 'yes' or 'no'.")

report.displayTotals()
