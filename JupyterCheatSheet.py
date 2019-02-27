iPython Widgets

import ipywidgets as widgets
from ipywidgets import interactive
from IPython.display import display

#Provide a dropdown list of options and assign this to a variable for later use
from IPython.display import display
list = ['LA', 'NY', 'BOS', 'SF']
btn= widgets.Dropdown(options = list)
display(btn, list) #OMIT LIST IF YOU ONLY WANT THE BUTTON TO SHOW 
test = btn.value
print(test)