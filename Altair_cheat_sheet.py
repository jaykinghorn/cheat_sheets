import altair as alt
alt.renderers.enable('notebook')#required for Jupyter notebook

"""
Altair Follows a standard structure of 
alt.Chart(df).mark_*().encode() #*=chart type
Within the basic chart, specify x and y axes based in encode()
mark_bar
mark_point
color='col_x' #column to use for color separations
shape='col_y' #column to use for shape separatons
Additional mark attributes: fill, size, stroke

text= 'col_x' #column to use for text on the point/line
tooltip = 'col_x' #column to use for the tooltip value 
href='col_x' #hyperlink for points


"""

#create a bar chart
alt.Chart(df).mark_bar().encode(
    y='num_events',
    x='borough'
)

#same bar chart with modifications for size, color and properties
alt.Chart(df).mark_bar(size=50, color='firebrick').encode(
    y='num_events',
    x='borough'
).properties(width=600)

#adding .interactive() allows a chart to scale 

#Line Chart with years separated as separate lines
import altair as alt

data = "https://frdata.wikimedia.org/donationdata-vs-day.csv"

alt.Chart(data).mark_line().encode(
    alt.X('monthdate(date):T', axis=alt.Axis(format='%B', title='Month')),
    alt.Y(
        'max(ytdsum):Q', stack=None,
        axis=alt.Axis(title='Cumulative Donations')
    ),
    alt.Color('year(date):O', legend=alt.Legend(title='Year')),
    alt.Order('year(data):O')
)


#Advanced Features 
#Data Transformations
#Altair has built-in data transformations 
alt.Chart.(df).mark_point().encode(
	x='col_a', y='average(col_b)'
	)
	this creates a scatter plot with the average of column b

#Specify the datatype within the plot
alt.Chart(df).mark_point().encode(
	alt.Y('col_a', axis=alt.Axis(title='column name', type='nominal'),
	alt.X('col_b', type='quantitative', aggregate='average')
	#additional encodings = Q: quantitative, O: ordered quantity, N:nominial (unordered),
	#T: temporal