#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' '''

__author__ = 'Wang Junqi'

import csv;

f=open('train.csv','rb');
f1=open('train1.csv','wb');
f2=open('train2.csv','wb');
csv_reader=csv.reader(f);
tittle=csv_reader.next();
csv_write1=csv.writer(f1);
csv_write2=csv.writer(f2);
csv_write1.writerow(tittle);
csv_write2.writerow(tittle);
for row in csv_reader:
    if row[1]=='1':
        csv_write1.writerow(row);
    else:
        csv_write2.writerow(row);
f.close();
f1.close();
f2.close();

