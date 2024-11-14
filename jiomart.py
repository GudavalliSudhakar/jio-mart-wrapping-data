# -*- coding: utf-8 -*-
"""JioMart.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Gwxy0A3EwA8mt1usTslwhwgw-vga3BtL

#Importing Needed Data
"""

# Loading required libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

"""#Identification of URL"""

# Identify the URL

URL = 'https://www.jiomart.com/c/groceries/2'

"""#Loading the WebPage in Memory using requests library"""

page = requests.get(URL)

"""## Check the Status Code of the Page

"""

page.status_code

htmlCode = page.text
soup = BeautifulSoup(htmlCode)

"""## Extracting the HTML Code of the WebPage

#Checking HTML Code
"""

htmlCode

"""#Wrapping Needed Data"""

#Wrapping Single name

name = soup.find('div', attrs={'class' : 'plp-card-details-name line-clamp jm-body-xs jm-fc-primary-grey-80'})
print(name.text)
name = name.text
x = name.strip()
print(x)

#Wrapping all Names

res_names = []
names = soup.find_all('div', attrs={'class' : 'plp-card-details-name line-clamp jm-body-xs jm-fc-primary-grey-80'})
for i in names:
    x = i.text
    x = x.strip()
    res_names.append(x)
print(res_names)
print(len(res_names))

# Wrapping single prices

price = soup.find('span', attrs={'class' : 'jm-heading-xxs jm-mb-xxs'})
print(price.text)
price = price.text
x = price.strip()
print(x)

#Wrapping all Prices

res_prices = []
prices = soup.find_all('span', attrs={'class' : 'jm-heading-xxs jm-mb-xxs'})
for i in prices:
    x = i.text
    x = x.strip()
    res_prices.append(x)
print(res_prices)
print(len(res_prices))

#Wrapping Details

details = soup.find('div', attrs={'class' : 'plp-card-details-container'})
print(details)
print(details.text)
name = details.text
x = name.strip()
print(x)
main = x.split("    ")
print(main)
main[1] = main[1].split("  ")
print(main)
main[2] = main[2].strip()
print(main)

#Wrapping all details
res_details = []
details = soup.find_all('div', attrs={'class' : 'plp-card-details-container'})
for i in details:
  x = i.text
  x = x.strip()
  res_details.append(x)
main = []
for details in res_details:
  k = details.split("    ")
  if len(k) == 3:
    main.append(k)
print(main)
for i in main:
  i[1] = i[1].split("  ")
  i[2] = i[2].strip()
print(main)
names = []
discounted_price = []
actual_price = []
discount_percent = []
for i in main:
  names.append(i[0])
  discounted_price.append(i[1][0])
  actual_price.append(i[1][1])
  discount_percent.append(i[2])
print(names)
print(len(names))
print(discounted_price)
print(len(discounted_price))
print(actual_price)
print(len(actual_price))
print(discount_percent)
print(len(discount_percent))
final_discounted_prices = []
final_actual_prices = []
for i in discounted_price:
  i = i.replace("₹","")
  i = i.replace(",","")
  final_discounted_prices.append(i)
for i in actual_price:
  i = i.replace("₹","")
  i = i.replace(",","")
  final_actual_prices.append(i)
print(names)
print(final_discounted_prices)
print(final_actual_prices)
print(discount_percent)

"""#Applying Pandas"""

df = pd.DataFrame({'Product' : names , 'Discounted Price': final_discounted_prices , 'Actual Price' : final_actual_prices , 'Discount Percent' : discount_percent})
df
df['Discounted Price'] = df['Discounted Price'].astype(float)
df['Actual Price'] = df['Actual Price'].astype(float)
df

"""#Applying Matplotlib"""

plt.hist(df['Discounted Price'], bins = 2, color='purple', alpha=0.7)
plt.title('Histogram - Price Variation')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()

plt.pie(df['Discounted Price'], labels=df['Product'], autopct = '%1.2f%%', startangle = 90)
plt.axis('equal')
plt.show()