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

        print (dataframe)
        #print("\nData types of the start/end columns after conversion:")
        #print(dataframe.loc[:, ['start', 'end']].dtypes)

        #print(dataframe.loc[:, ['start', 'end']])


def data_preparation(df1, df2):
    """Summary or Description of the Function
    
           Parameters:
           argument1 (int): Description of arg1
    
           Returns:
           int:Returning value
    
        """
    
    df1['start'] = pd.to_datetime(df1['start'], format = '%d/%m/%Y')
    df1['end'] = pd.to_datetime(df1['end'], format = '%d/%m/%Y')
    
    '''
    try:
        columns_to_change= ['countries', 'events', 'participants_m', 'participants_f', 'participants']

        for x in columns_to_change:
            df1[x] = df1[x].astype('int')
    except ValueError as e:
        print(f"Error, can't convert column {df1[x].name} to int: {e}") 
    '''

    return df1.merge(df2, how='left', left_on='country', right_on='Name')

    

if __name__ == '__main__':

    try:
        csvPath = pathlib.Path(__file__).parent.parent.joinpath('tutorialpkg' ,'data', 'paralympics_events_raw.csv')
        xlsxPath = pathlib.Path(__file__).parent.parent.joinpath('tutorialpkg' ,'data', 'paralympics_all_raw.xlsx')
        npcPath = pathlib.Path(__file__).parent.parent.joinpath('tutorialpkg' ,'data', 'npc_codes.csv')
    except FileNotFoundError as e:
        print(f"File not found. Please check the file path. Error: {e}")

    csvDf = pd.read_csv(csvPath)
    xlsxDf1 = pd.read_excel(xlsxPath)
    xlsxDf2 = pd.read_excel(xlsxPath, sheet_name = "medal_standings")
    npcDf = pd.read_csv(npcPath, encoding='utf-8', encoding_errors='ignore', usecols=['Code', 'Name'])
    
    mergedDf = data_preparation(csvDf, npcDf)
    print_dataframe_data(mergedDf)

    print("\nDone")
    