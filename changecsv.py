#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' '''

__author__ = 'Wang Junq'

import csv;

pre=33563901./6865066;
pre=1-pre/(pre+1);
f_init=open('l1005.csv','rb');
f_result=open('l1005-change.csv','wb');
csv_init=csv.reader(f_init);
csv_result=csv.writer(f_result);
tittle=csv_init.next();
csv_result.writerow(tittle);
for row in csv_init:
#   pre=float(row[1]);
#   if pre<0.25 and pre>0.11:
#       pre=0.1698;
#   elif pre>0.6:
#       pre=0.99;
#   elif pre>0.4:
#       pre=0.6;
#   elif pre>0.35:
#       pre=0.5;
    temp_list=[row[0],pre];
    csv_result.writerow(temp_list);
f_init.close();
f_result.close();
