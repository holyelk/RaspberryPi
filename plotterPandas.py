import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def clean_Numbers():
    # Cleaning numbers 
    count=0
    for row in df['Temperature']:
        if (row < 20):
            df.loc[count,'Temperature'] = df.loc[count-1,'Temperature']
        count+=1

def clean_Time():
    # Cleaning Time 
    df['Time'] = df['Time'].str.rsplit(':', 1).str.get(0)


df = pd.read_csv('/home/pi/sensor_readings.csv')
#print(df.dtypes)

clean_Numbers()
clean_Time()

#print(df['Time'])

x = df['Time'].tail(50)
y = df['Temperature'].tail(50)
#x = df['Time']
#y = df['Temperature']

plt.plot(x,y)
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.gcf().autofmt_xdate()
plt.gca().xaxis.set_major_locator(ticker.MaxNLocator(10))
plt.gca().xaxis.set_minor_locator(ticker.MaxNLocator(40))
#plt.gca().xaxis.set_major_formatter(plt.NullFormatter()) 
plt.gca().tick_params(axis='x',length = 8)
plt.tight_layout()
plt.show()
