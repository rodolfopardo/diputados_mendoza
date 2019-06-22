
# coding: utf-8

# ## Estos son los diputados elegidos por los partidos políticos

# Los diputados han sido elegidos para competir en las PASO 2019 en las presidenciales legislativas.
# Nombres como Alfredo Cornejo, Omar De Marchi, Alejandro Bermejo y Marcelo Romano suenan en las listas confeccionadas por los partidos políticos. 

# In[1]:


cambia_mza = ["Cornejo", "De Marchi", "Latorre"]


# In[2]:


peronismo = ["Uceda", "Bermejo", "Carmona"]


# In[3]:


protectora = ["Romano", "Montiveros", "Montilla"]


# Imprimiendo a los **candidatos** de los diferentes _partidos políticos_ 

# In[4]:


print("Los candidatos de Cambia Mendoza son:", cambia_mza)


# In[5]:


print("Los candidatos del peronismo mendocino son:", peronismo)


# In[6]:


print("Los candidatos de Protectora son:", protectora)


# Para los candidatos del **FIT** el ingreso será manual debido al desconocimiento de la lista

# In[13]:


fit_mendoza = input("¿Cuál es el candidato del Fit que conoce?")


# In[15]:


if fit_mendoza == "Barbeito":
    
    print("Es correcto")

else:
        
    print("No es correcto")


# Es hora de **combinar** todas las listas de todos los partidos

# In[16]:


lista_general = cambia_mza + peronismo + protectora
print(lista_general)


# Es hora de **eliminar** los candidatos de **Cambia Mendoza**

# In[25]:


lista_general.reverse()

print(lista_general)


# Ingresamos hipoteticamente un **nuevo integrante**

# In[40]:


lista_general.append("Pardo")


# In[41]:


lista_general


# In[50]:


lista_general.remove("Montilla")


# In[51]:


lista_general


# In[53]:


lista_general.remove("Romano")


# In[54]:


lista_general

