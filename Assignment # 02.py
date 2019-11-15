#!/usr/bin/env python
# coding: utf-8

# In[1]:


sub1 = int(input("Enter First Subject: "))
sub2 = int(input("Enter Second Subject: ")) 
sub3 = int(input("Enter Third Subject: "))
sub4 = int(input("Enter Fourth Subject: "))
sub5 = int(input("Enter Fifth Subject: "))
avg = (sub1+sub2+sub3+sub4+sub5)/5
if(avg>=90):
    
 print("Grade: A")
elif(avg>=80):
 print("Grade: B")
elif(avg>=70):
 print("Grade: C")
elif(avg>=60):
 print("Grade: D")
else:
 print("Grade: F")

Total = sub1+sub2+sub3+sub4+sub5
print("Total Marks:",Total)


# In[2]:



num = int(input("Enter Number"))
if (num % 2 == 0):
 print(num, "Num is Even")
else:
 print(num, "Num is odd")


# In[3]:


list=[1,2,3,4,5,43,43,21,55,67]
print("Length of List:",len(list))


# In[4]:


mylist = [2, 2, 2, 2, 2];
total = sum(mylist);

print(total)


# In[5]:


mylist = [14, 19, 41, 49, 100]

print("Largest num is:", max(mylist))


# In[6]:


a= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
  if i<5:
    print(i)


# In[ ]:




