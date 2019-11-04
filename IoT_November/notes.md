

- Concept of _Event Row Structure_ whereby each row is an event. In the simplest form, each event row contains a sub-activity (the event), a start timestamp and an end timestamp. Additional metadata can be added or removed based on the needs of the analysis. For example, using the start and end timestamps, the duration can be determined (in any temporal units desired). The day and time of day can be determined, the 'phase' of the day can be determined, weekend or weekday ...

- Concept of the _Boolean Array Structure_ whereby each row is a timestamp and the columns of the dataset are the sub activities and values of the cells are boolean to indicate if the sub activity is occuring (1) or is not occuring (0). All metadata associated with the timestamps and then sub activities is stored in separate reference files (e.g. *.csv, *.json).

Basu et al, tackle the problem of energy management via automation & give consideration to user convenience. Their model (using only energy-consuming appliance behaviour) is 
Specifically mention the challenge of building a generalized model... _The problem of appliance usage prediction through con­sumption data is new. [6] deals with the problem of the user behavior prediction in a home automation system using a Bayesian network for a single appliance but a general model for appliance prediction is still lacking._ They also specifically model time as periodic variables, segmenting on hour of day and day of week, noting, 'this way of modelling time takes into account the periodic nature of human behaviour'












https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns 


<iframe id="command-video" src="https://player.vimeo.com/video/345089185?autopause=0&amp;autoplay=1&amp;controls=true&amp;quality=1080p&amp;muted=1" height="475" frameborder="0" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen="" allow="autoplay" data-ready="true"></iframe>

<iframe src="https://player.vimeo.com/video/354994299?loop=1&amp;autopause=0&amp;autoplay=1&amp;quality=1080p&amp;muted=1" height="475" frameborder="0" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen="" allow="autoplay"></iframe>

<iframe id="analyze-video" src="https://player.vimeo.com/video/353492936/?autopause=0&amp;autoplay=1&amp;title=0&amp;quality=1080p&amp;loop=1&amp;muted=1" height="475" frameborder="0" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen="" allow="autoplay" data-ready="true"></iframe>

Add Header to ggplots

from IPython.display import IFrame
IFrame(src='1WeekdayMorning.html', width=1200, height=600)

from IPython.core.display import display, HTML
HTML('1WeekdayMorning.html')

Image(filename = PATH + 'images/floorPlan.png', width=1000, height=1000)

ADD KEY + MENTION S1

<center>
<div w3-include-html="1WeekdayMorning.html"></div>
</center> 
<i> This text is italic. </i> <br>
Fig 1. DESCRIBE

<iframe src='1WeekdayMorning.html', width=700, height=600></iframe>

http://127.0.0.1:8888/notebooks/Documents/GitHub/IoT_ResearchProject/00.%20A%20Phase%201.ipynb 


ds = ds[ds.subAct != 'bedroom_jewelrybox']
ds = ds[ds.subAct != 'foyer_closet']
ds = ds[ds.subAct != 'kitchen_cereal']
ds = ds[ds.subAct != 'kitchen_containers']
ds = ds[ds.subAct != 'bedroom_lamp']


https://github.com/AlistairGJ/IoT_ResearchProject/blob/October/00.%20A%20Phase%201.ipynb 
https://nbviewer.jupyter.org/github/AlistairGJ/IoT_ResearchProject/blob/053b88f41a0e62e6b8c5365416b8e373ab8a28ba/00.%20A%20Phase%201.ipynb#Abstract  


import gc
gc.collect() 

from IPython import get_ipython;   
get_ipython().magic('reset -sf') 

%run -i Packages.py
%matplotlib inline