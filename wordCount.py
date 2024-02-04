#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:


TC1=pd.read_csv('/Users/andrei/Documents/Maestria_MNA/Trimestre_6/Pruebas_de_Software/Semana4/Ejercicio_Programacion1/P3/TC1.txt')


# In[3]:


TC2=pd.read_csv('/Users/andrei/Documents/Maestria_MNA/Trimestre_6/Pruebas_de_Software/Semana4/Ejercicio_Programacion1/P3/TC2.txt')


# In[4]:


TC3=pd.read_csv('/Users/andrei/Documents/Maestria_MNA/Trimestre_6/Pruebas_de_Software/Semana4/Ejercicio_Programacion1/P3/TC3.txt')


# In[5]:


TC4=pd.read_csv('/Users/andrei/Documents/Maestria_MNA/Trimestre_6/Pruebas_de_Software/Semana4/Ejercicio_Programacion1/P3/TC4.txt')


# In[6]:


TC5=pd.read_csv('/Users/andrei/Documents/Maestria_MNA/Trimestre_6/Pruebas_de_Software/Semana4/Ejercicio_Programacion1/P3/TC5.txt')


# In[7]:


df = TC1


# In[8]:



# In[9]:


df.columns = ['TC1']


# In[10]:



# In[11]:


df ['TC2']= TC2
df ['TC3']= TC3
df ['TC4']= TC4
df ['TC5']= TC5


# In[12]:


df.loc[0] = ["mother","conduct","neighbors","disciplinary","loaded"]


# In[13]:


print(df)


# In[14]:


datos= df['TC1']
diccionario_conteoTC1 = {}


# In[15]:


for numero in datos:
    CLAVE = str(numero)
# Si no existe...
    if CLAVE not in diccionario_conteoTC1:
# lo agregamos:
        diccionario_conteoTC1[CLAVE] = 1
# Si ya existe...
    else:
# Lo aumentamos
        diccionario_conteoTC1[CLAVE] += 1


# In[16]:


FRECUENCIA_MAYOR = 0
numero_mas_repetido = datos[0]
# Imprimimos el diccionario solo para depurar
print(diccionario_conteoTC1)


# In[17]:

for numero in diccionario_conteoTC1:
    if diccionario_conteoTC1[numero] > FRECUENCIA_MAYOR:
        numero_mas_repetido = numero
        FRECUENCIA_MAYOR = diccionario_conteoTC1[numero]
# Finalmente imprimimos el más repetido, con su conteo
conteo = diccionario_conteoTC1[str(numero_mas_repetido)]


# In[18]:


print(
    f"El número que más se repite es {numero_mas_repetido} (encontrado {conteo} ocasiones)"
)


# In[19]:


datos= df['TC2']
diccionario_conteoTC2 = {}


# In[20]:


for numero in datos:
    CLAVE = str(numero)
# Si no existe...
    if CLAVE not in diccionario_conteoTC2:
# lo agregamos:
        diccionario_conteoTC2[CLAVE] = 1
# Si ya existe...
    else:
# Lo aumentamos
        diccionario_conteoTC2[CLAVE] += 1


# In[21]:


FRECUENCIA_MAYOR = 0
numero_mas_repetido = datos[0]
# Imprimimos el diccionario solo para depurar
print(diccionario_conteoTC2)


# In[22]:


for numero in diccionario_conteoTC2:
    if diccionario_conteoTC2[numero] > FRECUENCIA_MAYOR:
        numero_mas_repetido = numero
        FRECUENCIA_MAYOR = diccionario_conteoTC2[numero]
# Finalmente imprimimos el más repetido, con su conteo
conteo = diccionario_conteoTC2[str(numero_mas_repetido)]


# In[23]:


print(
    f"El número que más se repite es {numero_mas_repetido} (encontrado {conteo} ocasiones)"
)


# In[24]:


datos= df['TC3']
diccionario_conteoTC3 = {}


