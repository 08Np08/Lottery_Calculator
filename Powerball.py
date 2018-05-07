#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 10:25:12 2018

@author: Nik
"""
#lotto prob

file = open("lottonum.txt","r")

num_dict = {}
lotto_dict = {}
freq_dict = {}

def main():
    count = 0

    for line in file:
        line = line.strip("\n")
        line = line.strip(',')
        line = line.split(" ")

        lotto_dict[count] = line
        num_dict[count] = line
        count += 1


    for i in lotto_dict:
        for j in lotto_dict[i]:
            if j not in freq_dict:
                freq_dict[j] = 0

    for i in lotto_dict:
        for j in lotto_dict[i]:
            freq_dict[j] += 1
            
    powerball_frequency()
    print()
    main_num_frequency()
    print()
    bottom_ten()
    print()
    top_ten()
    print()
    most_due() 


def most_due():
    time_dict = {}
    count = 0
    for i in lotto_dict:
        count += 1
        for j in lotto_dict[i]:
            time_dict[j] = count

    most_due = []
    sort_num = 1000
    sort_value = 1000
    time_dict2 = time_dict.copy()

    for i in range(10):
        for j in time_dict2:
            x = time_dict2[j]
            if x < sort_num:
                sort_value = j
                sort_num = x
            
        most_due.append(sort_value)
        time_dict2.pop(str(sort_value))
        sort_num = 1000
        sort_value = 1000
    
    print("   Most Due")
    print("Place \t Number")
    x = 1
    for i in most_due:
        print(x,"\t",i)
        x += 1 
        
def top_ten():       
        
    top_ten = []
    sort_num = 0
    sort_value = 0
    freq_dict2 = freq_dict.copy()

    for i in range(10):
        for j in freq_dict2:
            x = freq_dict2[j]
            if x > sort_num:
                sort_value = j
                sort_num = x
            
        top_ten.append(sort_value)
        freq_dict2.pop(str(sort_value))
        sort_num = 0
        sort_value = 0
    
    print("    Top Ten")  
    print("Number \t Frequency")
    for i in top_ten:
        print(i,"\t",freq_dict[i])
        
def bottom_ten():
    bottom_ten = []
    sort_num = 1000
    sort_value = 1000
    freq_dict3 = freq_dict.copy()


    for i in range(10):
        for j in freq_dict3:
            x = freq_dict3[j]
            if x < sort_num:
                sort_value = j
                sort_num = x
            
        bottom_ten.append(sort_value)
        freq_dict3.pop(str(sort_value))
        sort_num = 1000
        sort_value = 1000
        
    print("  Bottom Ten")  
    print("Number \t Frequency")
    for i in bottom_ten:
        print(i,"\t",freq_dict[i])

def main_num_frequency():
    count = 0
    nums_dict = {}
    for i in num_dict:
        for j in num_dict[i]:
            if j not in nums_dict:
                nums_dict[j] = 0

                
    for i in num_dict:
        for j in num_dict[i]:
            if count == 5:
                break
            nums_dict[j] += 1
            count += 1
        count = 0    
    print("1-69 Number Frequency")
    print("Number \t Frequency")
    for i in nums_dict:   
        print(i,"\t",nums_dict[i])
    
def powerball_frequency():
    count = 0
    nums_dict = {}
    
    for i in num_dict:
        for j in num_dict[i]:
            if j not in nums_dict:
                nums_dict[j] = 0
              
    for i in num_dict:
        for j in num_dict[i]:
            if count < 5:
                count += 1
                continue
            nums_dict[j] += 1
            count += 1
        count = 0
    
    nums1_dict = nums_dict.copy()
    
    for i in nums1_dict:
        if nums_dict[i] == 0:
            del nums_dict[i]
    
    nums1_dict = nums_dict.copy()
    print("Powerball Frequency")
    print("Number \t Frequency")
    for i in nums_dict:   
        print(i,"\t",nums_dict[i])
        

main()
file.close()
