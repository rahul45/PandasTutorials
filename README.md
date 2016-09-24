# PandasTutorials
Installation Process:
	step1 :download pip
	step2 :run get-pip.py
	step3: install pandas by using below command
		>pip install pandas
	step4: install metplotlib 
		>pip install metplotlib
	

#pandas.io.data as web
 ##pandas works with many type of datatype different file format like .csv etc
pd.DataFrame(dictionary)
print(df)

#Dictonary Representation in Pandas
#'''
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
#import pandas.io.data as web
style.use('ggplot')#using plots style
web_status={'Day':[2,3,2,34,23,23],
			'Visitors':[23,23,34,54,65,43],
			'Bousd':[23.4,34,34,54,23,34]}
df=pd.DataFrame(web_status)
##for setting a index
print df.set_index('Day')
##if you want to set index for evry then
#df=df.set_index("Day")
##Or you can also set the index by using inplace is true
df.set_index("Day",inplace=True)
#print df
#print df.head()#will print first five
#will print last five by defult
print df.tail()
##you can also pass the parameter here like want to print last 3 or 2
##then just pass into the function or in head too you can pass the number
print "_______________________________"
print df.tail(3)
print "_____________________________\n"
print df.head(6)



