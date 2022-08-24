#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 21:20:00 2021

@author: hboateng
"""
from vecutil import list2vec, vec2list
from statistics import mean

class hwtwo:
    def create_voting_dict(strlist):
        """
        Input: a list of strings.  Each string represents the voting record of a senator.
               The string consists of 
                  - the senator's last name, 
                  - a letter indicating the senator's party,
                  - a couple of letters indicating the senator's home state, and
                  - a sequence of numbers (0's, 1's, and negative 1's) indicating the senator's
                    votes on bills
                  all separated by spaces.
        Output: A dictionary that maps the last name of a senator
                to a list of numbers representing the senator's voting record.
        Example: 
            >>> vd = create_voting_dict(['Kennedy D MA -1 -1 1 1', 'Snowe R ME 1 1 1 1'])
            >>> vd == {'Snowe': [1, 1, 1, 1], 'Kennedy': [-1, -1, 1, 1]}
            True
    
        You can use the .split() method to split each string in the
        strlist into a list; the first element of the list will be the senator's
        name, the second will be his/her party affiliation (R or D), the
        third will be his/her home state, and the remaining elements of
        the list will be that senator's voting record on a collection of bills.
    
        You can use the built-in procedure int() to convert a string
        representation of an integer (e.g. '1') to the actual integer
        (e.g. 1).
    
        The lists for each senator should preserve the order listed in voting data.
        In case you're feeling clever, this can be done in one line.
        """
        return {sen.split()[0]:[int(k) for k in sen.split()[3:]] for sen in strlist}
    
    def policy_compare(sen_a, sen_b, voting_dict):
        """
        Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
               names to lists representing their voting records.
        Output: the dot-product (as a number) representing the degree of similarity
                between two senators' voting policies
        Example:
            >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
            >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
            -2
        
        The code should correct compute dot-product even if the numbers are not all in {0,1,-1}.
            >>> policy_compare('A', 'B', {'A':[100,10,1], 'B':[2,5,3]})
            253
            
        You should definitely try to write this in one line.
        """
        return list2vec(voting_dict[sen_a])*list2vec(voting_dict[sen_b])

    def most_similar(sen, voting_dict):
        """
        Input: the last name of a senator, and a dictionary mapping senator names
               to lists representing their voting records.
        Output: the last name of the senator whose political mindset is most
                like the input senator (excluding, of course, the input senator
                him/herself). Resolve ties arbitrarily.
        Example:
            >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
            >>> most_similar('Klein', vd)
            'Fox-Epstein'
            >>> vd == {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
            True
            >>> vd = {'a': [1,1,1,0], 'b': [1,-1,0,0], 'c': [-1,0,0,0], 'd': [-1,0,0,1], 'e': [1, 0, 0,0]}
            >>> most_similar('c', vd)
            'd'
    
        Note that you can (and are encouraged to) re-use your policy_compare procedure.
        """
        
        # This is not the most obvious way. Just being a tad silly.
        comp_dict = {hwtwo.policy_compare(sen,sen2,voting_dict):sen2 
                     for sen2 in voting_dict.keys() if sen != sen2 }
        
        return comp_dict[max(comp_dict)]
    
    def least_similar(sen, voting_dict):
        """
        Input: the last name of a senator, and a dictionary mapping senator names
               to lists representing their voting records.
        Output: the last name of the senator whose political mindset is least like the input
                senator.
        Example:
            >>> vd = {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
            >>> least_similar('a', vd)
            'c'
            >>> vd == {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
            True
            >>> vd = {'a': [-1,0,0], 'b': [1,0,0], 'c': [-1,1,0], 'd': [-1,1,1]}
            >>> least_similar('c', vd)
            'b'
        """
        # This is not the most obvious way. Just being a tad silly.
        comp_dict = {hwtwo.policy_compare(sen,sen2,voting_dict):sen2 
                     for sen2 in voting_dict.keys() if sen != sen2 }
        
        return comp_dict[min(comp_dict)]
    
    def find_average_similarity(sen, sen_set, voting_dict):
        """
        Input: the name of a senator, a set of senator names, and a voting dictionary.
        Output: the average dot-product between sen and those in sen_set.
        Example:
            >>> vd = {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
            >>> sens = {'Fox-Epstein','Ravella','Oyakawa','Loery'}
            >>> find_average_similarity('Klein', sens, vd)
            -0.5
            >>> sens == {'Fox-Epstein','Ravella', 'Oyakawa', 'Loery'}
            True
            >>> vd == {'Klein':[1,1,1], 'Fox-Epstein':[1,-1,0], 'Ravella':[-1,0,0], 'Oyakawa':[-1,-1,-1], 'Loery':[0,1,1]}
            True
        """
        return mean([hwtwo.policy_compare(sen,sen2,voting_dict) for sen2 in sen_set])
       
    
    def find_average_record(sen_set, voting_dict):
        """
        Input: a set of last names, a voting dictionary
        Output: a vector containing the average components of the voting records
                of the senators in the input set
        Example: 
            >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
            >>> senators = {'Fox-Epstein','Ravella'}
            >>> find_average_record(senators, voting_dict)
            [-0.5, -0.5, 0.0]
            >>> voting_dict == {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
            True
            >>> senators
            {'Fox-Epstein','Ravella'}
            >>> d = {'c': [-1,-1,0], 'b': [0,1,1], 'a': [0,1,1], 'e': [-1,-1,1], 'd': [-1,1,1]}
            >>> find_average_record({'a','c','e'}, d)
            [-0.6666666666666666, -0.3333333333333333, 0.6666666666666666]
            >>> find_average_record({'a','c','e','b'}, d)
            [-0.5, 0.0, 0.75]
            >>> find_average_record({'a'}, d)
            [0.0, 1.0, 1.0]
        """
        
       # return list(((sum([list2vec(voting_dict[sen]) for sen in sen_set])/
       #         float(len(sen_set))).f).values())
        
        return vec2list(sum([list2vec(voting_dict[sen]) for sen in sen_set])/
                float(len(sen_set)))
      
    
    def bitter_rivals(voting_dict):
        """
        Input: a dictionary mapping senator names to lists representing
               their voting records
        Output: a tuple containing the two senators who most strongly
                disagree with one another.
        Example: 
            >>> voting_dict = {'Klein':[-1,0,1], 'Fox-Epstein':[-1,-1,-1], 'Ravella':[0,0,1], 'Oyakawa':[1,1,1], 'Loery':[1,1,0]}
            >>> br = bitter_rivals(voting_dict)
            >>> br == ('Fox-Epstein', 'Oyakawa') or br == ('Oyakawa', 'Fox-Epstein')
            True
        """    
        most_bitter_sen = sorted({ sen:hwtwo.policy_compare(sen, (hwtwo.least_similar(sen, voting_dict)), voting_dict) for sen in voting_dict}.items(), key= lambda x:x[1])[0][0]
        return (most_bitter_sen, hwtwo.least_similar(most_bitter_sen, voting_dict))


#%% TEST CASE
#f = open('US_Senate_voting_data_109.txt')
#senvoterec = list(f)
#votdict = hwtwo.create_voting_dict(senvoterec)
#br = hwtwo.bitter_rivals(votdict)
voting_dict = {'Klein':[-1,0,1], 'Fox-Epstein':[-1,-1,-1], 'Ravella':[0,0,1], 'Oyakawa':[1,1,1], 'Loery':[1,1,0]} 
br = hwtwo.bitter_rivals(voting_dict)

    

