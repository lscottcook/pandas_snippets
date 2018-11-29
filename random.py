#inclusive of the right exclusive on the left

#triple quotes for strings expands multiple lines


#Transpose
df.T

#Filtering by something in
df[[for x in  x df.column where 'a' in x ]]


#Tag duplicates find the number of instances
df['dupicate tag '] = df.groupby('col 1').cumcount() + 1


#Filter by what is not contained in another DataFrame
df_3 = df_1[(~df_1['col 1']).isin(df_2['col 2'])]


#Wrap jn
\

#hide Pandas warnings in jupyter notebook 
import warnings
warnings.filterwarnings('ignore')


# Add 'upstream' repo to list of remotes
git remote add upstream <link for original repo>

# Fetch from upstream remote
git fetch upstream
git checkout master
git merge upstream/master

# Widen diplay output of df in jupyter notebook  
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)


#finding path for user 
(os.path.expanduser('~'))



"""function for creating an Excel Workbook with multiple dataframes each on a separate worksheet then upload to S3. User is either on
a windows machine or the script is running form Jenkins 
filename = the name of the Excel file without .xlsx
args = the name of the dataframes
"""
sys.path.insert(0, os.path.abspath('.'))
user = (os.path.expanduser('~'))

#get filepath for the user
def get_filepath(user):
    #for windows 
    if  'User' in user:
        filepath = user + '/<insert folder name>/'
    #for linux     
    elif 'jenkins' in user:
        filepath = '/tmp/%s'

    return filepath

user_filepath = get_filepath(user)

def upload_s3(filename,*args):
    s3resource = boto3.resource('s3')
    bucket = s3resource.Bucket('<insert s3 bucket name>')
    filename = '{}_{}.xlsx'.format(
        filename,pd.datetime.today().strftime(
            '%m%d%y'),engine='xlsxwriter',options={'remove_timezone':True})
    filepath = user_filepath + filename
    workbook = pd.ExcelWriter(filepath, engine='xlsxwriter')
    #create a worksheet for each df passed into the function
    for n,df in enumerate(args):
        df.to_excel(workbook,'sheet%s' % str(n + 1),index=False)
    workbook.save()
    #path on S3 to upload
    basepath = '<insert filepath on S3 without the bucket name> /%s'
    bucket.upload_file(filepath, (basepath % filename), ExtraArgs={'ServerSideEncryption' : 'AES256'})
    os.remove(filepath)
    #optional print statement 
    print 'Finished uploading file <insert file path>' + filename
    
    """
    Example of calling the function:
    df_report = upload_s3('Annual_Report', df_1, df_2') 
    """
        
        
##############        
#Pass in commandline arguements into function 
import sys, os
import argparse
sys.path.insert(0, os.path.abspath('.'))

parser = argparse.ArgumentParser(description='You can add a ')

parser.add_argument('-n','--name', help='users name',required=True)
args = parser.parse_args()

#create a function 
def get_specific_ptn(dataframe,args):
    first_name = args.name
    hello = "Hi " + first_name
    return hello 

#run script 
python welcome_user.py -n Lisa 
############## 


############## 
"""create parse df to create multiple excel workbooks. For example if you have a df containing information
for multiple employees and and need to create individual reports to distribute to each employee"""
def get_individual_reports(df_all_employees):
    names = df_all_employees['employee_name'].unique()
    for name in names:
        df_individual = df_all_employees[df_all_employees['employee_name']==name]
        individual_wb = ExcelWriter('{}_Employee_Report_{}.xlsx'.format(name,pd.datetime.today().strftime('%m%d%y')))
        df_inividual.to_excel(individual_qb, 'Employee Results', index=False )
    return individual_wb 




