# -*- coding: utf-8 -*-

import random


#分割 train.txt文件，分成  train_test.txt 和 train_train.txt
def splitDataSet(dataSet,M,k,seed):
    test=[]
    train=[]
    random.seed(seed)
    for line in dataSet:
        if random.randint(0,M)==k:
            test.append(line)
        else:
            train.append(line)
    return test,train


def startSplitTrain(src_file,testpath,trainpath,k):
    records=[]
    f=open(src_file,'r')
    for line in f.readlines()[1:]:
        records.append(line)
    
    test_part,train_part=splitDataSet(records,5,k,10)
    out=open(testpath,'w')
    for line in test_part[0:len(test_part)]:
        out.write('%s'%(line))
    
    out=open(trainpath,'w')
    for line in train_part[0:len(train_part)]:
        out.write('%s'%(line))
    
    print('test and train write completed')


startSplitTrain('~/talk.txt','~/train_test.txt',
                '~/train_train.txt',3)
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    