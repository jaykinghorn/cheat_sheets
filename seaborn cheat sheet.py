import seaborn as sns


#Plotting with Seaborn
#Additional commands that can be added to below
hue = 'col3'
markers = ['o', 'x']
scatter_kws ={'s': tips['col4']*10} #Adjusts size based on column values

#Histogram
sns.barplot

#scatterplot with a regression line
ax = sns.regplot(x='col1', ='col2', data=df)
ax.set_title('Insert Your Title Here')
ax.set_xlabel('Add X Label')
ax.set_ylabel('Add Y Label')
#optional set fit_reg=False to only show scatterplot
#Tip: add hue='col3' as a means of addressing multivariate data

#jointplot shows scatterplot and histograms with pearson r value
sns.jointplot(x='col1', y='col2', data=df)

#hexbin is used when there are too many points for a scatterplot. It clusters
#points together into hexes. Also shows pearson r value and histograms
sns.jointplot(x='col1', y='col2', data=df, kind='hex')

#boxplot, voilin plot = similar structure to above
sns.boxplot, sns.violinplot 
#adding hue='col3' can be helpful for multivariate data

#rotate labels on x axis for legibility
g = sns.barplot(data=df, x='Park', y='annual_change', color='cyan')
g.set_xticklabels(g.get_xticklabels(), rotation=30)

#change figure size
#be sure to import matplotlib.pyplot as plt
plt.subplots(figsize=(10,15))
sns.scatterplot(x='X', y='Y', data=df)

Year over year comparison
http://atedstone.github.io/pandas-plot-seasons-time-series/