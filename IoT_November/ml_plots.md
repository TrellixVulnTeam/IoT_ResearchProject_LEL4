---
title: "subActPlots"
author: "AlistairGJ"
date: "14/11/2019"
output: html_document
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(message = FALSE, warning = FALSE)
library(ggplot2)
library(ggridges)
library(dplyr)
library(viridis)
library(lubridate)
library(ggExtra)
library(tidyr)
library(readr)
library(cowplot)
library(data.table)
library(ggsci)
```

dsPRE <- read_csv('/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/intermediate_datasets/S1SubActivities_preprocessedWfeatures.csv', 
http://www.sthda.com/english/wiki/ggplot2-barplots-quick-start-guide-r-software-and-data-visualization 
https://haozhu233.github.io/kableExtra/awesome_table_in_pdf.pdf 
http://www.stat.columbia.edu/~tzheng/files/Rcolor.pdf
https://cran.r-project.org/web/packages/kableExtra/vignettes/awesome_table_in_html.html 
https://daattali.com/shiny/colourInput/ 

```{r}
feat <- read_csv('/Users/alistairgj/kitchen_refrigerator_best_feats.csv')
dt <- read_csv('/Users/alistairgj/kitchen_refrigerator_dt.csv')
roc <- read_csv('/Users/alistairgj/kitchen_refrigerator_roc.csv')
```

```{r}
f <- ggplot(feat, aes(reorder(feature, score), score)) + geom_bar(stat="identity")
f <- f + coord_flip() + theme_gray()
f <- f + labs(x = "Feature", y = "Score") +
  theme(text = element_text(size=8), 
        legend.title = element_blank(),
        axis.title.y=element_blank(),
        legend.position = c(0.9,0.12),
        legend.background = element_rect(fill=alpha('white', 0.5)),
        legend.key.size = unit(5, "mm"))
f
```


```{r}
d <- ggplot(dt, aes(max_depth, test_score, group = criterion, color = criterion))
d <- d + geom_line(size=0.5) + geom_point(size = 0.5) + scale_colour_startrek() + theme_grey()
d <- d + labs(x = "Depth", y = "Score") +
  theme(text = element_text(size=8), 
        legend.title = element_blank(),
        legend.position = c(0.8,0.15),
        legend.background = element_rect(fill=alpha('white', 0.5)),
        legend.key.size = unit(5, "mm"))
d
```


```{r}
r <- ggplot(roc, aes(fpr, tpr))
r <- r + geom_line(size=0.5, colour="dodgerblue2") + geom_point(size = 0.5, colour="dodgerblue2") + theme_grey()
r <- r + labs(x = "False Positive Rate", y = "True Positive Rate (Recall)") + 
  scale_y_continuous(limits=c(0,1), expand = c(0, 0.01)) +
  scale_x_continuous(limits=c(0,1), expand = c(0, 0.01)) +
  theme(text = element_text(size=8), 
        legend.title = element_blank(),
        legend.position = c(0.9,0.12),
        legend.background = element_rect(fill=alpha('white', 0.5)),
        legend.key.size = unit(5, "mm"))
r <- r + geom_segment(aes(x = 0, y = 0, xend = 1, yend = 1, fill = "black"))
r
```






```{r fig.width=10, fig.height=2.75}
plot <- plot_grid(f, d, r, labels = "AUTO", label_size = 8, nrow = 1,  rel_widths = c(1, 1, 1))
plot
ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/MLtest.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 4.5, units = c("cm"), dpi = 300)
```


```{r fig.width=10, fig.height=2}
subActNum = unique(dsPRE$subActNum)

