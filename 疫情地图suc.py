#!/usr/bin/env python
# coding: utf-8

# In[37]:


import requests
import re
import json
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Page


# In[29]:


url='http://ncov.dxy.cn/ncovh5/view/pneumonia'
html=requests.get(url).content.decode('utf8')
data=re.findall('getAreaStat = (.*?)}catch',html)[0]
data=json.loads(data)
data


# In[30]:


needed_data=[{
    'provinceShortName':province['provinceShortName'],
    'confirmedCount':province['confirmedCount'],
    'currentConfirmedCount':province['currentConfirmedCount']
}for province in data]
needed_data


# In[34]:


needed_data=pd.DataFrame(needed_data)
needed_data


# In[36]:


list_province=needed_data['provinceShortName'].tolist()
list_confirmed_count=needed_data['confirmedCount'].tolist()
list_current_confirmed_count=needed_data['currentConfirmedCount'].tolist()


# In[68]:


map_one=Map()
map_one.add("现存确诊",zip(list_province,list_current_confirmed_count))
map_one.set_global_opts(title_opts=opts.TitleOpts(title="中国疫情地图-现存确诊"),
                    visualmap_opts=opts.VisualMapOpts(pieces=[{"value":0,"color":'white'},
                                                             {"min":1,"max":29},
                                                             {"min":30,"max":99},
                                                             {"min":100,"max":499},
                                                             {"min":500,"color":'red'}],
                                                      is_piecewise=True))
map_two=Map()
map_two.add("累计确诊",zip(list_province,list_confirmed_count))
map_two.set_global_opts(title_opts=opts.TitleOpts(title="中国疫情地图-累计确诊"),
                     visualmap_opts=opts.VisualMapOpts(pieces=[{"value":0,"color":'white'},
                                                             {"min":1,"max":29},
                                                             {"min":30,"max":99},
                                                             {"min":100,"max":499},
                                                             {"min":500,"max":999},
                                                              {"min":1000,"color":'red'}],is_piecewise=True)  )


# In[69]:


page=Page()
page.add(map_one)
page.add(map_two)
page.render('./疫情地图-2.html')


# In[ ]:




