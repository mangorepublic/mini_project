import datetime

class MonthlyFieldService:

    def __init__(self):
        self.totalPlacements = 0
        self.totalHours = 0
        self.totalVideos = 0
        self.totalReturnVisit = 0
        self.totalBibleStudies = 0
    
    def hoursCalculation(self, startTime, endTime):
        timeDifference = (endTime - startTime).total_seconds()
        return timeDifference / 3600
    
    def collectingData(self):
        try:
            startTime = datetime.datetime.strptime(input("\nEnter start time (HH:MM): "), "%H:%M")
            placements = int(input("Enter number of placements: "))
            videos = int(input("Enter number of videos shown: "))
            returnVisit = int(input("Enter number of return visit: "))
            bibleStudies = int(input("Enter the number of bible studies conducted: "))
            endTime = datetime.datetime.strptime(input("Enter end time (HH:MM): "), "%H:%M")
            hoursSpent = self.hoursCalculation(startTime, endTime)

            self.totalPlacements += placements
            self.totalHours += hoursSpent
            self.totalVideos += videos
            self.totalReturnVisit += returnVisit
            self.totalBibleStudies += bibleStudies

            print(f"Hours spent in field service: {hoursSpent:.2f} hours")

            while True:
                moreEntries = input("\nDo you want to enter more data? (yes/no): ").lower()
                if moreEntries != "yes":
                    break
                else:
                    startTime = datetime.datetime.strptime(input("\nEnter start time (HH:MM): "), "%H:%M")
                    placements = int(input("Enter number of placements: "))
                    videos = int(input("Enter number of videos shown: "))
                    returnVisit = int(input("Enter number of return visit: "))
                    bibleStudies = int(input("Enter the number of bible studies conducted: "))
                    endTime = datetime.datetime.strptime(input("Enter end time (HH:MM): "), "%H:%M")
                    hoursSpent = self.hoursCalculation(startTime, endTime)

                    self.totalPlacements += placements
                    self.totalHours += hoursSpent
                    self.totalVideos += videos
                    self.totalReturnVisit += returnVisit
                    self.totalBibleStudies += bibleStudies

                    print(f"Hours spent in field service: {hoursSpent:.2f} hours")

        except ValueError:
            print("Invalid input! Kindly enter valid numbers.")

    def displayTotals(self):
        print("\nMonthly Totals")
        print(f"Total Placement given out: {self.totalPlacements}")
        print(f"Total Hours spent in field service: {self.totalHours:.2f} hours")
        print(f"Total Videos shown: {self.totalVideos}")
        print(f"Total Return Visits: {self.totalReturnVisit}")
        print(f"Total Bible Studies conducted: {self.totalBibleStudies}")


report = MonthlyFieldService()
report.collectingData()
report.displayTotals()