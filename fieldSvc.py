# import the datetime module foe working with times
import datetime

# defining a class named MonthlyFieldService
class MonthlyFieldService:

    # intializing the total counts set to zero
    def __init__(self):
        self.totalPlacements = 0
        self.totalHours = 0
        self.totalVideos = 0
        self.totalReturnVisit = 0
        self.totalBibleStudies = 0
    
    # method for calculating hours spent, takes startTime and endTime as parameters
    def hoursCalculation(self, startTime, endTime):
        # calculating the time difference in seconds and converting it to hours
        timeDifference = (endTime - startTime).total_seconds()
        return timeDifference / 3600
    
    # a method to collect data from the user
    def collectingData(self):
        # loop to handle input validation and and collection of data to handle the various attributes
        while True:
            try:
                # get start time from user input in HH:MM format and convert it to datetime object
                startTime = datetime.datetime.strptime(input("\nEnter start time (HH:MM): "), "%H:%M")
                break
            except ValueError:
                print("Invalid input! Please enter a valid time in HH:MM format.")

        # similar loops for collecting other attributes: placements, videos, return visits, and bible studies
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
        hoursSpent = self.hoursCalculation(startTime, endTime)

        # updating the total counts with the data collected
        self.totalPlacements += placements
        self.totalHours += hoursSpent
        self.totalVideos += videos
        self.totalReturnVisit += returnVisit
        self.totalBibleStudies += bibleStudies

        # printing hours spent in field service
        print(f"Hours spent in field service: {hoursSpent:.2f} hours")

    #  a method to display monthly totals
    def displayTotals(self):
        print("\nMonthly Totals")
        print(f"Total Placement given out: {self.totalPlacements}")
        print(f"Total Hours spent in field service: {self.totalHours:.2f} hours")
        print(f"Total Videos shown: {self.totalVideos}")
        print(f"Total Return Visits: {self.totalReturnVisit}")
        print(f"Total Bible Studies conducted: {self.totalBibleStudies}")
