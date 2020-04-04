#!/usr/bin/env python
# coding: utf-8

# In[37]:


import requests
import re
import json
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts.charts import Page


# In[38]:


url='http://ncov.dxy.cn/ncovh5/view/pneumonia'
html=requests.get(url).content.decode('utf-8')
data=re.findall('getListByCountryTypeService2true = (.*?)}catch',html)[0]
data=json.loads(data)


# In[39]:


needed_data=[{
    'continents':country['continents'],
    'country_name':country['provinceName'],
    'current_confirmed_count':country['currentConfirmedCount'],
    'confirmed_count':country['confirmedCount'],
    'cured_count':country['curedCount'],
    'dead_count':country['deadCount'],
    'dead_rate':country['deadRate']
    }for country in data]
data=pd.DataFrame(needed_data)
data


# In[40]:


group_data=data.groupby('continents')
group_data=group_data.sum()
group_data=group_data.sort_values(by='current_confirmed_count',ascending=False)
group_data


# In[41]:


bar=Bar()
bar.add_xaxis(['欧洲','北美洲','亚洲','南美洲','非洲','大洋洲','其他'])
bar.add_yaxis("current_confirmed_count",group_data['current_confirmed_count'].tolist(),category_gap="40%")
bar.add_yaxis("confirmed_count",group_data['confirmed_count'].tolist(),category_gap="40%")
bar.add_yaxis("cured_count",group_data['cured_count'].tolist(),category_gap="40%")
bar.add_yaxis("dead_count",group_data['dead_count'].tolist(),category_gap="40%")
bar.set_global_opts(title_opts=opts.TitleOpts(title="全球疫情可视化-pie"),
                    toolbox_opts=opts.ToolboxOpts())
bar.render('./全球疫情可视化-pie.html')


# In[42]:


data_one=data.sort_values(by='dead_rate',ascending=False)
data_one=data_one[:10]
data_one


# In[ ]:





# In[ ]:





# In[ ]:




