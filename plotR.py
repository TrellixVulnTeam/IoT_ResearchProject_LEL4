import pandas as pd
import rpy2
#%matplotlib inline
from rpy2.robjects import pandas2ri
pandas2ri.activate()
#%load_ext rpy2.ipython

%%R -u px -w 1000 -h 800
p <- ggplot(total_counts, aes(x = subAct, y = count, group = DAY, color = DAY))
p <- p + geom_line()
p <- p + geom_point()
p <- p + coord_flip() + labs(title = "Plot of SubActivity Count versus SubActivity",
                             subtitle = "ADD SUBTITLE",
                             caption = "Source: TBU",
                             x = "SubActivity",
                             y = "Aggregated Count")
p