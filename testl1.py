#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' '''

__author__ = 'Wang Junqi'

import csv;
import string;
import numpy as np;
import pickle;

def convert2vec(sample,title):
    result_dir={};
    click=string.atoi(sample[1]);
    day=sample[2][4:6];
    day=string.atoi(day)%7;
    result_dir['day'+str(day)]=1;
    hour=sample[2][-2:];
    result_dir['hour'+hour]=1;
    for i in xrange(3,24):
        result_dir[title[i]+','+sample[i]]=1;
    return result_dir,click;

def test2vec(sample,title):
    result_dir={};
    day=sample[1][4:6];
    day=string.atoi(day)%7;
    result_dir['day'+str(day)]=1;
    hour=sample[1][-2:];
    result_dir['hour'+hour]=1;
    for i in xrange(2,23):
        result_dir[title[i]+','+sample[i]]=1;
    return result_dir;

def sigmoid(pre):
    pre=1/(1+np.exp(-pre));
    return pre;

def logic_lose(pre,y):
    return -np.log(pre) if y==1 else -np.log(1-pre);

w={};
n={};
a=0.1;
b=33563901./6865066;
c=2;
l1_a=0.001;

for adsa in xrange(1):
    f_train=open('train.csv','rb');
    csv_operater = csv.reader(f_train);
    tittle=csv_operater.next();
    for t,row in enumerate(csv_operater):
        x_Dir,y=convert2vec(row,tittle);
        pre=0.0;
        for key in x_Dir.keys():
            if not w.has_key(key):
                w[key]=0.0;
                n[key]=1;
            else:
                pre+=w[key];
                n[key]+=1;
        pre=sigmoid(pre);
        for key in x_Dir.keys():
            if w[key]>0:
                theta=1;
            elif w[key]<0:
                theta=-1;
            else:
                theta=0;
            temp_a=a/(np.sqrt(n[key]));
            w[key]-=temp_a*(pre-y)+theta*temp_a*l1_a;
        if t%10000==0:
            print pre,y,t;
    f_train.close();
   
#f=open('__w','wb');
#pickle.dump(w,f);
#f.close();

f_test=open('test.csv','rb');
f_result=open('out0.01.csv','wb');
csv_writer=csv.writer(f_result);
csv_writer.writerow(['id','click']);
csv_operator=csv.reader(f_test);
tittle=csv_operator.next();
for row in csv_operator:
    temp_id=row[0];
    x_Dir=test2vec(row,tittle);
    pre=0.0;
    for key in x_Dir.keys():
        if w.has_key(key):
            pre+=w[key];
    pre=sigmoid(pre);
    csv_writer.writerow([temp_id,pre]);
f_result.close();
f_test.close();
