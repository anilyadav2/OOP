#!/usr/bin/env python
# coding: utf-8

# In[1]:
import Retail_class as rc


def main():
    item1=rc.Retailitem('Jacket',12,59.95)
    item2=rc.Retailitem('Designer Jeans',40,34.95)
    item3=rc.Retailitem('shirt',20,24.95)
    
    print('descritions','inventory','price')
    print(item1._get_descritions(),item1._get_inventory(),item1._get_price())
    print(item2._get_descritions(),item2._get_inventory(),item2._get_price())
    print(item3._get_descritions(),item3._get_inventory(),item3._get_price())

main()    
    


# In[ ]:





# In[6]:





# In[ ]:




