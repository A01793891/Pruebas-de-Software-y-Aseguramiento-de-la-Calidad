#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np

# In[2]:


TC1=pd.read_csv('/Users/andrei/Documents/Maestria_MNA/Trimestre_6/Pruebas_de_Software/Semana4/Ejercicio_Programacion1/P1/TC1.txt',sep=" ")


# In[3]:


TC2=pd.read_csv('/Users/andrei/Documents/Maestria_MNA/Trimestre_6/Pruebas_de_Software/Semana4/Ejercicio_Programacion1/P1/TC2.txt',sep=" ")


# In[4]:


TC3=pd.read_csv('/Users/andrei/Documents/Maestria_MNA/Trimestre_6/Pruebas_de_Software/Semana4/Ejercicio_Programacion1/P1/TC3.txt',sep=" ")


# In[5]:


TC4=pd.read_csv('/Users/andrei/Documents/Maestria_MNA/Trimestre_6/Pruebas_de_Software/Semana4/Ejercicio_Programacion1/P1/TC4.txt',sep=" ")


# In[6]:


TC5=pd.read_csv('/Users/andrei/Documents/Maestria_MNA/Trimestre_6/Pruebas_de_Software/Semana4/Ejercicio_Programacion1/P1/TC5.txt',sep=" ")


# In[7]:


TC6=pd.read_csv('/Users/andrei/Documents/Maestria_MNA/Trimestre_6/Pruebas_de_Software/Semana4/Ejercicio_Programacion1/P1/TC6.txt',sep=" ")


# In[8]:


TC7=pd.read_csv('/Users/andrei/Documents/Maestria_MNA/Trimestre_6/Pruebas_de_Software/Semana4/Ejercicio_Programacion1/P1/TC7.txt',sep=" ")


# In[9]:


df = TC1


# In[10]:


df.columns = ['TC1']


# In[11]:


df ['TC2']= TC2
df ['TC3']= TC3
df ['TC4']= TC4
df ['TC5']= TC5
df ['TC6']= TC6
df ['TC7']= TC7


# In[12]:


df.loc[0] = ["480","72","18","-4.5","480","127620004531949000000.00","157638329490099000000.00"]


# In[13]:


print(df)


# In[14]:


df.describe()


# In[15]:


print(df)


# In[16]:


print(df['TC1'])


# In[17]:


df['TC1']= pd.to_numeric(df['TC1'],errors = 'coerce')


# In[18]:

# In[19]:

df['TC1'].describe()

# In[20]:


df['TC2']= pd.to_numeric(df['TC2'],errors = 'coerce')


# In[21]:


# In[22]:


df['TC3']= pd.to_numeric(df['TC3'],errors = 'coerce')


# In[23]:

# In[24]:


df['TC4']= pd.to_numeric(df['TC4'],errors = 'coerce')


# In[25]:

# In[26]:


print(df['TC5'])


# In[27]:


df['TC5']= pd.to_numeric(df['TC5'],errors = 'coerce')


# In[28]:

# In[29]:


df['TC5'].describe()


# In[30]:


print(df['TC6'])


# In[31]:


df['TC6']= pd.to_numeric(df['TC6'],errors = 'coerce')


# In[32]:

# In[33]:


df['TC6'].describe()


# In[34]:


print(df['TC7'])


# In[35]:


df['TC7']= pd.to_numeric(df['TC7'],errors = 'coerce')


# In[36]:

# In[37]:


df['TC7'].describe()


# In[38]:


print(df)


# In[39]:


df.isnull().values.any()


# In[40]:


df.isnull().any()


# In[41]:


df.isna().values.any()


# In[42]:


df.isna().any()


# In[43]:


df = df.dropna()


# In[44]:


print(df)


# In[45]:


df.isnull().values.any()


# In[46]:


df.isnull().any()


# In[47]:


df.isna().values.any()


# In[48]:

df.isna().any()
# In[49]:
def my_mean(datos):  
    mean= sum(datos)/len(datos)
    return mean
# In[50]:

meanTC1 = my_mean(df['TC1'])

# In[51]:


# In[52]:

ascendingTC1 = df.sort_values('TC1',ascending=False)

# In[53]:
# In[54]:
medianTC1 = pd.DataFrame(ascendingTC1)

# In[55]:

print(medianTC1.loc[152, 'TC1'])

# In[56]:

medianaTC1 = medianTC1.loc[152, 'TC1']

# In[57]:

# In[58]:

meanTC2 = my_mean(df['TC2'])

# In[59]:

# In[60]:

