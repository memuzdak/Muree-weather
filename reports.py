def whole_year_report(report):
    print("Highest: " + str(report[0]))
    print("Lowest: " + str(report[1]))
    print("Humidity: " + str(report[2]))


def month_avg_report(report):

    print("Highest Average: " + str(report[0]) + 'C')
    print("Lowest Average: " + str(report[1]) + 'C')
    print("Average Mean Humidity: " + str(report[2] + '%'))
