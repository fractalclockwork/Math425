#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 21:20:00 2021

@author: hboateng
"""
class hwone:
    def tuple_sum(A,B):
        """
        input: lists A and B of the same length, where each element in each
               list is a pair (x,y) of numbers
        output: list of pairs (x,y) in which the first element of the ith
                pair is the sum of the first element of the ith pair in
                A and the first element of the ith pair in B. Similarly, the
                second element of the ith pair is the sum of the second
                element of the ith pair of A and the second element of the 
                ith pair in B.
                Example: Given lists A = [(1,2), (10,20)] and 
                         B = [(3,4), (30,40)], tuple_sum(A,B) 
                         returns [(4,6), (40,60)]
        """
        pass
    
    def inv_dict(d):
        """
        input: dictionary d representing an invertible function
        output: dictionary representing the inverse of f, the returned
                dictionary's keys are the values of d and its values are the
                keys of d
        Example: Given d = {'thank you': 'merci', 'goobye': 'au revoir'} ,
                 inv_dict(d) returns 
                 {'merci': 'thank you', 'au revoir': 'goobye'} 

        """
        pass
    
    def myUnion(L):
        """
        input : list of sets
        output: A set which is the union of all sets in L

        Example: Given L=[{1,2}, {'A','B'}], myUnion(L) returns
                 {'A','B',1, 2}

        """
        current = ... # Fill in here
        for x in L:
            current = ... # Fill in here
        return current
    
    def transform(a,b, L):
        """
        input: complex numbers a and b, and a list L of complex numbers
        output: the list of complex numbers obtained by applying
                f(z) = az + b to each complex number in L
                
        Example: if a = i, b = -i and L = [1+i, 1-i], transform(a,b, L)
                 returns [i*(1+i)-i, i*(1-i)-i] = [-1,1]
        """
        pass