# In[25]:


for numero in datos:
    CLAVE = str(numero)
# Si no existe...
    if CLAVE not in diccionario_conteoTC3:
# lo agregamos:
        diccionario_conteoTC3[CLAVE] = 1
# Si ya existe...
    else:
# Lo aumentamos
        diccionario_conteoTC3[CLAVE] += 1


# In[26]:


FRECUENCIA_MAYOR = 0
numero_mas_repetido = datos[0]
# Imprimimos el diccionario solo para depurar
print(diccionario_conteoTC3)


# In[27]:


for numero in diccionario_conteoTC3:
    if diccionario_conteoTC3[numero] > FRECUENCIA_MAYOR:
        numero_mas_repetido = numero
        FRECUENCIA_MAYOR = diccionario_conteoTC3[numero]
# Finalmente imprimimos el más repetido, con su conteo
conteo = diccionario_conteoTC3[str(numero_mas_repetido)]


# In[28]:


print(
    f"El número que más se repite es {numero_mas_repetido} (encontrado {conteo} ocasiones)"
)


# In[29]:


datos= df['TC4']
diccionario_conteoTC4 = {}


# In[30]:


for numero in datos:
    CLAVE = str(numero)
# Si no existe...
    if CLAVE not in diccionario_conteoTC4:
# lo agregamos:
        diccionario_conteoTC4[CLAVE] = 1
# Si ya existe...
    else:
# Lo aumentamos
        diccionario_conteoTC4[CLAVE] += 1


# In[31]:


FRECUENCIA_MAYOR = 0
numero_mas_repetido = datos[0]
# Imprimimos el diccionario solo para depurar
print(diccionario_conteoTC4)


# In[32]:


for numero in diccionario_conteoTC4:
    if diccionario_conteoTC4[numero] > FRECUENCIA_MAYOR:
        numero_mas_repetido = numero
        FRECUENCIA_MAYOR = diccionario_conteoTC4[numero]
# Finalmente imprimimos el más repetido, con su conteo
conteo = diccionario_conteoTC4[str(numero_mas_repetido)]


# In[33]:


print(
    f"El número que más se repite es {numero_mas_repetido} (encontrado {conteo} ocasiones)"
)


# In[34]:


datos= df['TC5']
diccionario_conteoTC5 = {}


# In[35]:


for numero in datos:
    CLAVE = str(numero)
# Si no existe...
    if CLAVE not in diccionario_conteoTC5:
# lo agregamos:
        diccionario_conteoTC5[CLAVE] = 1
# Si ya existe...
    else:
# Lo aumentamos
        diccionario_conteoTC5[CLAVE] += 1


# In[36]:


FRECUENCIA_MAYOR = 0
numero_mas_repetidoTC5 = datos[0]
# Imprimimos el diccionario solo para depurar
print(diccionario_conteoTC5)


# In[37]:


for numero in diccionario_conteoTC5:
    if diccionario_conteoTC5[numero] > FRECUENCIA_MAYOR:
        numero_mas_repetido = numero
        FRECUENCIA_MAYOR = diccionario_conteoTC5[numero]
# Finalmente imprimimos el más repetido, con su conteo
conteo = diccionario_conteoTC5[str(numero_mas_repetido)]


# In[38]:


print(
    f"El número que más se repite es {numero_mas_repetido} (encontrado {conteo} ocasiones)"
)


# In[68]:


dataConteo = [diccionario_conteoTC1,diccionario_conteoTC2,diccionario_conteoTC3,
              diccionario_conteoTC4,diccionario_conteoTC5]


# In[78]:


ConteoTotal = pd.DataFrame.from_dict(dataConteo)


# In[84]:


ConteoTotal.index = ['TC1', 'TC2', 'TC3','TC4','TC5']


# In[85]:


print(ConteoTotal)


# In[86]:


ConteoTotal.to_csv('fileWithDataCount.txt', sep='\t', index=False)
