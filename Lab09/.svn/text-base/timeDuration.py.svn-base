#! /usr/bin/env python3.4

import os
import glob
import re
import sys

class TimeSpan:
    def __init__(self,weeks,days,hours):
        if(type(weeks) is not int or type(days) is not int or type(hours) is not int):
            raise TypeError
        if(weeks < 0 or days < 0 or hours < 0):
            raise ValueError
        self.hours = hours
        self.days = days
        self.weeks = weeks

        if(self.hours >= 24):
            mod_val = self.hours % 24
            floor_val = self.hours // 24

            self.days = self.days + floor_val
            self.hours = mod_val


        if(self.days >= 7):

            mod_val = self.days % 7
            floor_val = self.days // 7

            self.days = mod_val
            self.weeks = self.weeks + floor_val


    def __str__(self):
        ret_str = "{0:02d}W {1:01d}D {2:02d}H".format(self.weeks,self.days,self.hours)
        return ret_str

    def getTotalHours(self):
        return self.weeks * (7 * 24) + (self.days * 24) + self.hours

    def __add__(self,other):
        #weeks1 = 0
        #hours1 = 0
        #days1 = 0
        if(type(other) is not TimeSpan):
            raise TypeError

        else:

            weeks1 = self.weeks + other.weeks
            hours1 = self.hours + other.hours
            days1 = self.days + other.days

        temp = TimeSpan(weeks1,days1,hours1)

        return temp

    __radd__ = __add__

    def __mul__(self, other):
        weeks1 = 0
        hours1 = 0
        days1 = 0
        print(type(other))
        if(type(other) is not int):
            raise TypeError

        if(other <= 0):
            raise ValueError


        weeks1 = self.weeks * other
        hours1 = self.hours * other
        days1 = self.days *other

        temp = TimeSpan(weeks1,days1,hours1)

        return temp

    __rmul__ = __mul__









