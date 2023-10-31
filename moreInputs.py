# again, importing the datetime module 
import datetime

# importing the MonthlyFieldService class and collectYearlyData function from the fieldSvc file
from fieldSvc import MonthlyFieldService, collectYearlyData

# Creating an instance of the MonthlyFieldService class that allows you to use the methods
# and attributes defined within that class
report = MonthlyFieldService()

# printing the header for the Field Service Report
print("\n\tField Service Report")
print("\t--------------------")

# calling the collectYearlyData function to collect and calculate yearly field service data
collectYearlyData()
