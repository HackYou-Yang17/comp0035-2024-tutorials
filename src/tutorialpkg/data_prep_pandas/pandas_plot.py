import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def create_hist_plots(df):

    # Create a histogram of the DataFrame
    summer_df = df[df['type'] == 'summer']
    winter_df = df[df['type'] == 'winter']

    summer_df.hist()
    winter_df.hist()

   # Show the plot
    plt.show()

def create_box_plots(df):

    df.boxplot(subplots=True, sharey=False)

    plt.show()


if __name__ == '__main__':

    try:
        df_prep = Path(__file__).parent.parent.joinpath('tutorialpkg' ,'data', 'paralympics_events_prepared.csv')

    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

    df_prep

    create_hist_plots(df_prep)
    create_box_plots(df_prep)