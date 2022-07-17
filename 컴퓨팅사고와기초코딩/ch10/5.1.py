import datetime as dt

times = dt.datetime.now()
todays = times.date()
num1 = 5
num2 = 1000
outfile = open('sample.txt', 'a')
outfile.write(str(todays) + ' ' + str(num1) + ' ' + str(num2) + '\n')
outfile.close()
infile = open('sample.txt', 'r')
lines = infile.read()
print(lines)
infile.close()
