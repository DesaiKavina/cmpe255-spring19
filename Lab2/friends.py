#!/usr/bin/env python
# coding: utf-8

# In[9]:


users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

ans = []
num_of_friends = []

def num_friends(user):
    count = 0
    for i in range(len(friendship)):
        if user == friendship[i][0]:
            count = count + 1
    return count
    pass

def sort_by_num_friends():
    for j in range(len(users)):
        val = num_friends(users[j]["id"])
        num_of_friends.append(val)
        ans.append((val, users[j]["name"]))   
    pass

def mean_num_friends(x):
    mean = sum(x)/len(x)
    return mean

def median_num_friends(x):
    x.sort()
    print("\nLisy of number of friends : ",x)
    n = len(x)
    if n%2==0:
        median = (x[n//2] + x[(n//2)+1]) / 2
    elif n%2!=0:
        median = x[n//2]
    return median

sort_by_num_friends()
ans1 = sorted(ans, reverse=True)
print("The names of people and their number of friends are : \n")
for itr in range(len(ans1)):
    print("{} has {} friends".format(ans1[itr][1],ans1[itr][0]))
    
median =  median_num_friends(num_of_friends)
mean = mean_num_friends(num_of_friends)
print("\nThe mean is  : ",mean)
print("\nThe median is : ",median)


# In[ ]:




