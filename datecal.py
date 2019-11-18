import datetime


def date_cal(arg):
    if arg[1] == '-e':
        d = arg[2]
        y = '*'+d+'*'
        return y
    if arg[1] == '-a' or arg[1] == '-c':
        d = arg[2]
        f_date = d.replace("/", " ")
        y, m = f_date.split()
        year = int(y)
        month = int(m)
        # day = int(d)
        x = datetime.datetime(year, month, True)
        return x.strftime('*' + '%Y' + '_' + '%b' + '*')


def file_date(self):
    d = str(self)
    f_date = d.replace("-", " ")
    y, m, d = f_date.split()
    year = int(y)
    month = int(m)
    day = int(d)
    x = datetime.datetime(year, month, day)
    return x.strftime('%B %d')
