#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Retailitem:
    def __init__(self,description, inventory,price):
        self._descrition=description
        self._inventory=inventory
        self._price=price
        
    def _set_descritions(self,description):
        self._descrition=description
        
    def _set_inventory(self,inventory):
        self._inventory=inventory
        
    def _set_price(self,price):
        self._price=price
     
    
    def _get_descritions(self):
        return self._descrition
        
    def _get_inventory(self):
        return self._inventory
        
    def _get_price(self):
        return self._price
     


# In[ ]:





# In[6]:





# In[ ]:




