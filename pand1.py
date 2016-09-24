import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
web_status={'Day':[2,3,2,34,23],
			'Visitors':[23,23,34,54,65],
			'Bousd':[23.4,34,34,54,23]}
df=pd.DataFrame(web_status)
print df