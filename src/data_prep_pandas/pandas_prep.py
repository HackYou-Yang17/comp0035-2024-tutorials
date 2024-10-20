import pandas as pd
import pathlib

# Complete 2.08, and 2.09

replacement_names = {
        'UK': 'Great Britain',
        'USA': 'United States of America',
        'Korea': 'Republic of Korea',
        'Russia': 'Russian Federation',
        'China': "People's Republic of China"
    }

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

    df1["country"] = df1["country"].replace(to_replace=replacement_names)

    merged_df = df1.merge(df2, how='left', left_on='country', right_on='Name')
    df_dropped = merged_df.drop(columns=['URL', 'disabilities_included', 'highlights', 'Name'], axis=1)

    df_dropped = df_dropped.drop(index=0)
    df_dropped = df_dropped.drop(index=17)
    df_dropped = df_dropped.drop(index=31)

    df_prepped = df_dropped.reset_index(drop=True)

    missing_rows = df_prepped[df_prepped.isna().any(axis=1)]

    '''
    try:
        columns_to_change= ['countries', 'events', 'participants_m', 'participants_f', 'participants']

        for x in columns_to_change:
            df1[x] = df1[x].astype('int')
    except ValueError as e:
        print(f"Error, can't convert column {df1[x].name} to int: {e}") 
    '''

    return missing_rows, df_prepped


if __name__ == '__main__':

    pd.set_option("display.max_columns", None)

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
    
    missing_rows_list, df_prepped = data_preparation(csvDf, npcDf)
    print_dataframe_data(missing_rows_list)
    #print_dataframe_data(df_prepped)

    print("\nDone")
    