ascendingTC2 = df.sort_values('TC2',ascending=False)

# In[61]:
# In[62]:

medianTC2 = pd.DataFrame(ascendingTC2)

# In[63]:

print(medianTC2.loc[152, 'TC2'])

# In[64]:

medianaTC2 = medianTC2.loc[152, 'TC2']

# In[65]:

# In[66]:

meanTC3 = my_mean(df['TC3'])
ascendingTC3 = df.sort_values('TC3',ascending=False)

# In[67]:

# In[68]:

medianTC3 = pd.DataFrame(ascendingTC3)

# In[69]:

print(medianTC3.loc[152, 'TC3'])

# In[70]:

medianaTC3 = medianTC3.loc[152, 'TC3']

# In[71]:

meanTC4 = my_mean(df['TC4'])
ascendingTC4 = df.sort_values('TC4',ascending=False)

# In[72]:

# In[73]:

medianTC4 = pd.DataFrame(ascendingTC4)

# In[74]:

print(medianTC4.loc[152,'TC4'])

# In[75]:


medianaTC4 = medianTC4.loc[152,'TC4']


# In[76]:

# In[77]:

meanTC5 = my_mean(df['TC5'])
ascendingTC5 = df.sort_values('TC5',ascending=False)

# In[78]:

# In[79]:


medianTC5 = pd.DataFrame(ascendingTC5)


# In[80]:


print(medianTC5.loc[152,'TC5'])

# In[81]:


medianaTC5 = medianTC5.loc[152,'TC5']


# In[82]:

# In[83]:

meanTC6 = my_mean(df['TC6'])
ascendingTC6 = df.sort_values('TC6',ascending=False)

# In[84]:

# In[85]:

medianTC6 = pd.DataFrame(ascendingTC6)

# In[86]:


print(medianTC6.loc[152,'TC6'])


# In[87]:


medianaTC6 = medianTC6.loc[152,'TC6']


# In[88]:


# In[89]:

meanTC7 = my_mean(df['TC7'])
ascendingTC7 = df.sort_values('TC7',ascending=False)

# In[90]:


# In[91]:

medianTC7 = pd.DataFrame(ascendingTC7)

# In[92]:

print(medianTC7.loc[152,'TC7'])

# In[93]:

medianaTC7 = medianTC7.loc[152,'TC7']

# In[94]:

# In[95]:

def my_var(columna):
   media = sum(columna)/len(columna)
   num = len(columna)
   suma = 0
   for dato in columna:
      suma += (dato-media)**2
   varianza = suma/(num-1)
   return varianza


# In[96]:

varianzaTC1=my_var(df['TC1'])

# In[97]:


# In[98]:

varianzaTC2=my_var(df['TC2'])

# In[99]:

varianzaTC3=my_var(df['TC3'])

# In[100]:

varianzaTC4=my_var(df['TC4'])

# In[101]:

varianzaTC5=my_var(df['TC5'])

# In[102]:

varianzaTC6=my_var(df['TC6'])

# In[103]:

varianzaTC7=my_var(df['TC7'])

# In[104]:

devStandarTC1= pow(varianzaTC1, 0.5)

# In[105]:

# In[106]:

devStandarTC2= pow(varianzaTC2, 0.5)

# In[107]:

# In[108]:

devStandarTC3= pow(varianzaTC3, 0.5)

# In[109]:

devStandarTC4= pow(varianzaTC4, 0.5)


# In[110]:


devStandarTC5= pow(varianzaTC5, 0.5)


# In[111]:


devStandarTC6= pow(varianzaTC6, 0.5)


# In[112]:


devStandarTC7= pow(varianzaTC7, 0.5)

# In[113]:

# In[114]:

datosTC1 = df['TC1']
diccionario_conteoTC1 = {}


# In[115]:

for numero in datosTC1:
    CLAVE = str(numero)
# Si no existe...
    if CLAVE not in diccionario_conteoTC1:
# lo agregamos:
        diccionario_conteoTC1[CLAVE] = 1
# Si ya existe...
    else:
# Lo aumentamos
        diccionario_conteoTC1[CLAVE] += 1

# In[116]:


FRECUENCIA_MAYOR = 0
numero_mas_repetido = datosTC1[0]
# Imprimimos el diccionario solo para depurar
print(diccionario_conteoTC1)


# In[117]:


for numero in diccionario_conteoTC1:
    if diccionario_conteoTC1[numero] > FRECUENCIA_MAYOR:
        numero_mas_repetido = numero
        FRECUENCIA_MAYOR = diccionario_conteoTC1[numero]
