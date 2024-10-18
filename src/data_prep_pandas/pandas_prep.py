import pandas as pd
import pathlib
 
pd.set_option("display.max_columns", None)


def print_dataframe_data(dataframe):
        """Summary or Description of the Function
    
           Parameters:
           argument1 (int): Description of arg1
    
           Returns:
           int:Returning value
    
        """

        print("\nData types of the start/end columns after conversion:")
        print(dataframe.loc[:, ['start', 'end']].dtypes)

        print(dataframe.loc[:, ['start', 'end']])


def data_preparation(dataframe):
    """Summary or Description of the Function
    
           Parameters:
           argument1 (int): Description of arg1
    
           Returns:
           int:Returning value
    
        """
    
    dataframe['start'] = pd.to_datetime(dataframe['start'], format = '%d/%m/%Y')
    dataframe['end'] = pd.to_datetime(dataframe['end'], format = '%d/%m/%Y')
    
    try:
        columns_to_change= ['countries', 'events', 'participants_m', 'participants_f', 'participants']

        for x in columns_to_change:
            dataframe[x] = dataframe[x].astype('int')
    except ValueError as e:
        print(f"Error, can't convert column {dataframe[x].name} to int: {e}")


if __name__ == '__main__':

    try:
        csvPath = pathlib.Path(__file__).parent.parent.joinpath('tutorialpkg' ,'data', 'paralympics_events_raw.csv')
        xlsxPath = pathlib.Path(__file__).parent.parent.joinpath('tutorialpkg' ,'data', 'paralympics_all_raw.xlsx')
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

    csvDf = pd.read_csv(csvPath)
    xlsxDf1 = pd.read_excel(xlsxPath)
    xlsxDf2 = pd.read_excel(xlsxPath, sheet_name = "medal_standings")

    data_preparation(xlsxDf1)
    print_dataframe_data(xlsxDf1)

    print("\nDone")
    