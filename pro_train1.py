#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' '''

__author__ = 'Wang Junqi'

import numpy as np;
import csv;
import random;

f=open('train1.csv','rb');
csv_reader=csv.reader(f);
tittle=csv_reader.next();
all_list=[];
for row in csv_reader:
    all_list.append(row);
random.shuffle(all_list);
f.close();
f=open('rtrain1.csv','wb');
csv_writer=csv.writer(f);
csv_writer.writerow(tittle);
for row in all_list:
    csv_writer.writerow(row);
f.close();
