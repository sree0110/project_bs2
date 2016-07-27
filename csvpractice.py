import csv

f = open("test.csv", 'w+')
try:
    writer = csv.writer(f) #initialising CSV module
    writer.writerow(('INPUT_NO', 'SQUARE_OF_NO', 'CUBE_OF_NO'))
    for no in range(1,11):
        writer.writerow( (no, no*no, no*no*no))
finally:
    f.close()
    
