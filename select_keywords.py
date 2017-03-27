

# coding: utf-8

# In[4]:

import sys
import os
import json
sys.path.append(os.path.join(os.getcwd(),'..'))
import watson_developer_cloud
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features
import xlwt


# In[3]:

nlu = watson_developer_cloud.NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='Put your username here',
    password='Put your password here')


# In[6]:

response = nlu.analyze(
    language='en',
    text = input('input =\n'),
    features=[features.Keywords()])

# print(json.dumps(response, indent=2))

my_keywords = response['keywords']
# print(my_keywords)

book = xlwt.Workbook()
newSheet_1 = book.add_sheet('KW_1')

newSheet_1.write(0, 0, 'KW')
newSheet_1.write(0, 1, 'Relevance')
i = 1 
for word in my_keywords:
    newSheet_1.write(i, 0, word['text'])
    newSheet_1.write(i, 1, word['relevance'])
    i += 1

filename = input("filename = ") + ".xls"
book.save(filename)
print("successfully saved! ({0})".format(filename))

# In[ ]:




