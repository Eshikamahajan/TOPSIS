# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 15:28:18 2020

@author: Eshika Mahajan
"""
import requests
import numpy as np
import pandas as pd

    
def topsis_exp1(filename,weight,impact):
    
    #   initialising empty arrays and lists 
    w=None
    i=None
    norm_Factor=None
    rank=None
    
    idealBest=[]
    idealWorst=[]
    
    
    #reading the csv
    df=pd.read_csv(filename)
    col_count=len(df.columns)
    col_count=(col_count-1)
    df = df.values[:,1:]
    
    #printing entered weight and impacts
    print(weight)
    print(impact)
    
    #converting list into array
    w=np.array(weight)
    i=np.array(impact)
    
    
    #getting col count for dataframe and enetered length of impact and weights
    
    weight_count=len(w)
    impact_count=len(i)
    
    #matching whether the enetered impacts and weights are equal to total col in daatframe or not
    if col_count==weight_count and col_count==impact_count:
        
        norm_Factor=np.sqrt(np.sum(df**2,axis=0,dtype=float),dtype=float)#calculating normaliseingfactor
        norm_Data=(df/norm_Factor)#normalising the dataframe
        norm_Data=np.round(norm_Data.astype(np.float64),decimals=2)#rounding to 2 decimal places
        wt_Norm_Data=norm_Data*w   #getting the weighted matrix
        
        
        #calculating the worst and the ideal value in every column i.e. V+ and V-
        for j in range(df.shape[1]):
            if i[j]==1:
                idealBest.append(max(wt_Norm_Data[:,j]))
                idealWorst.append(min(wt_Norm_Data[:,j]))
                
            if i[j]==0:
                idealBest.append(min(wt_Norm_Data[:,j]))
                idealWorst.append(max(wt_Norm_Data[:,j]))


#calcualting euclidian distance of every col from best and worst value
        S_best=np.sqrt(np.sum((wt_Norm_Data-idealBest)**2,axis=1,dtype=float),dtype=float)
        S_best=S_best.reshape(S_best.shape[0],-1)
        S_Worst=np.sqrt(np.sum((wt_Norm_Data-idealWorst)**2,axis=1,dtype=float),dtype=float)
        S_Worst=S_Worst.reshape(S_Worst.shape[0],-1)
        S=S_best+S_Worst
    
    
    #s_best and S_Worst are arrys
    
        performance=S_Worst/S  #formula for performance
        
        
        
        #sorting the performances array column wise and giving ranks on the basis of their order in the sorted array to the criteria
        order = performance.argsort(axis=0)
        rank = order.argsort(axis=0)
        rank=rank.reshape(rank.shape[0],)  # converting it into 1d array
    
        print("Item","Rank",sep="\t")
        for idx,x in enumerate(rank):
            print(idx+1,rank.shape[0]-(x),sep="\t",end="\n")   #printing criteria as well as  its rank
            
    else:
        print('range of weight or impact donot match the range of columns.' ) # if any error in entered weight and impact length



        
        