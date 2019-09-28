# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
#Code starts here

#Load DataSet in DataFrame
data = pd.read_csv(path, sep = ',', delimiter=None)

#Rename Total Column
data.rename(columns={"Total":"Total_Medals"}, inplace=True)

print(data.head(10))


# --------------
#Code starts here


conditions = [data['Total_Summer'] > data['Total_Winter'], data['Total_Summer'] < data['Total_Winter'], data['Total_Summer'] == data['Total_Winter']]
choices = ["Summer", "Winter", "Both"]

data['Better_Event'] = np.select(conditions, choices, default=np.nan)
#print(data.head(10))

better_event_count=data['Better_Event'].value_counts()
better_event = "Summer"



# --------------
#Code starts here
#top_10_summer = data.nlargest(11, ['Total_Summer'])
#print(top_10_summer.index.values[0])
#top_10_summer.drop([top_10_summer.index[0]], axis=0, inplace=True)
#top_10_winter = data.nlargest(11, ['Total_Winter'])
#top_10_winter.drop([top_10_winter.index[0]], axis=0, inplace=True)
#top_10_all = data.nlargest(11, ['Total_Medals'])
#top_10_all.drop([top_10_all.index[0]], axis=0, inplace=True)
#pre_merge = pd.merge(top_10_summer, top_10_all, how='inner', on=['Country_Name'])
#final_merge = pd.merge(pre_merge, top_10_winter, how='inner', on=['Country_Name'])
#print(final_merge['Country_Name'])
#summ_winter_ins = top_summer.Country_Name.isin(top_winter.Country_Name)

top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries = top_countries[:-1]

def top_ten(tc, Col):
    country_list = list((tc.nlargest(10, Col)['Country_Name']))
    return country_list
    
top_10_summer = top_ten(top_countries, 'Total_Summer')
top_10_winter = top_ten(top_countries, 'Total_Winter')
top_10 = top_ten(top_countries, 'Total_Medals')
#print(top_10_summer)
#print(top_10_winter)
#print(top_10)
summer_set = set(top_10_summer)
winter_set = set(top_10_winter)
all_set = set(top_10)

common = list(summer_set & winter_set & all_set)
print(common)




# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
#summer_df.plot(x="Country_Name", y="Total_Summer", kind="bar", grid=True)
#winter_df.plot(x="Country_Name", y="Total_Winter", kind="bar", grid=True)
#top_df.plot(x="Country_Name", y="Total_Medals", kind="bar", grid=True)

fig = plt.figure(figsize=(15,5))
fig.suptitle("Top 10 Winners from each Olympic Event", color="b", fontsize=12)
ax1 = fig.add_subplot(131)
ax1.set_ylabel("Medals Tally")
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)
summer_df.plot(x="Country_Name", y="Total_Summer", kind="bar", ax=ax1, grid=True, legend=False)
winter_df.plot(x="Country_Name", y="Total_Winter", kind="bar", ax=ax2, grid=True, legend=False)
top_df.plot(x="Country_Name", y="Total_Medals", kind="bar", ax=ax3, grid=True, legend=False)
ax1.set_title("Summer Olympic", color="m")
ax2.set_title("Winter Olympic", color="r")
ax3.set_title("Both Events", color="g")


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = (summer_df.loc[summer_df['Golden_Ratio'].idxmax()])['Country_Name']

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = (winter_df.loc[winter_df['Golden_Ratio'].idxmax()])['Country_Name']

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = (top_df.loc[top_df['Golden_Ratio'].idxmax()])['Country_Name']




# --------------
#Code starts here
data_1 = data[:-1]

data_1['Total_Points'] = (data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1)
most_points = data_1['Total_Points'].max()
print(most_points)
best_country = (data_1.loc[data_1['Total_Points'].idxmax()])['Country_Name']
print(best_country)

#top_country_gold = (top_df.loc[top_df['Golden_Ratio'].idxmax()])['Country_Name']


# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot(kind="bar", stacked=True, figsize=(8,8))
plt.xlabel("United States")
plt.ylabel("Medals Tally")
plt.xticks(rotation=45)




