
# coding: utf-8

# In[15]:



## create binary search function
def binary_search(sorted_list, value):
    #starting low and high values to search between
    low = 0
    high = len(sorted_list) - 1
    
    #use while loop until value is found or list is completely search
    while(low <= high):
        #find middle index and value between low and high variables to search
        mid = (low + high) // 2
        guess = sorted_list[mid]
        
        #see if guess is correct
        if (guess == value):
            return "index: {}".format(mid)
        #if not, update low if guess is lower than value
        elif (guess < value):
            low = mid + 1
        #and update high if guess is too high
        else:
            high = mid - 1
            
    #value wasn't found in list
    print("value not in list")
    return None


# In[16]:


# fill a test list with integers from 1 to 100
test = []
for i in range(100):
    test.append(i + 1)


# In[22]:


answer = binary_search(test, 63) # test function
print(answer)

