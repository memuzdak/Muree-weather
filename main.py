from datecal import date_cal
import sys
import read_data
from reports import whole_year_report, month_avg_report
from calculation import Calculation, CalculationAvg, Stars, Bonus


def main():
    arg = sys.argv
    date = date_cal(arg)
    obj = read_data.Files(date)
    o = obj.fetch_file_year()
    x = 1
    while x < len(sys.argv):
        if sys.argv[x] == '-e':
            cal_whole_year = Calculation(o)
            rep = cal_whole_year.whole_year_cal()
            whole_year_report(rep)
        if sys.argv[x] == '-a':
            cal_avg_month = CalculationAvg(o)
            rep = cal_avg_month.cal_month_avg()
            month_avg_report(rep)
        if sys.argv[x] == '-c':
            cal_bar_chart = Stars(o)
            cal_bar_chart.star_fun()
        # if sys.argv[x] == '-c':
        #     cal_bonus = Bonus(o)
        #     cal_bonus.bonus_star_fun()
        x += 2


if __name__ == '__main__':
    main()


