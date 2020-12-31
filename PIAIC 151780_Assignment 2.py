#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[2]:


import numpy as np
y=np.arange(0,10)
z=y.reshape((2,5))
print(z.tolist())


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[3]:


import numpy as np
x=[[0,1,2,3,4],[5,6,7,8,9]]
y=[[1,1,1,1,1],[1,1,1,1,1]]
arrx=np.array(x)
arry=np.array(y)
np.concatenate((arrx,arry),axis=0)


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[6]:


import numpy as np
arr = np.arange(0,10)
arrx=arr.reshape((2,5))
arrx=arrx.astype('int32')
arry = np.ones((2,5))
arry=arry.astype('int32')
np.hstack((arrx,arry))


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[7]:


import numpy as np
y=np.array([[0, 1],[2, 3], [4, 5], [6, 7], [8, 9]])
print(y)
y.flatten()


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[8]:


import numpy as np
arr = np.arange(0,15)
x = arr.reshape((3,5))
print(x)
x.ravel()


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[49]:


import numpy as np
arr = np.arange(0,15)
x = arr.reshape((5,3))
print(x)


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[10]:


import numpy as np
x=np.random.randn(5,5)
print(x)
x**2


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[11]:


import numpy as np
x=np.random.randn(5,6)
print(x)
np.mean(x)


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[12]:


import numpy as np
x=np.random.randn(5,6)
print(x)
np.std(x)


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[13]:


import numpy as np
x=np.random.randn(5,6)
print(x)
np.median(x)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[14]:


import numpy as np
x=np.random.randn(5,6)
print(x)
x.transpose()


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[18]:


import numpy as np
x=np.array([[1, 7, 8, 5],[4, 6, 2, 3],[9, 4, 2, 3],[1, 1, 5, 7]])
x.trace()


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[20]:


import numpy as np
x=np.array([[1, 7, 8, 5],[4, 6, 2, 3],[9, 4, 2, 3],[1, 1, 5, 7]])
np.linalg.det(x)


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[21]:


import numpy as np
x=np.array([[1, 7, 8, 5],[4, 6, 2, 3],[9, 4, 2, 3],[1, 1, 5, 7]])
print(np.percentile(x, 5))
print(np.percentile(x, 95))


# ## Question:15

# ### How to find if a given array has any null values?

# In[23]:


import numpy as np
x=np.array([-3.2623, -6.0915, -6.663 , 5.3731, 3.6182, 3.45 , 5.0077])
y=np.sqrt(x)
print(y)
np.isnan(y)

