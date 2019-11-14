
#### Foyer Door (SubActNum 140)

```{r fig.width=10, fig.height=2}
strip_plot(dsPRE, 140) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct140.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Kitchen Freezer (SubActNum 137)

```{r subAct137, echo=FALSE, fig.cap="A caption", out.width = '100%'}
p1 <- strip_plot(dsPRE, 137) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
p2 <- strip_plot(dsPOST, 137) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
plot_grid(p1, p2,
  nrow = 2,
  label_size = 8,
  align = "v"
)

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct137.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Kitchen Burner (SubActNum 106)

```{r subAct106, echo=FALSE, fig.cap="A caption", out.width = '100%'}
strip_plot(dsPRE, 106) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct106.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Kitchen Lightswitch (SubActNum 105)

```{r subAct105, echo=FALSE, fig.cap="A caption", out.width = '100%'}
p1 <- strip_plot(dsPRE, 105) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
p2 <- strip_plot(dsPOST, 105) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
plot_grid(p1, p2,
  nrow = 2,
  label_size = 8,
  align = "v"
)

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct105.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Study Lightswitch (TYPO) (SubActNum 92)

```{r subAct92, echo=FALSE, fig.cap="A caption", out.width = '100%'}
p1 <- strip_plot(dsPRE, 92) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
p2 <- strip_plot(dsPOST, 92) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
plot_grid(p1, p2,
  nrow = 2,
  label_size = 8,
  align = "v"
)

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct92.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Bathroom Door (SubActNum 130)

```{r subAct130, echo=FALSE, fig.cap="A caption", out.width = '100%'}
p1 <- strip_plot(dsPRE, 130) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
p2 <- strip_plot(dsPOST, 130) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
plot_grid(p1, p2,
  nrow = 2,
  label_size = 8,
  align = "v"
)

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct130.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Foyer Lightswitch (SubActNum 104)

```{r subAct104, echo=FALSE, fig.cap="A caption", out.width = '100%'}
strip_plot(dsPRE, 104) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct104.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Kitchen Toaster (SubActNum 131)

```{r subAct131, echo=FALSE, fig.cap="A caption", out.width = '100%'}
p1 <- strip_plot(dsPRE, 131) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
p2 <- strip_plot(dsPOST, 131) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
plot_grid(p1, p2,
  nrow = 2,
  label_size = 8,
  align = "v"
)

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct131.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Bathroom Exhaust Fan (SubActNum 96)

```{r subAct96, echo=FALSE, fig.cap="A caption", out.width = '100%'}
strip_plot(dsPRE, 96) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct96.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Bedroom Lightswitch (SubActNum 108)

```{r subAct108, echo=FALSE, fig.cap="A caption", out.width = '100%'}
strip_plot(dsPRE, 108) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct108.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Kitchen Oven (SubActNum 129)

```{r subAct129, echo=FALSE, fig.cap="A caption", out.width = '100%'}
strip_plot(dsPRE, 129) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct129.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Livingroom DVD (SubActNum 56)

DROPPED - One value only * 2

```{r subAct56, echo=FALSE, fig.cap="A caption", out.width = '100%'}
strip_plot(dsPRE, 56) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct56.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Livingroom Lamp (SubActNum 76)

```{r subAct76, echo=FALSE, fig.cap="A caption", out.width = '100%'}
strip_plot(dsPRE, 76) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct76.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Bedroom Jewelrybox (SubActNum 139)

```{r subAct139, echo=FALSE, fig.cap="A caption", out.width = '100%'}
strip_plot(dsPRE, 139) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct139.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Kitchen Washingmachine (SubActNum 142)

```{r subAct142, echo=FALSE, fig.cap="A caption", out.width = '100%'}
strip_plot(dsPRE, 142) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct142.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Kitchen Laundry Dryer (SubActNum 90)

```{r subAct90, echo=FALSE, fig.cap="A caption", out.width = '100%'}
strip_plot(dsPRE, 90) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct90.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Kitchen Garbage Disposal (SubActNum 98)

```{r subAct98, echo=FALSE, fig.cap="A caption", out.width = '100%'}
strip_plot(dsPRE, 98) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct98.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Livingroom Lightswitch (SubActNum 107)

```{r subAct107, echo=FALSE, fig.cap="A caption", out.width = '100%'}
p1 <- strip_plot(dsPRE, 107) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
p2 <- strip_plot(dsPOST, 107) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))
plot_grid(p1, p2,
  nrow = 2,
  label_size = 8,
  align = "v"
)

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct107.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```


#### Foyer Closet (SubActNum 81)

DROPPED

```{r subAct81, echo=FALSE, fig.cap="A caption", out.width = '100%'}
strip_plot(dsPRE, 81) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct81.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Kitchen Cereal (SubActNum 145)

DROPPED

```{r subAct145, echo=FALSE, fig.cap="A caption", out.width = '100%'}
strip_plot(dsPRE, 145) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct145.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Kitchen Containers (SubActNum 60)

DROPPED

```{r subAct60, echo=FALSE, fig.cap="A caption", out.width = '100%'}
strip_plot(dsPRE, 60) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct60.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Kitchen Coffee Machine (SubActNum 119)

```{r subAct119, echo=FALSE, fig.cap="A caption", out.width = '100%'}
strip_plot(dsPRE, 119) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct119.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```

#### Bedroom Lamp

DROPPED

```{r subAct64, echo=FALSE, fig.cap="A caption", out.width = '100%'}
strip_plot(dsPRE, 64) + theme(plot.margin = unit(c(0, 0, 0, 0), "cm"))

ggsave("/Users/alistairgj/Documents/GitHub/IoT_ResearchProject/IoT_November/images/subAct64.png", 
       plot = last_plot(), device = png(), 
       scale = 1.5, width = 18, height = 3, units = c("cm"), dpi = 300)
```
