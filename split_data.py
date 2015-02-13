#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' '''

__author__ = 'Wang Junqi'

import csv;

day_dict={};
f=open('train.csv','rb');
csv_o=csv.reader(f);
csv_o.next();
f_w=0;
csv_w=0;
for row in csv_o:
    time=row[2];
    day=time[4:6];
    if not day_dict.has_key(day):
        day_dict[day]=True;
        f_w=open(day+'.csv','wb');
        csv_w=csv.writer(f_w);
    csv_w.writerow(row);