strip_plot <- function(ds, i) {
  ds_filtered <- ds %>% filter(subActNum == i)
  d <- ggplot(ds_filtered, aes(durationSec, DAY))
  d <- d + geom_bin2d() + scale_y_discrete(limits=c('Sun', 'Sat', 'Fri', 'Thu', 'Wed', 'Tue', 'Mon')) +
    scale_x_continuous(expand = c(0.025, 0.025)) +
    scale_fill_viridis(breaks = function(x) unique(floor(pretty(seq(0, (max(x) + 1) * 1.1)))), direction = - 1) +
    theme_grey() +
    theme(legend.position = "none", axis.title.y=element_blank(), text = element_text(size=7),
          axis.text.x = element_text(size = 6, angle = 0)) + 
    labs(x = "Duration (Seconds)")

  e <- ggplot(ds_filtered, aes(HOUR, DAY))
  e <- e + geom_bin2d() + 
    scale_y_discrete(limits=c('Sun', 'Sat', 'Fri', 'Thu', 'Wed', 'Tue', 'Mon')) +
    scale_x_discrete(limits=c('4','5','6','7','8','9','10','11','12','13','14','15',
                              '16','17','18','19','20','21','22','23','0','1'), 
                     breaks=c('4', '5', '6','7','8','9','10','11','12','13','14','15',
                              '16','17','18','19','20','21','22','23','0','1'), expand = c(0.025, 0.025)) +
    scale_fill_viridis(breaks = function(x) unique(floor(pretty(seq(0, (max(x) + 1) * 1.1)))), direction = - 1) +
    theme_grey() +
    theme(legend.position = "right", axis.title.y=element_blank(), 
          text = element_text(size=7),
          axis.text.x = element_text(size = 6, angle = 0),
          legend.key.size = unit(1,"line")) + labs(x = "Hour of Day")
  
  f <- ggplot(ds_filtered, aes(x = DAY, y = durationSec, fill = DAY))
  f <- f + geom_boxplot() + coord_flip() +
    scale_x_discrete(limits=c('Sun', 'Sat', 'Fri', 'Thu', 'Wed', 'Tue', 'Mon')) +
    scale_y_continuous(expand = c(0.025, 0.025)) +
    theme_grey() +
    theme(legend.position = "none", axis.title.y=element_blank(), text = element_text(size=7),
          axis.text.x = element_text(size = 6, angle = 0)) + 
    labs(x = NULL, y = "Duration (Seconds)")

  plot_row = plot_grid(f, d, e, labels = "AUTO", label_size = 6, nrow = 1,  rel_widths = c(1, 1, 1.2))
  plot_grid(plot_row, ncol = 1, rel_heights = c(0.1, 1))
  
}
```

```{r fig.width=10, fig.height=4}
#p1 <- strip_plot(dsPRE, 139) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
#p2 <- strip_plot(dsPOST, 139) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
#plot_grid(p1, p2,
#  nrow = 2,
#  label_size = 8,
#  align = "v"
#)
```









#### Bathroom Lightswitch (SubActNum 101)

```{r fig.width=10, fig.height=2}
strip_plot(dsPRE, 101) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct101.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```


#### Bathroom Medicine Cabinet (SubActNum 57)

```{r fig.width=10, fig.height=4}
p1 <- strip_plot(dsPRE, 57) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
p2 <- strip_plot(dsPOST, 57) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
plot_grid(p1, p2,
  nrow = 2,
  label_size = 8,
  align = "v"
)

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct57.png", 
			plot = last_plot(), device = png(), 
      scale = 1.5, width = 18, height = 6, units = c("cm"), dpi = 300)
```



#### Study Drawer (SubActNum 82)

```{r fig.width=10, fig.height=4}
p1 <- strip_plot(dsPRE, 82) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
p2 <- strip_plot(dsPOST, 82) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
plot_grid(p1, p2,
  nrow = 2,
  label_size = 8,
  align = "v"
)

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct82.png", 
			plot = last_plot(), device = png(), 
      scale = 1.5, width = 18, height = 6, units = c("cm"), dpi = 300)
```


#### Kitchen Refrigerator (SubActNum 126)

```r
strip_plot(dsPRE, 126) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct126.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```





