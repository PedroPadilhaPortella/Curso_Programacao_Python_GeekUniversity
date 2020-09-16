import datetime

d1 = datetime.datetime(2014,7,16,23)
d2 = datetime.datetime.now()

diff = d2 - d1

days = diff.days
years, days = days // 365, days % 365
months, days = days // 30, days % 30

seconds = diff.seconds
hours, seconds = seconds // 3600, seconds % 3600
minutes, seconds = seconds // 60, seconds % 60

print("Desde {} passaram {} anos, {} meses, {} dias, {} horas, {} minutos e {} segundos".format(d1, years, months, days, hours, minutes, seconds))