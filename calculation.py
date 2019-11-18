import csv
from math import floor
from datecal import file_date


class Calculation:

    def __init__(self, file_taker):
        self.file_taker = file_taker

    def whole_year_cal(self):
        max_temperature_f = []
        max_temp_date_f = []
        min_temperature_f = []
        min_temp_date_f = []
        max_humidity_f = []
        max_humidity_date_f = []
        i = 0
        while i < len(self.file_taker):
            with open(self.file_taker[i]) as infile:
                csv.register_dialect('strip', skipinitialspace=True)
                input_file = csv.DictReader(infile, dialect='strip')
                fieldnames = input_file.fieldnames
                # print(fieldnames)
                max_temperature = []
                max_temp_date = []
                min_temperature = []
                min_temp_date = []
                max_humidity = []
                max_humidity_date = []
                for row in input_file:
                    min_temp_value = row["Min TemperatureC"]
                    max_temp_value = row["Max TemperatureC"]
                    max_humidity_value = row["Max Humidity"]
                    date_value = row["PKT"]
                    if min_temp_value and date_value and max_temp_value:
                        min_temperature.append(min_temp_value)
                        max_temperature.append(max_temp_value)
                        max_humidity.append(max_humidity_value)
                        min_temp_date.append(date_value)
                        max_temp_date.append(date_value)
                        max_humidity_date.append(date_value)
                        final_min = min(min_temperature)
                        final_max = max(max_temperature)
                        final_max_humidity = max(max_humidity)
                        min_index = min_temperature.index(final_min)
                        max_index = max_temperature.index(final_max)
                        max_humidity_index = max_humidity.index(final_max_humidity)
                max_temperature_f.append(int(final_max))
                max_temp_date_f.append(max_temp_date[max_index])
                min_temperature_f.append(int(final_min))
                min_temp_date_f.append(min_temp_date[min_index])
                max_humidity_f.append(int(final_max_humidity))
                max_humidity_date_f.append(max_humidity_date[max_humidity_index])
            i = i + 1
        i_max = max_temperature_f.index(max(max_temperature_f))
        max_report = str(max(max_temperature_f)) + 'C on ' + str(file_date(max_temp_date_f[i_max]))
        i_min = min_temperature_f.index(min(min_temperature_f))
        min_report = str(min(min_temperature_f)) + 'C on ' + str(file_date(min_temp_date_f[i_min]))
        ih_max = max_humidity_f.index(max(max_humidity_f))
        maxh_report = str(max(max_humidity_f)) + '% on ' + str(file_date(max_humidity_date_f[ih_max]))
        return max_report, min_report, maxh_report


class CalculationAvg:

    def __init__(self, file_taker):
        self.file_taker = file_taker

    def cal_month_avg(self):
        with open(self.file_taker[0]) as infile:
            csv.register_dialect('strip', skipinitialspace=True)
            input_file = csv.DictReader(infile, dialect='strip')
            fieldnames = input_file.fieldnames
            max_temperature_avg = []
            max_temp_date_avg = []
            min_temperature_avg = []
            min_temp_date_avg = []
            mean_humidity_avg = []
            mean_humidity_date_avg = []
            for row in input_file:
                min_temp_value_avg = row["Min TemperatureC"]
                max_temp_value_avg = row["Max TemperatureC"]
                mean_humidity_value_avg = row["Mean Humidity"]
                date_value = row["PKT"]
                if min_temp_value_avg and date_value and max_temp_value_avg:
                    min_temperature_avg.append(int(min_temp_value_avg))
                    max_temperature_avg.append(int(max_temp_value_avg))
                    mean_humidity_avg.append(int(mean_humidity_value_avg))
                    min_temp_date_avg.append(date_value)
                    max_temp_date_avg.append(date_value)
                    mean_humidity_date_avg.append(date_value)
                    final_min_avg = sum(min_temperature_avg) / len(min_temperature_avg)
                    final_max_avg = sum(max_temperature_avg) / len(max_temperature_avg)
                    final_mean_humidity_avg = sum(mean_humidity_avg) / len(mean_humidity_avg)
            return str(floor(final_max_avg)), str(floor(final_min_avg)), str(floor(final_mean_humidity_avg))


class Stars:

    def __init__(self, file_taker):
        self.file_taker = file_taker

    def star_fun(self):
        with open(self.file_taker[0]) as infile:
            csv.register_dialect('strip', skipinitialspace=True)
            input_file = csv.DictReader(infile, dialect='strip')
            max_temperature = []
            min_temperature = []
            i = 1
            for row in input_file:
                min_temp_value = row["Min TemperatureC"]
                max_temp_value = row["Max TemperatureC"]
                if min_temp_value and max_temp_value:
                    max_temperature.append(max_temp_value)
                    max_t = int(max_temperature[0])
                    print(i, '\033[1;30;40m' + max_t * '+', max_t, '\033[0m')
                    max_temperature.pop()
                    min_temperature.append(min_temp_value)
                    min_t = int(min_temperature[0])
                    print(i, '\033[94m' + min_t * '+', min_t, '\033[0m')
                    min_temperature.pop(0)
                i += 1


class Bonus:

    def __init__(self, file_taker):
        self.file_taker = file_taker

    def bonus_star_fun(self):
        with open(self.file_taker[0]) as infile:
            csv.register_dialect('strip', skipinitialspace=True)
            input_file = csv.DictReader(infile, dialect='strip')
            max_temperature = []
            min_temperature = []
            i = 1
            for row in input_file:
                min_temp_value = row["Min TemperatureC"]
                max_temp_value = row["Max TemperatureC"]
                if min_temp_value and max_temp_value:
                    max_temperature.append(max_temp_value)
                    min_temperature.append(min_temp_value)
                    max_t = int(max_temperature[0])
                    min_t = int(min_temperature[0])
                    print(i, '\033[1;30;40m' + min_t * '-' + max_t * '+', min_t, '\033[94m' + '-', max_t, '\033[0m')
                    max_temperature.pop()
                    min_temperature.pop()
                i += 1

