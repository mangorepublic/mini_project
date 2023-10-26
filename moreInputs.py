
import datetime

from fieldSvc import MonthlyFieldService

report = MonthlyFieldService()

report.collectingData()

while True:
    moreEntries = input("\nDo you want to enter more data? (yes/no): ").lower()
    if moreEntries == "no":
        break
    elif moreEntries == "yes":
        startTime = datetime.datetime.strptime(input("\nEnter start time (HH:MM): "), "%H:%M")
        placements = int(input("Enter number of placements: "))
        videos = int(input("Enter number of videos shown: "))
        returnVisit = int(input("Enter number of return visit: "))
        bibleStudies = int(input("Enter the number of bible studies conducted: "))
        endTime = datetime.datetime.strptime(input("Enter end time (HH:MM): "), "%H:%M")
        hoursSpent = report.hoursCalculation(startTime, endTime)

        report.totalPlacements += placements
        report.totalHours += hoursSpent
        report.totalVideos += videos
        report.totalReturnVisit += returnVisit
        report.totalBibleStudies += bibleStudies

        print(f"Hours spent in field service: {hoursSpent:.2f} hours")

report.displayTotals()
