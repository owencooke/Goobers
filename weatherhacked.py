import matplotlib.pyplot as plt
import pandas
from meteostat import Stations, Daily
import math

# Get coordinates for location from user
lat, lon = map(float, input('Please input coordinates of desired location (latitude longitude): ').split())

# Get weather stations close to coordiates, ordered by distance
stations = Stations(lat, lon)

# Get closest station as a Pandas dataframe containing station metadata (not weather)
station = stations.fetch(1)

# Get weather data from start-end date
start, end = map(str, input('Please input start/end dates for weather analysis, space-separated. Format: YYYY-MM-DD (start end): ').split())
data = Daily(station, start, end)
data = data.fetch()  # Pandas dataframe for weather data
#print(data)

# Get average temperature for each day as a list
tavg = data[data.columns[0]]
tavglist = tavg.to_numpy()
#print(tavglist[0])
sections = math.floor(len(tavglist)/365)
print(sections)
each_year = []
copy_tavglist = tavglist
yearmarker = []
for i in range(0, sections):
	each_year.append(copy_tavglist[(365*i):(365*(i+1))])
	yearmarker.append(365*i)

medians = []
for i in range(0, len(each_year)):
	medians.append(sum(each_year[i]) / 365)

print(each_year[7], each_year[8])
print("Medians ", medians)
print("Yearkmarker", yearmarker)

days = list(range(0, len(tavglist)))
plt.plot(days, tavglist, label='Average Daily Temperature (°C)')
plt.plot(yearmarker, medians, label='Median Temperature Each Year')
plt.ylabel('Temperature (°C)')
plt.xlabel('Days')
plt.legend()
plt.title('Daily Temperatures - Latitude: ' + str(lat) + ' Longitude: ' + str(lon))
plt.show()
