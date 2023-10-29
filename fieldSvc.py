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

        hoursSpent = self.hoursCalculation(startTime, endTime)

        self.totalPlacements += placements
        self.totalHours += hoursSpent
        self.totalVideos += videos
        self.totalReturnVisit += returnVisit
        self.totalBibleStudies += bibleStudies

        print(f"Hours spent in field service: {hoursSpent:.2f} hours")

    def displayTotals(self):
        print("\nMonthly Totals")
        print(f"Total Placement given out: {self.totalPlacements}")
        print(f"Total Hours spent in field service: {self.totalHours:.2f} hours")
        print(f"Total Videos shown: {self.totalVideos}")
        print(f"Total Return Visits: {self.totalReturnVisit}")
        print(f"Total Bible Studies conducted: {self.totalBibleStudies}")
