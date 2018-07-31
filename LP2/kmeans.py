
# coding: utf-8

# In[17]:


import traceback 
import numpy as np
import copy


# In[21]:


def kmeans(clusters,oldMeans): 
    final=[]
    #calculate distances
    try:
        flag=0
        print("",flag)
        
        while(flag==0):
            
            flag2=0
            if(len(oldMeans)!=0) :
                #check if old mean is equal to new mean
                for i in range(0,k):
                    print("Checking old and New Means",oldMeans[i][0],"\n",clusters[i][0],"i is : ",i)
                    if(oldMeans[i][0]!=clusters[i][0]):
                        flag2=1
                        break
            else :
                #if old mean lists is empty, ie first iteration case
                flag2=1
                
            print("Here",flag)
            
            if(flag2!=0) : 
                
                #record the old means
                oldMeans = copy.deepcopy(clusters)
                #print(hex(id(l)))

                #create the clusters
                for num in numbers :
                    min_dist=99999999
                    nearest_mean=0
                    for i in range(0,k):
                            #print(num)
                            dist=abs(clusters[i][0]-num)
                            if(min_dist>dist) :
                                min_dist=dist
                                nearest_mean=i

                            #print("min Dist ",min_dist)
                    if(num!=clusters[nearest_mean][0]) :
                        clusters[nearest_mean].append(num)
                        
                #calculate the means in each of the clusters     
                newMean=[]
                for i in range(0,k) :
                    avrg=sum(clusters[i])/ len(clusters[i])
                    newSublist=[]
                    newSublist.append(avrg)
                    newMean.append(newSublist)
                    
                #copy new means to clusters
                final=copy.deepcopy(clusters)
                clusters=[]
                clusters=newMean
            else :
                flag=1
                
        return final      
    except:
        print("error")
        traceback.print_exc()


# In[22]:


def main():
    try:
        # accepting the array as a list of integers
        size=int(raw_input("Enter total numbers"))
        numbers=[]
        for i in range(0,size) :
            num=int(raw_input("Enter next number"))
            numbers.append(num);
        print(numbers)
        print(numbers[1])

        # creating a numpy array of list objects
        k=int(raw_input("Enter total clusters"))
        clusters=np.empty((k,),dtype=np.object)

        #clusters=np.array()
        print(clusters)

        # selecting random mean values
        step=size/k
        ptr=0

        clusters = []
        oldMeans=[]
        
        #picking random numbers for initial mean values 
        for i in range(0,k):
            sublist = []
            for j in range(0,1):
                sublist.append(numbers[ptr])
                ptr=ptr+step
                clusters.append(sublist)

        print(clusters)
        print(oldMeans)
        
        #calculate the clusters
        print("Final Clusters are ",kmeans(clusters,oldMeans))
        
    except:
        print("error")
        traceback.print_exc()



# In[23]:


if __name__=="__main__":
    main()

