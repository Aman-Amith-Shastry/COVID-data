import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 7})

df1 = pd.read_html('https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN%3Aen&state=3')[0][1:]
df2 = pd.read_html('https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN%3Aen&state=7')[0][1:]

df = df1.merge(df2, how = 'inner' ,indicator=False)
loc = df['Location']
cases = df['Total cases']
vacs = df['People fully vaccinated']

plt.title('COVID 19 cases per state')
plt.gca().spines['top'].set_visible(False)  
plt.gca().spines['right'].set_visible(False)

plt.ticklabel_format(style='plain') 
plt.plot(loc,cases,label = 'Cases')
plt.plot(loc, vacs,label = 'Vaccination')
plt.xticks(rotation = 90)


plt.legend()
plt.show()
