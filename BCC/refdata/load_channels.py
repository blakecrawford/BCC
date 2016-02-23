import csv
#import models

with open('Channel.csv', 'rb') as csv_file:
    channel_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
    for row in channel_reader:
        #new_chan = models.Channel()
        for col in row:
            print col