# Finalmente imprimimos el más repetido, con su conteo
conteo = diccionario_conteoTC1[str(numero_mas_repetido)]


# In[118]:


print(
    f"El número que más se repite es {numero_mas_repetido} (encontrado {conteo} ocasiones)"
)


# In[119]:


ModaTC1 = numero_mas_repetido


# In[120]:


# In[121]:


datosTC2= df['TC2']
diccionario_conteoTC2 = {}


# In[122]:


for numero in datosTC2:
    CLAVE = str(numero)
# Si no existe...
    if CLAVE not in diccionario_conteoTC2:
# lo agregamos:
        diccionario_conteoTC2[CLAVE] = 1
# Si ya existe...
    else:
# Lo aumentamos
        diccionario_conteoTC2[CLAVE] += 1


# In[123]:


FRECUENCIA_MAYOR = 0
numero_mas_repetido = datosTC2[0]
# Imprimimos el diccionario solo para depurar
print(diccionario_conteoTC2)


# In[124]:


for numero in diccionario_conteoTC2:
    if diccionario_conteoTC2[numero] > FRECUENCIA_MAYOR:
        numero_mas_repetido = numero
        FRECUENCIA_MAYOR = diccionario_conteoTC2[numero]
# Finalmente imprimimos el más repetido, con su conteo
conteo = diccionario_conteoTC2[str(numero_mas_repetido)]


# In[125]:


print(
    f"El número que más se repite es {numero_mas_repetido} (encontrado {conteo} ocasiones)"
)


# In[126]:


ModaTC2 = numero_mas_repetido

# In[127]:


datosTC3= df['TC3']
diccionario_conteoTC3 = {}


# In[128]:


for numero in datosTC3:
    CLAVE = str(numero)
# Si no existe...
    if CLAVE not in diccionario_conteoTC3:
# lo agregamos:
        diccionario_conteoTC3[CLAVE] = 1
# Si ya existe...
    else:
# Lo aumentamos
        diccionario_conteoTC3[CLAVE] += 1

FRECUENCIA_MAYOR = 0
numero_mas_repetido = datosTC3[0]
# Imprimimos el diccionario solo para depurar
print(diccionario_conteoTC3)


# In[129]:


for numero in diccionario_conteoTC3:
    if diccionario_conteoTC3[numero] > FRECUENCIA_MAYOR:
        numero_mas_repetido = numero
        FRECUENCIA_MAYOR = diccionario_conteoTC3[numero]
# Finalmente imprimimos el más repetido, con su conteo
conteo = diccionario_conteoTC3[str(numero_mas_repetido)]


# In[130]:


print(
    f"El número que más se repite es {numero_mas_repetido} (encontrado {conteo} ocasiones)"
)


# In[131]:


ModaTC3 = numero_mas_repetido

# In[132]:


datosTC4= df['TC4']
diccionario_conteoTC4 = {}


# In[133]:


for numero in datosTC4:
    CLAVE = str(numero)
# Si no existe...
    if CLAVE not in diccionario_conteoTC4:
# lo agregamos:
        diccionario_conteoTC4[CLAVE] = 1
# Si ya existe...
    else:
# Lo aumentamos
        diccionario_conteoTC4[CLAVE] += 1

FRECUENCIA_MAYOR = 0
numero_mas_repetido = datosTC4[0]
# Imprimimos el diccionario solo para depurar
print(diccionario_conteoTC4)


# In[134]:


for numero in diccionario_conteoTC4:
    if diccionario_conteoTC4[numero] > FRECUENCIA_MAYOR:
        numero_mas_repetido = numero
        FRECUENCIA_MAYOR = diccionario_conteoTC4[numero]
# Finalmente imprimimos el más repetido, con su conteo
conteo = diccionario_conteoTC4[str(numero_mas_repetido)]

print(
    f"El número que más se repite es {numero_mas_repetido} (encontrado {conteo} ocasiones)"
)


# In[135]:


ModaTC4 = numero_mas_repetido

# In[136]:


datosTC5= df['TC5']
diccionario_conteoTC5 = {}


# In[137]:


for numero in datosTC5:
    CLAVE = str(numero)
# Si no existe...
    if CLAVE not in diccionario_conteoTC5:
# lo agregamos:
        diccionario_conteoTC5[CLAVE] = 1
# Si ya existe...
    else:
# Lo aumentamos
        diccionario_conteoTC5[CLAVE] += 1

FRECUENCIA_MAYOR = 0
numero_mas_repetido = datosTC5[0]
# Imprimimos el diccionario solo para depurar
print(diccionario_conteoTC5)


