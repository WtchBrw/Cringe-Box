import csv
import requests
import os
import shutil
import time

time.sleep(10)

chunk_size = 256

def pirate(source, name):
    r = requests.get(source, stream=True)
    cname = (name + '.mkv')
    with open(cname, 'wb') as f:
        for chunk in r.iter_content(chunk_size = chunk_size):
            f.write(chunk)

with open('pirate_this.csv') as file:
    reader = csv.reader(file)

    for row in reader:
        try:
            folder = row[2]
            path = (str(folder))
            if os.path.exists(path) == False:
                os.mkdir(path)

                source = row[0]
                name = row[1]
                pirate(source, name)

                waifu = ((name + '.mkv'))
                shutil.move(waifu, path)
                print('finished')
            else:
                source = row[0]
                name = row[1]
                pirate(source, name)

                waifu = ((name + '.mkv'))
                shutil.move(waifu, path)
                print('finished')
        except:
            pass
