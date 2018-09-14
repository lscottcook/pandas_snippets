#Group-By
df.groupby(['Col1', 'Col2'])

#
df_new = pd.crosstab(df['col1'], df['col2'])

df_new = pd.concat([df_1, df_2])

#merge


#Merging multiple dfs
 df_list = [df_1, df_2, df_3]
df_combine = reduce(lambda x,y: pd.merge(x, y, on='acronym', how='outer'), df_list)


#Renaming
df_rename = df.rename(columns = {'col1':'Column 1', 'col2':'Column 2'})

 result = df1.append([df2, df3])

 #Write to df not using merged cells
 merge_cells=False
 
 
 #Create a dataframe from multiple json files nested key values 
import os 
 
directory_path = '<directory filepath>'
def concat_json_files(directory_path):
    columns = [<list column names>]
    df = pd.DataFrame(columns=columns)
    for json_file in os.listdir(directory_path):
        full_filepath = os.path.join(directory_path, json_file)
        with open(full_filepath) as f:
            data = json.load(f)
            df_file = pd.DataFrame(data['<key for the top level you want to retrieve>'])
            #concat all the df's 
            df = pd.concat([df, df_files])
    return df 

