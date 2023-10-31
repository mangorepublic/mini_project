# import the datetime module for working with times
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
        # this approach provides a standardized unit of measurement for time duration.
        timeDifference = (endTime - startTime).total_seconds()
        return timeDifference / 3600
    
    # a method to collect data from the user for a single month
    def collectingData(self):
        decide = "yes"
        while decide.lower() == "yes":
            # loop to handle input validation and and collection of data to handle the various attributes
            while True:
                try:
                    # get start time from user input in HH:MM format and convert it to datetime object
                    startTime = datetime.datetime.strptime(input("Enter start time (HH:MM): "), "%H:%M")
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

            # asking the user if they want to print more data for this month
            decide =input("\nDo you want to enter more data for this month? (yes/no): ")
            if decide.lower() != "yes":
                break       

    #  a method to display monthly totals
    def displayTotals(self):
        print("\n\tMonthly Totals")
        print(f"Total Placement given out: {self.totalPlacements}")
        print(f"Total Hours spent in field service: {self.totalHours:.2f} hours")
        print(f"Total Videos shown: {self.totalVideos}")
        print(f"Total Return Visits: {self.totalReturnVisit}")
        print(f"Total Bible Studies conducted: {self.totalBibleStudies}")

# a function to collect data for all twelve months and calculate yearly totals
def collectYearlyData():
    yearlyTotals = MonthlyFieldService()
    decide = "yes"
    while decide.lower() == "yes":  
    
        # list of month names
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

        # Iterate through months
        for month in range(1, 13):
            # Months are represented by integers from 1 to 12
            print(f"\n-Data Entry for {months[month - 1]}")  # month - 1 to access month names list
            monthlyService = MonthlyFieldService()
            monthlyService.collectingData()

            yearlyTotals.totalPlacements += monthlyService.totalPlacements
            yearlyTotals.totalHours += monthlyService.totalHours
            yearlyTotals.totalVideos += monthlyService.totalVideos
            yearlyTotals.totalReturnVisit += monthlyService.totalReturnVisit
            yearlyTotals.totalBibleStudies += monthlyService.totalBibleStudies

            # Display monthly totals after entering data for the month
            monthlyService.displayTotals()

            # asking the user if they want to input more data for this year
            decide = input("\nDo you want to enter more data for this year? (yes/no): ")
            if decide != "yes":
                break
        
        # diplaying yearly totals
        print("\n\tYearly Totals")
        print(f"Total Placement given out: {yearlyTotals.totalPlacements}")
        print(f"Total Hours spent in field service: {yearlyTotals.totalHours:.2f} hours")
        print(f"Total Videos shown: {yearlyTotals.totalVideos}")
        print(f"Total Return Visits: {yearlyTotals.totalReturnVisit}")
        print(f"Total Bible Studies conducted: {yearlyTotals.totalBibleStudies}")
