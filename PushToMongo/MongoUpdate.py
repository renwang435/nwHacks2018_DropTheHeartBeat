import serial
import time as t
import pymongo
import datetime
from scipy import signal
from scipy import fftpack
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

uri = 'mongodb://chickenlittle:butter@ds255797.mlab.com:55797/population_db'

serial_port = '/dev/cu.usbmodem1421'

ser = serial.Serial(serial_port, 9600, timeout=0)

count = 0

count1 = 0

time_delay = 0.10

client = pymongo.MongoClient(uri)

db = client.get_default_database()

data = db['individual_db']

local_data = [8.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 6.0, 8.0, 7.0, 7.0, 7.0, 7.0, 5.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 6.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 6.0, 7.0, 7.0, 7.0, 7.0, 8.0, 8.0, 9.0, 10.0, 9.0, 8.0, 9.0, 10.0, 9.0, 9.0, 10.0, 9.0, 9.0]

local_time = []

logic = [0,0]

logic1 = [0,0]

frequency = 0

frequency1 = 0

heart_rate = 0

breathing_rate = 0

discrete_data = 0

label = 1.0

while count < 1000:
    temp_string = ser.readline().rstrip()

    # print(float(temp_string))

    if temp_string:

        time = datetime.datetime.now()

        discrete_data = float(temp_string)

        local_data.append(discrete_data)

        if len(local_data) > 25:
            local_data.remove(local_data[0])

        X = fftpack.fft(local_data)
        freqs = fftpack.fftfreq(len(local_data)) * 25
        # freqs = [100,90]

        # print(freqs)
        count += 1
        count1 += 1

        heart_rate = max(freqs)*6 + 12 * np.random.rand()

        breathing_rate = (max(freqs)*6 + 12 * np.random.rand())/4

        oxygen_saturation = float(temp_string)/10 * 3.7

        if heart_rate > 110 or heart_rate < 60 or oxygen_saturation < 95 :
            label = 2.0
        elif heart_rate > 120 or heart_rate < 50 or oxygen_saturation < 90 or oxygen_saturation > 120:
            label = 3.0
        else:
            label = 1.0

        query = {'datetime': datetime.datetime.now(), 'data': float(temp_string), 'heart_rate': max(freqs)*6 + 12 * np.random.rand(),'breathing_rate': (max(freqs)*6 + 12 * np.random.rand())/4, 'oxygen_saturation': float(temp_string)/5.4, 'X_Pos' : 49.280882 + 0.002086 * np.random.rand(), 'Y_Pos' : -123.117113 + 0.008719 * np.random.rand(), 'label': label}
        print(discrete_data, heart_rate, oxygen_saturation, label)
        data.insert(query)

        t.sleep(time_delay)

# db.drop_collection('iot_spo2')


client.close

print(local_data)