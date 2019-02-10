#!/usr/bin/env python
# coding: utf-8

# In[1]:


matplotlib inline


# In[8]:


from matplotlib import pyplot as plt
import math

def normal_pdf(x, mu=0, sigma=1):
    den = ( 2*(math.pi)*(sigma**2) )**(0.5)
    num = math.exp(- ((x-mu)**2)/(2*(sigma**2)) )
    ans = num / den
    return ans

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '-', label='mu=0,sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], '-', label='mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, sigma=-1) for x in xs], '-', label='mu=0,sigma=-1')
plt.legend()
plt.show()


# In[ ]:




