

- Concept of _Event Row Structure_ whereby each row is an event. In the simplest form, each event row contains a sub-activity (the event), a start timestamp and an end timestamp. Additional metadata can be added or removed based on the needs of the analysis. For example, using the start and end timestamps, the duration can be determined (in any temporal units desired). The day and time of day can be determined, the 'phase' of the day can be determined, weekend or weekday ...

- Concept of the _Boolean Array Structure_ whereby each row is a timestamp and the columns of the dataset are the sub activities and values of the cells are boolean to indicate if the sub activity is occuring (1) or is not occuring (0). All metadata associated with the timestamps and then sub activities is stored in separate reference files (e.g. *.csv, *.json).

Basu et al, tackle the problem of energy management via automation & give consideration to user convenience. Their model (using only energy-consuming appliance behaviour) is 
Specifically mention the challenge of building a generalized model... _The problem of appliance usage prediction through con­sumption data is new. [6] deals with the problem of the user behavior prediction in a home automation system using a Bayesian network for a single appliance but a general model for appliance prediction is still lacking._ They also specifically model time as periodic variables, segmenting on hour of day and day of week, noting, 'this way of modelling time takes into account the periodic nature of human behaviour'


## Introduction


Huang et al explore the idea of Service-oriented Computing (SOC) whereby the inherent complexity associated with networking and programming is abstracted away, shifting the focus from dealing with technical details to a focus on how the services are to be used. For example, under this paradigm, a light connected to the Internet is represented as a light service or a heater connected to the internet is represented as a heating service... 'realm of smart home'... A smart home can be considered as any regular home which has been augmented with various types of IoT services, the purpose of which is to make residents' life more convenient and efficient (@article{huang2018} @ 15/17 of @article{huang2018}). <br>

**Discuss IoT**
_The term ‘‘Internet-of-Things’’ is used as an umbrella keyword for covering various aspects related to the extension of the Internet and the Web into the physical realm, by means ofthe widespread deployment of spatially distributed devices with embedded identification,sensing and/or actuation capabilities. Internet-of-Things envisions a future in which digitaland physical entities can be linked, by means of appropriate information and communica-tion technologies, to enable a whole new class of applications and services. In this article,we present a survey of technologies, applications and research challenges for Internet-of-Things_ <br>

[IMAGE - Old Paradigm = user sitting at computer terminal] <br>
[IMAGE - New Paradigm = user surrounded by services] <br>

LINK - more internet users = more value for internet-based tech

Here we observe that the internet is evolving from interconnecting computers to interconnecting things [@article{atzori2010}]. <br>

This explosive expansion of digital technology has 



- Through the evaluation of sensor data from both energy-consuming and energy-dependent activities, a machine model XYZ was developed
- A proposed model for reducing energy-consumption whilst accounting for end-user convenience was devised and theoretically implemented.
- This work aims to bridge the gap between CONVENIENCE and ENERGY USAGE, a previously neglected consideration (these two haven't been directly considered side-by-side, as it were)


```python
Data = ds.drop(columns = 'kitchen_toaster').values   #
target = ds['kitchen_toaster']                       #

D_train, D_test, t_train, t_test = train_test_split(Data, 
                                                    target, 
                                                    test_size = 0.3,
                                                    random_state=999)

dt_classifier = DecisionTreeClassifier(max_depth=4,
                                       criterion='entropy',
                                       random_state = 999)
                                       
dt_classifier.fit(D_train, t_train);
dt_classifier.score(D_test, t_test)

cv_method = RepeatedStratifiedKFold(n_splits = 5, 
                                    n_repeats = 3, 
                                    random_state = 999)

dt_classifier = DecisionTreeClassifier(random_state=999)

params_DT = {'criterion': ['gini', 'entropy'],
             'max_depth': [2, 3, 4, 5]}

gs = GridSearchCV(estimator=dt_classifier, 
                  param_grid=params_DT, 
                  cv=cv_method,
                  verbose=1, 
                  scoring='accuracy')

```

```python
num_features = 5
fs_fit_mutual_info = fs.SelectKBest(fs.mutual_info_classif, k=num_features)
fs_fit_mutual_info.fit_transform(Data, target)
fs_indices_mutual_info = np.argsort(fs_fit_mutual_info.scores_)[::-1][0:num_features]
best_features_mutual_info = ds.columns[fs_indices_mutual_info].values
best_features_mutual_info

feature_importances_mutual_info = fs_fit_mutual_info.scores_[fs_indices_mutual_info]
feature_importances_mutual_info

plot_imp(best_features_mutual_info, feature_importances_mutual_info, 'Mutual Information', 'blue')

```

```r
Error in match.arg(highlight, highlighters()) : 
  'arg' should be one of “default”, “tango”, “pygments”, “kate”, “monochrome”, “espresso”, “zenburn”, “haddock”, “breezedark”

reticulate::use_python("/anaconda3/envs/IoT_ResearchProject/bin/python")

class.source = c("numCode", "R", "numberLines")

https://rpubs.com/AlistairGJ/GunViolenceData
https://rpubs.com/AlistairGJ/skillbuilder7
https://warwick.ac.uk/fac/sci/wdsi/events/vacationschool2016/for-participants/materials/knitr.pdf
https://github.com/rstudio/rticles 
http://jianghao.wang/post/2017-12-08-rmarkdown-templates/ 
https://github.com/ismayc/thesisdown 
https://libscie.github.io/rmarkdown-workshop/handout.html 
https://bookdown.org/ 
https://rstudio.com/wp-content/uploads/2015/03/rmarkdown-reference.pdf 
https://www.rdocumentation.org/packages/rmarkdown/versions/1.16/topics/pdf_document
https://cran.r-project.org/web/packages/citr/citr.pdf </br>
https://bookdown.org/yihui/rmarkdown/pdf-document.html 
https://libscie.github.io/rmarkdown-workshop/handout.html 
https://github.com/ismayc/thesisdown 
https://rpubs.com/onduuuu/python_in_r 
https://bookdown.org/yihui/bookdown/figures.html 
https://yihui.name/knitr/options/ 
https://stackoverflow.com/questions/41030477/changing-chunk-background-color-in-rmarkdown
https://bookdown.org/yihui/rmarkdown/pdf-document.html
https://stackoverflow.com/questions/38861041/knitr-rmarkdown-latex-how-to-cross-reference-figures-and-tables
```
https://yihui.name/knitr/options/


PLOTS - can do
total-population-living-in-extreme-poverty-by-world-region
world-population-1750-2015-and-un-projection-until-2100


As with any new technology, Cloud Computing brings with it both new opportunities and new challenges. 




Borne from the ubiquity of Cloud Computing

---







https://stackoverflow.com/questions/11707586/how-do-i-expand-the-output-display-to-see-more-columns 


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




<iframe id="command-video" src="https://player.vimeo.com/video/345089185?autopause=0&amp;autoplay=1&amp;controls=true&amp;quality=1080p&amp;muted=1" height="475" frameborder="0" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen="" allow="autoplay" data-ready="true"></iframe>

<iframe src="https://player.vimeo.com/video/354994299?loop=1&amp;autopause=0&amp;autoplay=1&amp;quality=1080p&amp;muted=1" height="475" frameborder="0" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen="" allow="autoplay"></iframe>

<iframe id="analyze-video" src="https://player.vimeo.com/video/353492936/?autopause=0&amp;autoplay=1&amp;title=0&amp;quality=1080p&amp;loop=1&amp;muted=1" height="475" frameborder="0" webkitallowfullscreen="" mozallowfullscreen="" allowfullscreen="" allow="autoplay" data-ready="true"></iframe>
