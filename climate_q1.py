# SQLlite Import
import sqlite3

# Connect to Climate Database #
connect = sqlite3.connect('climate.db')
cursor = connect.cursor()

#Confirm Table Name
cursor.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
res = cursor.fetchall()
print(res)

#Query Database #
cursor.execute("""SELECT Year, CO2, Temperature FROM ClimateData;""")
res = cursor.fetchall()
connect.close()

#Create Lists #
years = []
co2 = []
temp = []

#Populate Lists #
for r in res:
    years.append(r[0])
    co2.append(r[1])
    temp.append(r[2])

#Test Populated Lists
print( 'Years',years)
print('co2',co2)
print('Temp', temp)

#Matplot Import
import matplotlib.pyplot as plt

#Plot Data
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
plt.savefig("co2_temp_1.png")
