#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' '''

__author__ = 'Wang Junqi'

import string;
import random;
import numpy as np;
import csv;
import pickle;

def String_hashB(s):
    seed=13131313;
    haxi=0;
    for x in s:
        haxi+=ord(x)*seed+ord(x);
    haxi=haxi & int('7fffffff',16);
    return haxi;

def String_hashS(s):
    seed=1313;
    haxi=0;
    for x in s:
        haxi=haxi*seed+ord(x);
    haxi=haxi & int('7fffffff',16);
    return haxi;

def convert2vec(sample,scale_list):
    temp_list=[1];
    click=sample[1];
    hour=sample[2];
    temp_list.append(string.atoi(hour[-2]));
    for x in sample[3:-8]:
        temp_list.append(String_hashS(x));
    for x in sample[-8:]:
        temp_list.append(string.atoi(x));
    temp_list=np.array(temp_list);
    temp_list=1.0*temp_list/(10**scale_list);
    #print temp_list;
    return temp_list,string.atoi(click);

#w(d,1) x(n,d)
def logic_lose(w,x,y):
    pre_y=sigmoid(x.dot(w));
    result=10*y*np.log(pre_y)+(1-y)*np.log(1-pre_y);
    return -np.sum(result)/x.shape[0];

def sigmoid(pre):
    pre=1/(1+np.exp(-pre));
    pre[1-pre<0.00000001]-=0.00000001;
    pre[pre-0<0.00000001]+=0.00000001;
    return pre;
np.set_printoptions(threshold='nan');
flag=1;
init_w=np.random.rand(23,1);
scale_list=[0,1,8,8,9,9,8,9,8,8,8,8,8,8,8,4,2,1,3,0,1,5,1];
a=0.00001;
inc_ratio=1.07;
dec_ratio=0.93;
scale_list=np.array(scale_list);
f_train=open('train.csv','rb');
#csv_operator=csv.reader(f_train);
#csv_operator.next();
f_train.readline();
x=f_train.readline();
i_num=1;
while 1:
    matrix_x=[];
    matrix_y=[];
    for i in xrange(100000):
        if x:
            row=x.split(',');
            temp_list,temp_y=convert2vec(row,scale_list);
            matrix_x.append(temp_list);
            matrix_y.append(temp_y);
            x=f_train.readline();
        else:
            flag=0;
            break;
    matrix_x=np.array(matrix_x);#(n,d+1)
    matrix_y=np.array(matrix_y).reshape(matrix_x.shape[0],1);#(n,1)
    pre=sigmoid(matrix_x.dot(init_w));
    temp_decent=-(matrix_x.T).dot(2*matrix_y-pre-1*pre*matrix_y);
    #print pre;
    while 1:
        old_cost=logic_lose(init_w,matrix_x,matrix_y);
        init_cost=old_cost;
        new_cost=logic_lose(init_w-a*temp_decent,matrix_x,matrix_y);
        if new_cost>old_cost:
            while new_cost>old_cost:
                a*=dec_ratio;
                new_cost=logic_lose(init_w-a*temp_decent,matrix_x,matrix_y);
        init_w-=a*temp_decent;
        new_cost=logic_lose(init_w,matrix_x,matrix_y);
        print new_cost,i_num,old_cost,a;
        if old_cost-new_cost<0.00000000001*i_num:
            break;
#        if new_cost>old_cost:
#            init_w+=(a/(i_num*10000))*temp_decent;
#            break;
#        if old_cost-new_cost<0.0000000001*i_num:
#            break;
    i_num+=1;
    if not flag:
        break;
f=open('__w','wb');
pickle.dump(init_w,f);
f.close();
