#read in csv file
df = pd.read_csv('<filename>')

#Check dtype
df.info()
df.dytpes()


#Import another jupyter notebook
%run '<notebook name>.ipynb'

#List column names
df.columns

#import glob to read in files with certain extensions, prefex or middle by using *
data = glob_glob('*.csv')

#read in several files
df = DataFrame()
for myFile in data:
    all_data = pd.read_csv(myFile, <insert compression type  if necessary>)
    df = df.append(all_data)

#wrap text in jupyte notebook
df_new = df[(df['col1'].isnull()) & (df['col2'].isnull()) /
& (df['col3'].isnull())]

#Unique counts in a columne
len(df['col1'].unique())
