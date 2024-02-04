#!/usr/bin/env python
# coding: utf-8

# In[2]:

import pandas as pd

# In[3]:


TX=pd.read_csv('/Users/andrei/Documents/Maestria_MNA/Trimestre_6/Pruebas_de_Software/Semana4/Ejercicio_Programacion1/P2/TC1.txt')


# In[4]:


TC2=pd.read_csv('/Users/andrei/Documents/Maestria_MNA/Trimestre_6/Pruebas_de_Software/Semana4/Ejercicio_Programacion1/P2/TC2.txt')


# In[5]:


TC3=pd.read_csv('/Users/andrei/Documents/Maestria_MNA/Trimestre_6/Pruebas_de_Software/Semana4/Ejercicio_Programacion1/P2/TC3.txt')


# In[6]:


TC4=pd.read_csv('/Users/andrei/Documents/Maestria_MNA/Trimestre_6/Pruebas_de_Software/Semana4/Ejercicio_Programacion1/P2/TC4.txt')


# In[7]:


TX.columns = ['TC1']
TC2.columns = ['TC2']
TC3.columns = ['TC3']
TC4.columns = ['TC4']


# In[8]:


# In[9]:


TX.loc[0] = ["6980368"]
TC2.loc[0] = ["7116776"]
TC3.loc[0] = ["-39"]
TC4.loc[0] = ["-39"]


# In[10]:


# In[11]:


TC1Hex = TX['TC1']
TC2Hex = TC2['TC2']
TC3Hex = TC3['TC3']
TC4Hex = TC4['TC4']


# In[12]:


def binary(num):
    sample = bin(num & int("1"*24, 2))[2:]
    return ("{0:0>%s}" % (24)).format(sample)


# In[13]:


TX = TX.dropna()


# In[14]:


TX['TC1'] = TX['TC1'].astype(int)
TX['TC1'] = TX.apply(lambda x: binary(x[0]), axis=1)

# In[15]:


TC2['TC2'] = TC2['TC2'].astype(int)


# In[16]:


# In[17]:


TC2['TC2']= TC2.apply(lambda x: binary(x[0]), axis=1)


# In[18]:


# In[19]:


TC3['TC3'] = TC3['TC3'].astype(int)

TC3['TC3']= TC3.apply(lambda x: binary(x[0]), axis=1)


# In[20]:


TC4['TC4']= pd.to_numeric(TC4['TC4'],errors = 'coerce')
TC4 = TC4.dropna()


# In[21]:


# In[22]:


TC4['TC4'] = TC4['TC4'].astype(int)


# In[23]:


TC4['TC4']= TC4.apply(lambda x: binary(x[0]), axis=1)


# In[24]:


# In[25]:


BinaryNum = pd.concat([TX, TC2, TC3, TC4], axis=1)


# In[26]:


print(BinaryNum)


# In[27]:


# In[28]:


TC1Hex = TC1Hex.astype(int)
TC1Hex = TC1Hex.apply( hex )


# In[29]:


# In[30]:


TC2Hex = TC2Hex.astype(int)
TC2Hex = TC2Hex.apply( hex )


# In[31]:


# In[32]:


TC3Hex = TC3Hex.astype(int)
TC3Hex = TC3Hex.apply( hex )


# In[33]:

# In[34]:


TC4Hex = pd.to_numeric(TC4Hex,errors = 'coerce')
TC4Hex = TC4Hex.dropna()


# In[35]:


TC4Hex = TC4Hex.astype(int)
TC4Hex = TC4Hex.apply( hex )


# In[36]:


# In[37]:


HexadecimalNum = pd.concat([TC1Hex, TC2Hex, TC3Hex, TC4Hex], axis=1)


# In[38]:


print(HexadecimalNum)


# In[39]:


Results = pd.concat([BinaryNum, HexadecimalNum], axis=1)


# In[40]:


Results.columns = ['BinaryTC1', 'BinaryTC2', 'BinaryTC3', 'BinaryTC4', 'HexTC1', 'HexTC2','HexTC3','HexTC4']


# In[41]:


# In[42]:


Results.to_csv('fileWithData.txt', sep='\t', index=False)