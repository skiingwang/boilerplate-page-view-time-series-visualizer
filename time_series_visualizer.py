import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df.index = df['date']

df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(12, 6))
    plt.title('#2')
    plt.xlabel('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.ylabel('Page Views')
    plt.plot(df['date'], df['value'], marker='o', linestyle='-')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = (df.groupby(['year', 'month'])['value'].mean().reset_index())
    df_bar['month'] = a['month'].apply(lambda x: f'{x:02d}')
    labels = [f'{year}-{month}' for year, month in zip(a['year'], a['month'])]

    # Draw bar plot
    fig = plt.figure(figsize=(40, 10), facecolor='lightgrey')
    plt.bar(x=labels, height=a['value'])
    plt.title('Months', fontsize=18)
    plt.legend(['month'], fontsize=16, loc='upper left')
    plt.xlabel('Years', fontsize=16)
    plt.ylabel('Average Page Views', fontsize=16)
    fig.savefig('bar_plot.png')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    ax1 = sns.boxplot(x="year", y="value", data=df, ax=axes[0] ,palette="Set3")
    ax1.set_title("Year-wise Box Plot(Trend)")
    ax1.set_xlabel("Year")
    ax1.set_ylabel("Value")

    ax2 = sns.boxplot(x="month", y="value", data=df, ax=axes[1],palette="Set2")
    ax2.set_title("Month-wise Box Plot (Seasonality)")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Value")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
