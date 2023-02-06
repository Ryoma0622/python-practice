import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read the csv file into a dataframe
df = pd.read_csv("data.csv")

# Convert datetime column to datetime type
df["datetime"] = pd.to_datetime(df["datetime"])

# Group the datetime by hour and count the number of access
df = df.groupby(df["datetime"].dt.floor("H")).size().reset_index(name='accessCount')

# # Plot the bar chart
fig, ax = plt.subplots(figsize=(20, 7))
ax.bar(df["datetime"], df["accessCount"], width=0.05)
# Format the x-axis labels to show the date and hour
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H"))
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:00:00"))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=4))
# ax.set_xlim(df['datetime'].min(), df['datetime'].max())
# ax.set_xticks(df['datetime'])
plt.xlabel("Datetime")
plt.ylabel("Access Count")
plt.xticks(rotation=90)
# dates = df['datetime'].dt.date.unique()
firstDatetime = df['datetime'].iloc[0]
lastDatetime = df['datetime'].iloc[-1]
dates = pd.date_range(start=firstDatetime, end=lastDatetime, freq='D')
print(dates)
for i, date in enumerate(dates):
    plt.axvline(date, color='gray', alpha=0.5)
# Add bounding line for a specific date
date = "2023-02-05 02:00:00"
ax.axvline(pd.Timestamp(date), color='red', linestyle='--')

plt.show()