# In[138]:


for numero in diccionario_conteoTC5:
    if diccionario_conteoTC5[numero] > FRECUENCIA_MAYOR:
        numero_mas_repetido = numero
        FRECUENCIA_MAYOR = diccionario_conteoTC5[numero]
# Finalmente imprimimos el más repetido, con su conteo
conteo = diccionario_conteoTC5[str(numero_mas_repetido)]

print(
    f"El número que más se repite es {numero_mas_repetido} (encontrado {conteo} ocasiones)"
)


# In[139]:


ModaTC5 = numero_mas_repetido

# In[140]:


datosTC6= df['TC6']
diccionario_conteoTC6 = {}


# In[141]:


for numero in datosTC6:
    CLAVE = str(numero)
# Si no existe...
    if CLAVE not in diccionario_conteoTC6:
# lo agregamos:
        diccionario_conteoTC6[CLAVE] = 1
# Si ya existe...
    else:
# Lo aumentamos
        diccionario_conteoTC6[CLAVE] += 1

FRECUENCIA_MAYOR = 0
numero_mas_repetido = datosTC6[0]
# Imprimimos el diccionario solo para depurar
print(diccionario_conteoTC6)


# In[142]:


for numero in diccionario_conteoTC6:
    if diccionario_conteoTC6[numero] > FRECUENCIA_MAYOR:
        numero_mas_repetido = numero
        FRECUENCIA_MAYOR = diccionario_conteoTC6[numero]
# Finalmente imprimimos el más repetido, con su conteo
conteo = diccionario_conteoTC6[str(numero_mas_repetido)]

print(
    f"El número que más se repite es {numero_mas_repetido} (encontrado {conteo} ocasiones)"
)


# In[143]:


ModaTC6 = numero_mas_repetido


# In[144]:


datosTC7= df['TC7']
diccionario_conteoTC7 = {}


# In[145]:


for numero in datosTC7:
    CLAVE = str(numero)
# Si no existe...
    if CLAVE not in diccionario_conteoTC7:
# lo agregamos:
        diccionario_conteoTC7[CLAVE] = 1
# Si ya existe...
    else:
# Lo aumentamos
        diccionario_conteoTC7[CLAVE] += 1

FRECUENCIA_MAYOR = 0
numero_mas_repetido = datosTC7[0]
# Imprimimos el diccionario solo para depurar
print(diccionario_conteoTC7)


# In[146]:


for numero in diccionario_conteoTC7:
    if diccionario_conteoTC7[numero] > FRECUENCIA_MAYOR:
        numero_mas_repetido = numero
        FRECUENCIA_MAYOR = diccionario_conteoTC7[numero]
# Finalmente imprimimos el más repetido, con su conteo
conteo = diccionario_conteoTC7[str(numero_mas_repetido)]

print(
    f"El número que más se repite es {numero_mas_repetido} (encontrado {conteo} ocasiones)"
)


# In[147]:

ModaTC7 = numero_mas_repetido


# In[148]:


TC1Statistics = pd.DataFrame([meanTC1,medianaTC1,ModaTC1,varianzaTC1,devStandarTC1])


# In[149]:


TC2Statistics = pd.DataFrame([meanTC2,medianaTC2,ModaTC2,varianzaTC2,devStandarTC2])


# In[150]:


TC3Statistics = pd.DataFrame([meanTC3,medianaTC3,ModaTC3,varianzaTC3,devStandarTC3])


# In[151]:


TC4Statistics = pd.DataFrame([meanTC4,medianaTC4,ModaTC4,varianzaTC4,devStandarTC4])


# In[152]:


TC5Statistics = pd.DataFrame([meanTC5,medianaTC5,ModaTC5,varianzaTC5,devStandarTC5,])


# In[153]:


TC6Statistics = pd.DataFrame([meanTC6,medianaTC6,ModaTC6,varianzaTC6,devStandarTC6,])


# In[154]:


TC7Statistics = pd.DataFrame([meanTC7,medianaTC7,ModaTC7,varianzaTC7,devStandarTC7,])


# In[155]:

Results = pd.concat([TC1Statistics,TC2Statistics,TC3Statistics,TC4Statistics,
                     TC5Statistics,TC6Statistics,TC7Statistics], axis=1)
Results.columns = ['TC1','TC2','TC3','TC4','TC5','TC6','TC7']    
Results.index = ['mean','median','Mode','variance','DevStnd']

# In[156]:

# In[157]:

Results.to_csv('StatisticsResults.txt', sep='\t', index=False)