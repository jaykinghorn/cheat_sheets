

---- Working With Data ------

#data cleanup on import -e.g. remove dollar signs or extraneous,
# pass them to df.replace(), specifying each char and it's replacement:
import regex
df[cols] = df[cols].replace({'\$': '', ',': ''}, regex=True)

Open file manually before bringin into pandas
with open('file.csv', 'r') as f:
   ...:     exam_lines = f.readlines()

Rename Columns
df.rename(columns = {'$b':'B'}, inplace = True)

Null Values
#quick way to count the total number of null values
np.count_nonzero(df.isnull())
#can pass a column
np.count_nonzero(df['col1'].isnull())

#fill na with value, in this case, zero
df.fillna(0)
#fill forward or fill backward with adjacent data
df.fillna(method='ffill') #or 'bfill'
df.dropna() #drops missing values
#when performing calculations, skipna=True by default 

#Drops columns based on column index
df.drop(df.columns[1:10], axis = 1, inplace = True)

#view rows with null values
df.loc[pd.isnull(df['col1']),:]

#apply a function to a dataframe, to a column(s) or row(s)
df.apply(my_function, axis=0) #change the axis to axis=1 to apply to a row 
df['col1'] = df.apply(my_function, axis=0)

#merge and join data
new_df = df1.merge(df2, left_on='keycol_fromdf1', right_on='keycol_fromdf2')

----- Slicing and Selecting Data ------
# loc based on row name 
#iloc based on row index (number)
#display the 100th row
print(df.loc[99])
#display multiple rows
print(df.loc[[0,99,999]])

#slicing columns or subsetting columns. note the colon to select all rows within the two columns
subset = df.loc[:,['col1', 'col2']]
#subset or slice columns with iloc, passing numeric values
subset = df.iloc[:, [2,4,-1]]
#or
subset = df.iloc[:,:3]

#to select non-contiguous columns with ranges, 
pd.concat([df[['col1','col2']], df.loc[:,'col4':'col50']], axis=1)
#alternatively, use numpy arange to create a list of columns
initial_col = [0,1]
others = np.arange(3,7).tolist()
columns = initial_col + others
new_df = df.iloc[:,columns]

#subset columns - selects all rows, can pass a row index here as well
df.loc[:, ['col1','col2', 'col_n']

#Select all rows "except" those listed (e.g. selects b,c,d,e,)
df2 = df[df.columns.difference(['col_a', 'col_f','col_g'])]

#conditional selection
#separate attributes are enclosed in their own brackets
df.loc[df.column == 'Value_1']
df.loc[(df.column1 == 'Value_1') & (df.column2 >= 30)]
df.loc[(df.column1 == 'Value_1) | (df.column2 >= 30)]
df.loc[df.column2.isin(['Value_1', 'Value_2'])
df.loc[df.column.notnull()] #or isnull

#split and combine columns
col1_split = df['col1'].str.split('_', expand=True)
col1_split.columns = ['new_col1', 'new_col2']
joined_df = pd.concat([df, col1_split], axis=1)
#alternate way
new_col = df['col_name'].str.split('?',expand=True, n=1)
df_joined = pd.concat([new_col, df], axis=1)

-------Groupby and aggregations -----------
df.groupby('col_for_grouping')['col_for_aggregating'].sum()

#create a muliti-column grouped df that will group by cols 1 and 2 then sum based on 3 and 4
#This will create a multi-index dataframe
df2 = df.groupyb(['col_1','col2'])[['col3','col4']].sum()
#use reset_index to flatten the dataframe and avoid multi-index

#Use aggregation to look at multiple attributes of a second column
newdf = df.groupby('col1').col2.agg([min, max])


#boolean subset of DataFrame
df[df['col1'] > criteria]

#Groupby 
#standard syntax is to specify first the column to group by, then the aggregation function to occur
grouped_df = df.groupby(['col1'])['col2'].sum()
#alternatively, you can simply create a groupby object. This returns a groupby object
grouped = df.groupby('col1')
#to view the groupby Object or to perform calculations 
grouped.groups or grouped.sum() #mean(), #min()

#reshape data from wide to tall. A.k.a "tidy data"
pd.melt(df, id_vars='col_to_keep_unchanged')
#id_vars is a container(list, tuple, ndarray) that represents the variables that will remain as is
#value_vars identifes the columsn you want to melt down, or pivot, By default, pandas will melt
#any columns not specified in the id_vars parameter

#filter data based on a specific criteria. Here it filters on having a minimum of 30 samples.
new_df = df.groupby('col1').filter(lambda x: x['col1'].count() >=30)


#load multiple csv files into single dataframe 
import glob
list_of_filenames = glob.glob('filepath/*.csv')

list_filename_df = []

for csv_filename in list_of_filenames:
	df = pd.read_csv(csv_filename)
	list_filename_df.append(df)

#same for loop in a list comprehension
list_filename_df_comp = [pd.read_csv(data) for data in list_of_filenames]
df_loop_concat_comp = pd.concat(list_filename_df_comp)

#pull filenames and strip the {.csv} from the filename, add names to list
import glob
filenames = []
for name in glob.glob('*.csv'):
    filenames.append(name[:-4])

---- Time-based Calculations ------
#look at pandas strftime for additional functionality, not native to pandas
#datetime has a number of built in attributes
d = pd.to_datetime('2016-02-29')
d.month #year, week, day, weekday_name
#extract a portion of a date for a new column
df['year']= df['Date'].dt.year

#creating new columns based on date attributes
df['closing_quarter'] = (df['Closing Date'].dt.quarter)

#subsetting data by dates - two examples
df.loc[(df.Date.dt.year == 2010) & (df.Date.dt.month ==6)]
df.loc[(df.Date.dt.year >= 2010) & (df.Date.dt.year < 2011)]

#setting the date column to the index gives even more flexibility. Example selects all rows from June, 2010
df.index = df['Date']
df['2010-06'].iloc[:,:]

#resample date frequencies. If you resample to a higher frequency than the data, NaN fills missing values.
new = df.resample('M').sum()

#Converting minutes to seconds (python) - second brackets are needed for python 3
def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

print (get_sec('1:23:45'))

#Time-Date Handling
#Trim Datetime to date only (two parts)
df['Date_col'] = df['Date_col'].dt.date
df['Date_col'] = pd.to_datetime(df['Date_col'])

#TimeZones
#specify timezones and perform conversions using pytz
import pytz
depart=pd.Timestamp('2017-08-29 07:00', tz='US/Eastern')
#creating timedeltas across timezones will create an error unless the timezones are normalized. The example demonstrates a Pacific Arrival time, converted to allow timedelta calculation
duration = arrive.tz_convert('US/Eastern') - depart

#Linear Regression
import statsmodels.formula.api as smf
model = smf.ols(formula='tip~total_bill', data=tips) #the two variables being compared are separated by ~
results = model.fit()
results.summary() 

----- Correlation and Statistical Analysis -------
corr_matrix = df.corr()
corr_matrix['target_column'].sort_values(ascending=False)
#creates a correlation plot then prints the values in descending order for a target column



