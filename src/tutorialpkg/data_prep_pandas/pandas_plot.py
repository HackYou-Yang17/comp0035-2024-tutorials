import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def print_plots(df):

    # Create a histogram of the DataFrame
    summer_df = df[df['type'] == 'summer']
    winter_df = df[df['type'] == 'winter']

    summer_df.hist()
    winter_df.hist()

   # Show the plot
    plt.show()

if __name__ == '__main__':

    try:
        df_prep = Path(__file__).parent.parent.joinpath('tutorialpkg' ,'data', 'paralympics_events_prepared.csv')

    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

    print_plots(df_prep)