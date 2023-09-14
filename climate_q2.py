#Pandas Import
import pandas as pd

#Read CSV file
df = pd.read_csv('climate.csv')

#Dataset details check
df.info()

# Assign data
years = df['Year']
co2 = df['CO2']
temp = df['Temperature']

# TEST
print('Years', years)
print('CO2', co2)
print('Temp', temp)

#Matplot Import
import matplotlib.pyplot as plt

#plot data
plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

