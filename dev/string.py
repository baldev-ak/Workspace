# def minion_game(string):
#     vowels = 'AEIOU'
#     Stuart_score, Kevin_score = 0, 0
#     length = len(string)
#     for start_idx in range(length):
#         score = length - start_idx
#         if string[start_idx] in vowels:
#             Kevin_score += score
#         else:
#         	Stuart_score += score
#     if Stuart_score == Kevin_score:
#         print('Draw')
#     if Stuart_score > Kevin_score:
#         print('Stuart {}'.format(Stuart_score))
#     if Stuart_score < Kevin_score:
#         print('Kevin {}'.format(Kevin_score))

# minion_game('BANANA')

# def merge_the_tools(s, k):
#     length = len(s)
#     t = 0
#     t1 = k
#     temp = []
#     if length % k != 0 :
#         print("--------Can't convert into sub-string---------")
#     else:
#         for i in range(t,k):
#             temp.append(s[i])
#             t+=k
#             k=k+t
#         print(temp)



# if __name__ == '__main__':
#     s, k = input(), int(input())
#     merge_the_tools(s, k)


# if __name__ == '__main__':
#     N = int(input())
#     arr = []
    
#     for i in range(N):
#         s = input().split()
        
#         #/****************************************************/

#         if s[0] == 'append' and len(s) == 2:
#             a = int(s[1])
#             arr.append(a)

#         elif s[0] == 'insert' and len(s) == 3:
#             index = int(s[1])
#             value = int(s[2])
            
#             arr.insert(index,value)

#         elif s[0] == 'remove' and len(s) == 2:
#             value = int(s[1])
#             arr.remove(value)

#         elif s[0] == 'print' and len(s) == 1:
#             print(arr)

#         elif s[0] == 'sort' and len(s) == 1:
#             arr.sort()

#         elif s[0] == 'reverse' and len(s) == 1:
#             arr.reverse()

#         elif s[0] == 'pop' and len(s) == 1:
#             length = len(arr)
#             arr.pop(length-1)
    
# def print_full_name(first, last):
#     # Write your code here
#     print("Hello "+ first + " " + last +"! You just delved into python.")
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for i in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     for name,marks in student_marks.items():
#         if query_name == name and len(marks) == 3:
#             total = 0
#             for i in marks:
#                 total = total +i
#             average = total / 3
#             print(average)
#             print("%.2f" % average)

# if __name__ == '__main__':
#     arr = []
#     score_list = []
#     name_list = []
#     for i in range(int(input())):
#         name = input()
#         score = float(input())
#         mylist = [name,score]
#         arr.append(mylist)
#         score_list.append(score)
#     # length = len(arr)    
#     score_l = sorted(list(set(score_list)))[1]
#     print(score_l)
#     arr.sort()

#     for name,score in arr:
#         if score == score_l:
#             print(name)
        

    # print(arr)
    # print(score_list)

# def mutate_string(string, position, character):
#     l = list(string)
#     l[position] = character
#     string = ''.join(l)   
#     return string

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# def count_substring(string, sub_string):
#     # print(string, sub_string)
#     length_sub = len(sub_string)
#     values = []
#     for i in range(0, len(string)):
#         x = slice(i, length_sub)
#         values.append(string[x])
#         length_sub+=1
#     x = values.count(sub_string)
#     return x

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)

# if __name__ == '__main__':
    # s = input()
    
    # print(True in list(map(lambda x: x.isalnum(),s)))
    # print(True in list(map(lambda x: x.isalpha(),s)))
    # print(True in list(map(lambda x: x.isdigit(),s)))
    # print(True in list(map(lambda x: x.islower(),s)))
    # print(True in list(map(lambda x: x.isupper(),s)))

# import textwrap

# def wrap(string, max_width):
#     # print(string)
#     # print(max_width)
#     start = 0
#     result = ''
#     for i in range(0,len(string)+1,max_width):
#         a = string[i:i+max_width]
#         if len(string)==max_width:
#             print(a)
#         else:
#             return a

#     # return

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)

# Student ID → ___1_____2_____3_____4_____5__               
# Subject 1   |  89    90    78    93    80
# Subject 2   |  90    91    85    88    86  
# Subject 3   |  91    92    83    89    90.5
#             |______________________________
# Average        90    91    82    90    85.5 


# def solution(sub, student):
#     mylist = []
#     for i in range(student):
#         mylist.append(map(float,input().split()))
#     for j in zip(*mylist):
#         print(sum(j))

# if __name__ == '__main__':
#     sub, student = map(int,input().split())
#     s_new = solution(sub, student)


# if __name__ == '__main__':
#     n = int(input())
#     print(sorted(list(map(int, input().split())))[-2])


# Enter your code here. Read input from STDIN. Print output to STDOUT

# n = int(input())
# a = list(map(int,input().split()))
# no = int(input())
# b = list(map(int,input().split()))

# print(len(set(a).difference(b)))

# def average(arr):
#     a = set(arr)
#     return sum(a)/len(a)

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the time_delta function below.
# def time_delta(t1, t2):
#     t =t1 -t2 
#     print(t.total_seconds())
# if __name__ == '__main__':
#     t = int(input())

#     for t_itr in range(t):
#         t1 = input()

#         t2 = input()

#         delta = time_delta(t1, t2)

# for i in range(int(input())):
#     try:
#         a,b = input().split()
#         print(int(a)//int(b))
#     except ZeroDivisionError as e:
#         print("Error Code:",e)
#     except ValueError as v:
#         print("Error Code:",v)

# def missing_integer(nums):
#     if all(i>1 for i in nums)==True and (i!=0 for i in nums):
#         return 1

#     elif all(i<1 for i in nums)==True:
#         return 1

#     else:
#         nums.sort()
#         a = min(nums)
#         b = max(nums)

#         mylist = []
#         for i in nums:
#             for j in range(a,b+1):
#                 mylist.append(j)
                
#         a = (sorted(list(set(mylist).difference(nums)))[0])
#         return a





# nums = [-55]

# print(missing_integer(nums))
# from itertools import permutations

# s, k =  input().split()

# x = list(permutations(s,int(k))) 

# x = sorted(x)
# print(x)

# for i in x:
#     print(*i,sep="")

# from itertools import combinations_with_replacement

# s, k = input().split()
# for i in range(1,int(k)+1):
#     for j in combinations_with_replacement(sorted(s),i):
#         print(''.join(j))
# from itertools import groupby
# for key, group in groupby(input()):
#    print('({}, {})'.format(len(list(group)), key), end=" ")

# s=set()

# for i in range(int(input())):
#     s.add(input())
# print(len(s))

# n = int(input())
# s = set(map(int, input().split()))

# for i in range(int(input())):
#     a = input().split()
    
#     if a[0] == 'pop':
#         s.pop()
    
#     elif a[0] == 'discard' and len(a) == 2:
#         s.remove(a[1])
    
#     elif a[0] == 'remove' and len(a) == 2:
#         s.discard(a[1])

# print(sum(s))     

# n = int(input())
# eng = set(map(int, input().split())) 
# N = int(input())
# fr = set(map(int, input().split()))    

# print(len(eng.union(fr)))

# n = int(input())
# A = set(map(int, input().split()))
# N = int(input())


# cube = lambda x: x**3# complete the lambda function 

# def fibonacci(n):
#     # return a list of fibonacci numbers
#     a,b = 0,1
#     count = 0
#     mylist = []
#     if n<= 0:
#         return mylist
#     elif n == 1:
#         mylist.append(a)
#         return mylist
#     else:
#         while count< n:
#             mylist.append(a)
#             result = a + b
#             a = b
#             b = result
#             count+=1
#         return mylist
# if __name__ == '__main__':
#     n = int(input())
#     print(list(map(cube, fibonacci(n))))
    # fibonacci(n)

# Enter your code here. Read input from STDIN. Print output to STDOUT
# ui = input().split()
# x = int(ui[0])
# print(eval(input()) == int(ui[1]))



# print([]*3)
# print(('a','b','c')*2)
# print((2)**2)
# print([{}]*2)
# print({3:1}*2)
# print((2,4)**2)



# mylist = [[-1],[2,3],[1,-1,-3]]
# for i in reversed(range(len(mylist))):
#     li = []
#     length = len(mylist[i])
#     # print(length)
#     for j in range(length-1):
#         a = mylist[i][j]
#         b = mylist[i][j+1]
#         x = min(a,b)
#         li.append(x)
#             # print("a")
#         for k in range(len(li)):
#             total = mylist[k+1][k]+ li[k]
                
#     print(total)

# strs = ["flower","flow","flight"]

# # for i in strs:
# #     x = i.startswith(i[0])
# #     print(x)
# for i in zip(*strs):



# arr = [-732,-376,-459,457,-772,762,-182,807,-956,-855,648,714,-476,-491,-935,643,106,407,-600,-46,-192,848,936,646,880,970,964,-336,175,-656,506,78,374,983,-180,266,22,61,41,103,-558,951,-465,15,730,-675,733,-304,429,-435,411,-841,45,308,174,-629,365,62,-984,879,-91,-393,986,-105,-578,-283,-42,-874,-841,-415,-477,-68,688,-692,-932,-389,636,222,635,-157,778,-738,-473,55,908,-109,-238,86,-77,362,948,116,-291,395,-978,-773,-820,-990,485,-458,-153,-783,-840,688,656,-488,146,962,314,390,612,-607,544,456,457,-348,710,80,848,-844,488,706,-914,613,-824,190,-499,415,754,-303,-533,-738,770,-334,649,516,-101,154,-636,-724,-811,-506,876,-27,-836,-970,141,-908,-761,-78,367,-725,-454,821,536,-736,-295,535,520,628,751,-353,541,111,180,-893,264,98,-207,48,999,234,-468,-400,957,-365,346,-136,748,-353,991,336,825,808,556,412,-754,-627,407,897,481,207,37,969,741,751,-780,-409,225,-244,610,486,591,-270,379,577,-871,-782,-20,803,-449,173,246,962,-187,-332,-66,-730,102,663,205,403,824,-89,-422,-421,-437,842,-622,304,-769,105,740,-942,884,-507,-742,443,-262,-966,852,742,770,98,-344,-410,-378,24,-863,729,-488,-555,29,-968,231,-480,722,-31,156,397,562,-683,686,-747,42,-323,891,-813,-718,-749,432,-788,785,638,823,801,220,-912,224,648,9,728,-515,334,253,-385,-774,680,-178,-833,-33,-904,-752,956,-253,-546,-740,875,661,545,440,-904,199,-806,-131,324,627,-700,538,365,-394,378,-7,-525,-181,-23,978,-565,-208,785,292,337,416,676,273,-647,-875,-311,815,270,597,994,55,-574,210,221,9,521,548,130,92,-457,-431,-555,58,650,-562,-62,-989,-198,67,360,783,679,474,-692,-571,83,41,442,195,453,187,-874,-57,854,44,959,410,-63,805,-985,57,-982,606,-910,393,-122,-755,525,-469,-159,-357,-413,-274,-559,6,967,-396,-50,-498,504,-363,-239,97,434,26,894,-351,-673,578,289,-401,964,703,-231,70,797,-775,647,738,-344,423,-704,-29,652,230,-149,-101,-282,-258,-50,559,492,-151,832,-199,878,30,570,-262,-639,842,-243,-713,-985,-884,-589,-351,-303,873,-636,363,-24,10,-730,461,338,348,-158,-538,-494,-348,405,-985,-328,-433,-951,704,717,-571,545,468,799,545,-398,843,-459,-488,427,-170,-700,-996,980,817,338,-958,124,-529,-894,-833,-419,774,-132,298,508,-703,267,212,320,-840,579,990,-533,531,612,664,535,-677,-631,-488,-505,-848,-919,740,130,483,-833,-565,-614,745,-643,-922,885,618,-820,-414,-686,989,-862,-673,363,-712,-822,-219,273,650,-381,-798,732,616,-996,115,-412,636,821,-310,534,-913,-922,-797,127,482,-741,39,509,565,987,-592,-228,-428,411,-566,644,743,440,441,-765,-682,-742,487,587,-920,212,-44,495,-473,-675,566,103,472,900,401,-950,-595,-480,-912,-28,311,-258,423,-72,-980,-664,718,636,838,158,-260,802,63,-735,334,-145,896,331,523,57,-62,575,4,974,-932,-614,121,17,-152,-574,-313,654,-192,-939,-547,758,-361,635,531,-558,814,391,-65,-540,732,53,-742,-824,57,-556,525,-798,600,844,-206,-73,-656,879,968,444,248,20,338,-810,-291,729,-768,-937,169,-625,-171,733,823,-377,359,-701,548,132,167,193,542,223,-725,662,-703,190,172,224,-728,-611,910,-813,-456,445,593,488,578,366,227,-478,911,-2,574,-376,312,-179,863,975,-817,-388,588,-886,-972,964,281,-350,94,850,-848,-422,-142,481,369,-830,777,675,-842,840,44,213,629,858,-760,302,829,547,923,117,-298,80,-572,649,-702,-637,-550,789,-142,-707,449,-281,919,144,-628,953,-218,-125,507,347,607,-999,-838,-142,-875,-953,-763,-729,912,657,-617,-765,-386,177,78,-336,76,-509,-937,65,-773,-607,386,-603,-171,-916,-811,187,-19,463,-237,633,627,-901,235,-630,-839,-847,208,129,130,968,-945,593,-195,-770,-507,106,56,-266,912,-483,448,-949,238,-41,-474,448,-105,-386,79,132,-224,-885,156,-193,-815,692,-138,-731,-783,-182,676,37,179,544,-426,664,-186,509,-976,-219,-880,458,497,-591,-500,264,-526,-967,162,-605,971,-641,-366,-278,903,512,-756,-957,798,795,998,-812,-796,947,-282,944,952,259,989,722,-862,927,240,-82,725,753,-941,-928,-613,600,333,328,-330,591,-345,-694,-979,-829,-975,72,-188,242,74,408,-143,-633,163,-285,985,-556,-481,-618,679,-316,968,544,378,845,-98,940,-143,945,-42,277,-744,-520,-847,168,-427,601,-644,898,843,-21,-258,126,793,-9,154,454,840,700,837,867,457,774,-81,9,-500,-989,156,832,-361,-579,697,754,-912,-178,304,949,-305,-463,-139,507,111,-697,787,80,-268,-140,961,83,958,-700,78,720,155,-265,-595,948,617,603,-5,-314,561,546,888,-153,278,-304,424,-925,125,-565,-731,205,-59,363,-872,-814,-630,899,905,-221,464,-723,748,-108,-258,-877,680,244,-472,-532,211,-554,-519,305,-334,896,627,-972,117,465,639,193,-785,-2,555,-137,-318,-977,432,-279,-166,72,3,-312,-605,800,-303,417,732,-628,661,-530,628,-343,8,-259,23,728,833,-759,-142,-539,682,-973,393,7,-762,-71,304,958,225,907,533,-168,140,16,-852,-784,428,543,-268,64,247,-656,260,796,914,-912,-107,-605,-440,-22,-248,-638,-716,621,-454,600,621,-352,-311,227,903,-326,-961,-512,-819,-365,391,737,-331,-790,-599,381,172,817,573,996,-495,651,643,-896,559,-10,-137,-553,-628,-750,-91,-502,-140,506,737,178,195,-732,-807,-414,-725,-864,479,897,955,545,655,-32,-949,969,-688,-82,-576,426,-479,-608,-379,287,-44,219,937,62,744,586,-594,85,-896,-355,918,370,939,944,-990,-897,811,-4,-782,-714,266,531,-636,-116,-950,718,-876,372,-483,965,-600,188,916,220,11,996,645,889,-307,-292,-788,-437,888,-300,-869,101,891,452,912,-876,355,451,944,49,244,-512,528,-876,221,-267,-544,-689,-838,160,522,-406,-75,-38,-744,-980,145,-769,-457,-77,-462,-302,795,-267,267,379,533,545,674,126,-105,-478,-75,456,-115,-529,-267,-311,595,-873,812,-206,-389,573,457,370,-558,-587,-983,-643,404,-435,590,-683,-324,-57,-871,473,451,-342,330,557,479,729,956,-712,3,868,-733,-110,-438,334,-226,346,83,-690,80,65,-397,-791,-876,555,293,144,470,872,424,-809,-187,816,757,-82,-964,-711,-735,934,-962,-488,136,-444,72,-653,-533,984,77,-28,-992,-2,-925,-4,972,247,814,612,-857,-180,344,135,41,-315,103,-526,722,636,314,612,928,-706,397,615,875,-113,-761,-684,685,-757,-345,-451,886,-149,621,980,428,547,482,-199,-887,73,-545,603,298,-881,-342,105,490,164,-932,471,762,-299,172,242,446,508,-349,-218,-385,397,411,851,-969,-243,-665,78,308,-8,-218,718,578,-447,541,-414,-192,-196,264,336,-35,-683,-297,-528,31,-807,497,-689,-155,926,-944,-453,-210,304,171,675,-814,-403,-579,203,799,-59,-350,-941,-858,-495,410,-309,930,331,-696,-643,-533,-6,-721,-445,881,157,-339,410,-346,61,-711,537,-433,276,372,-828,-145,345,448,-9,102,555,-364,920,-210,-279,317,741,-957,-529,7,332,258,-988,16,690,-663,-86,204,-68,479,20,-237,-773,-528,-52,418,-562,285,-321,-888,-398,-446,-199,909,271,-420,-27,-398,-855,184,-906,-236,207,941,-677,-190,-735,-251,-539,-225,-649,31,-89,721,-418,198,382,82,814,-853,389,-946,-960,-770,-107,-365,-9,-725,-709,-115,-525,-255,-51,490,450,981,398,-855,-138,433,318,919,-729,-33,251,-689,810,-957,813,-423,-713,877,-659,-689,847,429,-914,562,768,-862,516,267,-395,-953,-779,509,-385,628,998,-340,-350,-994,-401,502,-808,436,271,-394,-250,203,-326,-544,663,657,984,-195,-252,621,-547,-592,467,-124,213,-93,-36,-363,654,485,-691,720,-39,-547,752,-805,-179,-461,-135,475,643,716,989,-262,547,-234,444,700,695,-710,883,975,953,493,89,964,-205,-630,-985,-298,80,-364,-272,592,-999,-681,-923,-370,-63,909,-406,-967,447,-263,620,606,-982,379,627,379,-305,0,643,-812,-681,703,163,559,411,-21,546,152,-671,647,-130,13,-357,-26,167,-7,392,508,832,507,-19,-314,197,591,-569,-230,395,380,691,-227,-988,842,424,926,524,593,-780,-219,948,-280,760,-112,830,239,169,-930,548,117,-418,902,61,-868,897,826,628,172,-561,-259,481,-171,473,-909,543,-81,-137,268,-758,-601,751,116,797,-680,478,773,-554,244,23,-53,54,997,-254,614,3,649,-62,-121,-3,284,-513,474,861,777,-636,-511,580,-915,-219,261,224,565,154,332,515,-330,-384,227,389,-600,-243,715,603,733,11,200,318,524,-785,-426,-529,-990,-364,835,-956,75,-844,324,-542,701,571,824,360,-209,-1,-201,-200,-84,489,925,704,-498,-257,653,-140,-408,-249,888,-299,-685,-156,-580,737,366,-875,-625,-836,620,624,146,41,316,138,-386,926,566,-723,791,657,-217,850,23,614,-551,565,-486,-745,746,86,316,26,-84,500,312,345,-620,-992,552,-268,442,179,-424,-621,-901,110,-893,-334,477,-462,233,516,-261,931,521,-610,535,319,-230,-597,-935,200,727,-843,130,428,188,-150,404,574,124,382,858,-132,-982,80,984,-140,263,175,-165,-278,859,-514,834,-163,222,-640,-980,690,277,-673,-155,176,615,701,729,-730,-16,730,-561,-363,-600,-485,-781,-923,628,-781,-379,-451,-350,84,773,925,408,-647,-73,-408,-869,-236,-845,311,-351,-275,613,372,96,-692,-403,-910,-130,188,21,483,-785,-725,733,-901,-344,370,-312,-865,-438,896,-680,415,-798,-671,-175,-161,461,-885,910,-820,782,-279,798,798,-929,863,918,543,989,306,-71,197,-353,47,35,344,919,18,-185,902,714,624,-383,827,-168,154,392,96,975,-293,-294,-311,-112,782,-176,847,-569,-830,-273,875,618,486,-615,330,-22,-548,-418,-775,185,221,584,-501,-763,276,-3,318,-615,-509,324,299,389,728,-546,-10,-527,148,-379,904,-327,959,829,734,790,933,621,-427,-193,908,-63,478,-587,491,-57,281,948,4,-813,599,-192,81,-599,567,731,425,-382,74,-1,187,-893,-613,415,300,53,-184,641,478,22,525,830,-461,16,-486,-417,225,508,-899,987,919,946,476,-488,11,783,-259,875,-841,942,136,799,584,-850,-759,221,-797,971,405,957,-37,540,622,-65,-157,-791,788,251,-341,-578,99,762,202,-819,-77,786,675,905,445,-791,677,346,-482,-82,34,-893,114,374,196,745,-967,-528,664,-613,-82,668,-674,-815,751,-745,140,232,517,-763,516,-561,276,467,873,213,-885,-844,-317,883,-664,406,303,-216,-550,549,-942,-794,-720,754,-642,107,-353,-67,-302,-48,37,-974,762,82,547,-480,-251,-812,684,-883,-990,-690,734,-179,950,-658,-50,653,-664,-763,506,54,794,-337,276,-852,894,977,954,-827,-712,332,714,550,387,-10,967,825,-698,229,476,134,858,-762,838,-322,739,751,-106,-932,49,3,739,-728,-222,-896,-477,-796,-935,-477,-581,53,-712,923,904,-653,-366,-570,-278,348,996,-529,416,-827,-111,61,-784,524,-251,-419,-404,553,943,-706,-138,888,993,31,-446,221,-902,290,842,-393,-846,408,614,-726,220,-889,-418,-254,709,578,-121,-758,-340,143,-421,933,-782,906,965,-229,138,416,-761,492,-82,342,865,-952,733,410,-186,561,-640,-603,644,-805,-184,-861,-373,115,721,-782,-355,737,-219,-149,-566,583,504,768,-122,-957,-626,872,-126,894,244,140,765,-290,827,236,-335,-905,-952,989,362,-385,408,-920,326,335,645,937,664,-683,281,893,683,-430,-743,83,938,438,365,652,-806,-355,-654,766,314,-812,-373,843,920,270,-428,-164,-4,218,32,-66,926,-889,-377,636,828,772,482,-20,166,864,938,-388,810,-585,535,116,118,767,-910,889,-548,-934,333,-128,-760,-691,318,987,-289,-674,-206,-973,686,-183,722,703,532,-841,-85,36,98,-763,400,897,245,816,-838,157,847,560,-906,505,-760,470,350,-260,-597,545,544,-64,407,-771,-661,-713,861,963,365,346,473,732,641,-411,-30,402,689,98,922,-128,426,336,-828,38,-237,-162,442,-735,-250,-842,-658,345,-65,952,-711,126,-28,115,-797,-316,489,-919,-563,-106,917,493,-780,-697,293,81,318,-598,-592,562,285,63,125,-199,261,558,-620,270,-23,-188,713,779,266,393,-500,659,-315,-202,801,763,-891,208,-20,76,52,848,-119,-994,906,-782,269,725,598,-68,461,-402,-175,-75,10,-892,-134,-833,826,698,-186,556,-340,-596,618,-349,-709,-842,-468,-349,-288,68,542,73,37,-601,737,-341,477,163,626,-911,209,-724,437,378,0,-733,-197,842,546,-888,249,-886,555,-435,-167,-616,137,40,221,-378,-757,-972,-312,-850,-244,-144,512,-306,603,-319,423,-807,-629,882,-54,629,876,-475,-642,-702,-285,989,262,883,448,-948,-246,416,202,-55,-751,84,887,722,-803,787,226,-127,-350,-137,548,186,464,-48,-148,770,-688,563,567,863,436,397,155,-674,528,236,944,-896,-499,503,413,-692,653,805,-455,507,850,575,-357,381,958,758,193,-823,993,508,812,315,602,365,-241,-469,-61,-324,203,-463,649,867,-147,-731,841,-626,-556,-134,67,758,-702,-650,-638,-404,-972,-902,646,167,716,271,-5,-189,314,634,375,118,401,400,779,-825,-30,-324,928,-956,586,-672,135,741,-265,-722,-778,221,-696,-226,-294,378,-7,785,831,700,-832,977,159,979,-591,-183,-278,-2,562,-224,-430,584,-327,979,73,102,732,-366,-797,-482,826,223,374,-777,215,-979,-166,381,-218,264,-168,972,466,-89,-93,-797,462,695,795,179,-821,947,-961,-310,928,-380,-603,-705,668,-868,-170,-835,-539,675,-974,-532,-122,-558,229,-888,-691,-976,178,-411,-561,805,843,537,585,-474,-42,-173,-646,-146,207,452,-629,-416,329,-272,-103,32,459,-514,558,-120,-461,532,450,34,-625,-885,-636,-285,873,168,-902,-525,739,-206,-39,146,-926,-253,-755,-625,444,792,-680,-865,-455,857,-520,-805,654,135,958,117,-602,-161,664,282,-586,810,528,-346,648,-876,-354,-590,-848,799,227,347,545,-284,-202,-49,-336,158,414,489,164,-511,871,-377,-670,-182,-297,376,416,490,858,342,-44,40,613,-71,-775,692,310,506,-325,-26,421,-855,-391,9,-617,-138,-448,76,482,-181,459,-17,870,-124,-152,394,-866,-297,657,-639,-474,373,471,-102,2,-92,-90,759,-937,927,-535,-950,533,-171,-58,-365,806,653,779,94,35,148,-994,-372,-178,163,93,-100,-889,-918,784,-685,-693,-786,189,818,-444,62,-218,529,-46,735,-407,-98,-649,-96,367,700,283,561,-834,-973,993,-133,-782,926,-543,-979,-423,-992,-253,521,5,845,850,-294,-792,-789,176,-809,279,673,-472,109,-272,-862,-88,-230,817,505,591,-796,-17,-453,-858,-571,-267,-550,673,-420,-110,543,-199,499,309,-789,-917,695,328,-738,405,468,-769,-568,-145,369,754,-333,-462,-914,86,-293,-291,389,132,-160,-199,-247,-295,-519,894,270,419,781,-92,-314,-654,-44,32,-251,71,776,496,-247,381,393,347,-637,-120,111,-87,-447,872,577,-249,43,952,-662,161,-226,-301,-588,129,-820,907,681,421,-543,689,-543,161,-190,267,-726,-713,-814,704,323,312,326,328,-907,-377,-110,563,-522,80,451,-343,-244,34,582,863,391,-750,721,586,426,-900,-212,-327,957,-968,856,-167,375,388,-109,226,26,-388,-906,-245,821,-577,702,-290,218,295,-45,-132,646,-726,-956,-30,-180,999,-486,-114,246,265,-274,-392,244,382,838,-172,-158,-995,-764,-738,-973,-88,711,-23,-40,288,-95,-401,-938,901,-788,468,-998,-17,835,552,-902,4,-341,440,-30,-878,175,57,-544,524,323,-389,310,-512,-116,-808,-394,523,-789,-108,-406,-523,-563,705,-937,383,654,-425,-436,526,-38,667,-656,631,548,-948,366,202,-889,744,-50,295,920,237,59,-128,-780,685,-830,93,-845,-279,-331,16,584,-34,224,-616,854,378,-829,709,-42,339,-938,-978,-639,-170,-155,570,-52,-731,712,36,-54,400,676,95,-122,-323,-694,-965,740,442,-629,-659,804,232,-913,74,-406,481,292,-770,33,995,-927,532,-320,788,993,-622,761,476,113,-224,-657,434,-807,431,-532,-162,692,941,628,-102,-761,-43,-780,465,680,-689,499,835,-258,-319,470,818,-546,-703,-456,-746,601,210,-101,-507,-609,-99,-773,-589,434,484,424,511,559,406,-861,-724,-547,-903,-749,194,293,-833,-713,467,-453,121,-121,910,-877,676,-210,342,923,695,898,40,-501,-404,158,-874,-71,441,550,364,540,296,401,49,-775,-67,-294,883,985,-229,-908,-713,607,949,560,471,836,-382,117,-105,57,-681,326,10,-644,4,629,-206,928,611,-412,-487,-110,988,836,-565,-573,-418,-139,700,283,-520,-368,485,903,-439,41,-162,-266,-38,990,-495,-340,686,412,927,-238,895,-399,-674,-100,-947,368,-98,73,517,929,121,658,968,81,-497,399,846,-464,105,-177,-510,-866,897,-193,-155,539,-289,-352,895,-620,104,-41,836,962,323,-774,239,-115,-454,-530,-682,663,34,-143,60,-91,557,798,-731,-391,975,-81,-781,-372,70,106,-929,328,533,-314,-726,289,-267,-136,-316,703,476,141,-219,489,516,174,182,428,777,-201,-605,-697,-353,-255,-84,-333,450,-970,-60,576,-50,75,963,-16,-592,443,-957,-863,136,-742,161,469,96,-916,499,780,-83,41,-121,981,-351,760,-614,-164,-138,-296,85,-111,-253,576,-555,-54,285,475,59,-951,534,-256,52,-268,520,101,12,940,190,-526,-139,-67,916,949,698,164,345,145,71,-788,487,159,386,904,807,-503,561,587,-520,-478,345,462,790,-422,-427,220,85,588,550,-933,-953,721,-502,73,227,-499,-364,-370,687,136,-624,518,38,-635,-158,-856,-639,-526,721,300,-285,-174,-819,563,-395,490,540,-246,411,208,-622,-701,-125,248,-528,326,-384,-515,576,365,-509,-715,-972,991,134,122,-675,889,28,370,-13,-560,-527,500,-568,259,767,-224,-787,419,783,557,138,393,353,-553,465,978,615,863,-338,-110,-780,898,-528,71,-294,8,-608,89,-500,-630,3,-94,-704,-411,-514,-941,500,434,-961,-117,254,-563,-164,455,-173,-470,-180,-20,-11,-563,-707,-967,-791,771,-337,-249,567,-395,975,914,-124,-242,-182,109,-546,-712,-855,-156,645,793,418,689,-437,676,-146,874,916,-527,-605,-892,-537,-733,-180,333,526,118,87,-243,-535,459,-944,-549,99,246,-77,-145,-888,-714,307,589,-651,-622,348,639,-650,559,116,-105,889,-71,-880,-580,222,-714,-344,427,-63,-240,-939,153,-912,-246,745,-454,-156,-666,-754,562,-144,-113,323,-687,-936,789,712,-684,-291,-530,-496,-678,730,147,-42,593,-742,-936,-619,895,466,439,124,703,-106,-136,520,-105,-318,-807,-652,-462,308,784,-557,-416,-431,845,-877,708,301,886,388,-712,772,-134,-633,708,554,-362,-452,-498,25,-957,55,93,492,127,-787,-566,-146,-469,638,297,-483,-646,-885,610,-37,787,-315,-139,613,-733,2,169,441,-395,418,-784,-829,453,366,146,-188,-444,-55,-493,328,483,-148,878,-842,-279,249,199,343,-547,964,-47,955,189,-918,-375,395,239,-807,110,468,-911,-756,-222,-151,740,-697,469,119,16,215,863,281,-403,814,-339,246,632,581,-160,-763,-759,788,187,905,236,212,-193,695,-462,127,-375,-110,600,-671,235,-15,-775,461,899,627,-141,831,196,62,993,936,-284,-238,416,-961,159,-127,265,108,-151,583,658,-521,33,-948,-116,480,257,-608,399,745,-624,160,-329,-721,-350,67,106,582,-541,810,958,-154,-884,-142,-695,-495,218,543,386,-223,234,-632,892,613,-587,470,-905,-293,101,612,-280,322,-188,209,-189,928,807,-267,-415,187,418,206,163,-263,-417,874,868,5,-476,-36,-384,-937,-605,-94,436,865,420,-968,-252,307,-759,-810,220,84,-309,502,128,-889,343,517,-997,-768,-906,-311,678,-432,778,34,-820,457,-543,300,-126,-27,706,-859,-367,749,959,-40,-813,851,855,-987,-883,866,233,387,991,-83,479,77,872,-233,-280,-488,957,216,851,-761,-438,-727,581,263,880,947,-562,-198,-57,578,620,175,-298,880,-112,-302,-82,-446,-657,-239,-438,215,792,-432,-464,-641,836,725,645,-851,168,-112,-381,-344,-996,104,-758,227,697,-78,964,-409,972,-959,-426,191,919,800,-98,67,-246,385,862,-401,679,548,390,-391,-414,450,-780,-306,-625,-791,-460,443,-606,955,170,-177,-355,908,-558,868,797,750,-245,112,-993,648,-980,257,130,818,-939,-625,142,-141,-947,-606,-38,-332,268,-969,106,-32,-557,7,718,-63,992,-665,667,-914,909,990,-36,-246,-830,114,-545,-152,551,611,-827,-655,399,-536,-348,-76,893,115,-609,771,-312,-318,-991,988,-205,625,796,433,-803,584,63,-565,229,910,719,-452,-329,93,244,-226,951,-701,992,939,158,-148,-306,643,332,-347,496,-263,394,-125,383,-609,-212,-855,467,-135,-279,-240,-523,59,-795,-853,134,-918,-651,-325,-422,-431,-390,-869,-238,91,-146,585,997,23,78,125,155,-179,-976,122,-14,668,352,71,335,50,242,-280,-804,-620,425,-563,-728,-817,-859,-417,-932,-916,118,-148,-822,174,890,-765,-505,548,30,-74,-405,278,-954,-118,945,627,-374,392,274,-752,810,124,589,-457,-715,530,-206,-241,849,-541,-253,-930,361,-82,-756,545,-485,364,907,-209,-895,742,-159,-376,-113,-349,394,425,603,-488,996,-10,-347,538,-826,-537,-558,-329,-989,82,-448,276,271,-702,832,-674,-796,-490,-451,-294,822,647,203,-153,-181,142,-852,-661,-884,482,-554,665,263,208,-881,655,30,212,675,248,-995,-415,-411,-949,-153,202,249,-298,507,571,390,-4,-110,-553,-307,-813,283,-485,-58,304,903,132,84,-855,200,-18,364,-255,-12,9,746,360,630,229,-519,810,-374,-264,13,334,996,684,669,-526,135,932,-376,-392,-634,322,-148,900,-126,-646,-114,-740,-475,620,-15,151,175,-819,-790,350,614,455,571,-600,567,-490,-882,-921,-651,-34,-922,383,30,-156,-956,207,-853,240,934,-909,-718,-890,650,39,158,894,-277,447,170,-87,430,-468,-306,-729,78,324,416,566,223,-195,-314,-825,-320,-432,-541,449,-136,579,-989,-180,-509,818,-462,-201,-658,-951,-838,-580,-203,823,89,446,-531,-822,-175,-413,671,-191,825,-14,-296,-948,-912,888,-662,88,-231,-459,-623,-935,-543,170,332,911,733,472,564,759,99,790,46,363,361,-883,-632,-362,-519,192,441,-147,269,-555,-274,-861,-673,773,-315,367,324,-387,-480,-37,418,787,983,-704,-978,289,-750,-522,476,854,583,640,-768,942,-360,-215,755,40,-591,-341,-205,-280,941,953,-104,986,834,46,861,145,3,38,353,26,860,620,-117,-746,882,-431,633,725,-418,46,-263,908,415,-663,-556,-475,590,-603,-858,-781,330,861,-398,51,681,-345,33,-648,528,305,408,728,-96,13,66,50,-738,-255,-504,983,-295,-728,-268,798,351,-363,-505,-664,-513,-125,792,195,602,-854,910,-631,596,64,-600,-554,0,757,708,-772,652,-871,-532,992,-11,497,207,830,-977,42,-501,-172,519,291,366,119,-84,-434,170,-621,81,862,-291,-546,-825,-922,520,-140,583,-383,-109,59,576,-741,695,-26,417,-345,655,-532,980,810,-918,-586,930,663,-73,916,593,172,510,435,-798,757,202,860,-817,536,499,-324,-306,-505,-228,-113,-441,517,659,397,313,-267,-388,-129,518,658,-620,631,643,91,238,-762,569,-387,263,-422,-69,424,67,-49,-95,210,161,766,-415,-719,-372,527,637,60,676,-821,977,-412,406,86,34,-182,-191,606,445,585,330,-528,932,-996,532,-425,-214,291,-429,837,-907,873,599,-320,-123,-951,-192,-684,-891,84,15,915,840,-961,-432,-806,523,-358,555,783,353,-231,221,-669,-489,-730,382,796,198,115,981,597,56,-40,-273,-574,856,-768,280,-817,-300,-751,331,-149,-687,-791,-613,714,811,875,-51,338,643,-560,299,-35,791,-514,564,643,-144,224,770,-194,336,-212,195,-567,-48,-568,-412,415,-633,-360,-526,-785,242,-209,403,-72,-482,-183,-210,240,-174,351,991,-108,477,-305,-60,800,-184,-544,-538,380,-687,-53,-32,-550,312,46,-783,-24,-773,-645,129,233,31,-294,-468,364,-821,604,260,-171,-327,-216,257,-838,-81,-566,899,274,-298,653,290,-716,213,-164,873,-99,-251,-131,105,358,378,113,-325,371,-249,959,479,-54,-7,252,-105,-171,153,-85,-761,-974,-36,-188,-396,161,-657,-838,75,370,439,53,78,22,-23,372,261,-136,599,984,-561,-536,-983,474,165,974,425,104,-216,-261,-182,-46,-297,-497,-502,-865,622,-301,768,-917,-428,-180,157,-107,-58,-982,-730,100,503,283,90,-422,-343,864,-226,851,906,-463,-295,-775,-332,660,-821,-778,647,408,133,-640,-194,445,-391,-889,38,-820,-799,778,-378,56,-568,-77,524,991,615,607,230,-537,-716,446,-752,-210,-816,-49,67,-359,563,-534,-245,-380,-282,-441,907,-613,-377,790,-396,-223,296,149,-906,662,892,390,252,-679,961,952,67,909,272,719,-90,-325,256,701,-685,315,491,-936,-986,-226,309,430,-704,115,384,942,664,620,-876,713,-868,-281,-297,-311,860,210,-994,791,636,-696,-820,-745,24,-96,359,-852,304,-103,613,-117,-542,-896,-497,182,579,980,83,-168,-962,475,-371,-521,933,953,-434,-716,-407,-399,-76,241,816,355,658,-78,-211,-378,365,97,-943,355,-867,760,-238,492,299,-148,-712,-912,25,748,358,-619,-416,-887,-652,-824,-498,-838,767,-414,166,186,-443,345,-404,-414,673,56,-337,-319,-575,188,-131,-776,841,279,914,-999,645,890,776,-571,-212,136,-465,-613,60,-89,-989,-458,890,313,-528,596,-747,730,170,996,-749,-67,688,126,-115,-280,50,-409,811,41,-153,994,925,-886,58,531,-206,-338,-743,225,-84,-456,460,473,-837,17,-364,-506,-82,337,-990,748,-799,-823,860,-516,-831,800,-185,904,372,-889,-925,220,907,476,-576,-302,971,655,-111,244,201,-127,237,-648,-817,847,37,535,-349,617,444,505,205,394,462,-737,-643,-161,-524,43,604,-916,-884,569,-823,-790,869,156,-800,-453,-285,-666,378,951,-744,271,835,501,430,243,468,156,-439,788,-43,-870,938,-224,-786,-551,-170,222,138,-192,392,886,309,-522,359,-448,-667,879,175,477,625,-121,547,-235,-893,504,475,-695,-40,479,-537,-535,-479,652,-296,-848,-822,873,-712,765,-256,-950,-698,-672,-301,873,342,678,-375,-402,-735,641,-111,188,-496,-494,-529,409,914,-150,-518,-709,-125,744,273,470,270,-500,-559,-125,-644,399,-232,-239,-561,-472,84,79,498,947,-522,-805,219,-484,-396,-10,-620,481,570,-982,-754,315,-914,-717,778,-576,198,-722,181,24,179,-622,978,-976,-247,-241,840,803,412,316,-847,959,846,-836,-439,614,817,-729,844,855,51,415,56,967,-625,-400,1,107,556,986,140,841,-4,95,-375,852,-27,-726,-591,509,-46,229,735,809,-754,-311,522,-51,-59,665,290,-476,703,-238,108,734,644,329,-514,3,317,-968,-871,565,608,-150,4,-513,-191,-209,-549,-718,-967,722,-495,633,-109,979,381,816,-669,436,-134,-480,549,-998,-299,269,-694,-256,-650,-103,-436,425,268,-20,-862,-323,776,-554,-118,-62,-645,35,-792,301,75,-656,-284,-47,27,-370,-778,-312,-272,182,36,-553,-827,-992,28,-230,722,-224,209,413,-735,234,293,18,-830,-828,-709,884,-980,-367,87,-157,-636,-274,-429,300,-753,943,834,-606,-702,-554,382,-664,652,870,-79,-497,194,-865,-317,-783,677,-289,405,530,-840,-820,442,359,-711,822,-14,-341,-624,533,-8,70,342,323,502,664,-333,-813,-888,-878,-77,941,873,-427,131,949,269,-197,569,-685,307,693,944,-613,956,-771,513,15,653,499,-709,-593,-457,373,456,959,189,40,766,586,445,-321,902,-649,-998,347,85,-772,107,14,38,-435,559,-178,574,340,298,-742,265,-663,-876,268,831,-937,444,-962,858,-360,255,939,324,940,820,-928,529,634,300,-775,-918,867,-950,-814,469,129,735,911,-208,-915,-568,971,-96,-525,723,-236,548,-456,-732,-831,-587,319,-574,-93,527,-77,-486,757,820,-752,-157,-269,-604,203,-149,-117,-713,-153,801,213,-952,140,-146,-762,-224,-77,-921,827,-545,184,495,760,-436,-138,-974,789,650,860,-545,757,64,488,-689,162,527,48,740,468,-972,232,806,993,232,-630,487,841,-580,547,758,-93,-603,737,559,-413,-10,-198,30,182,-299,987,902,-503,-669,736,-213,347,117,885,-706,-385,-631,359,311,820,-331,811,-785,431,-878,720,882,299,728,132,618,-606,560,62,-326,-468,938,-276,-913,-248,-378,-875,-509,461,725,830,-627,-18,569,-181,-598,430,-303,561,992,-311,-743,534,192,815,-437,-520,549,-119,-862,-525,387,859,-472,917,961,904,-326,131,371,584,-941,-519,925,157,298,-425,873,783,524,350,-876,56,523,-91,-220,424,-588,-943,824,872,360,-989,-284,-621,-852,829,330,-148,-878,769,-510,-419,-900,976,-647,-724,532,145,-452,-664,-483,-428,-278,637,354,508,-665,319,14,239,-255,-713,753,698,91,890,165,88,223,-616,-480,-823,-532,-475,517,991,-919,-350,147,-425]

# x = [i for i in arr if arr.count(i)>1]
# if len(x)>1:
#     print(True)
# else:
#     print(False)


# store = {
#         "shelf1":{
#                     "product1":{
#                                 "J":[10,30,45,50],
#                                 "F":[60,64,68]
#                                 },
#                     "product2":{
#                                 "J":[66,67,81,75],
#                                 "F":[71,78,85]
#                                 },
#                     "product3":{
#                                 "J":[18,20],
#                                 "F":[21,22],
#                                 "M":[22,23,24]
#                                 },

#                 },
#         "shelf2":{
#                     "product1":{
#                                 "J":[206,220,225],
#                                 "M":[180,170,165],
#                                 "A":[160,150,136]
#                                 },
#                     "product4":{
#                                 "J":[300],
#                                 "F":[280,300,385],
#                                 "M":[280,300,385],
#                                 "A":[360,376]
#                                 },
#                     "product3":{},
#                     "product6":{}
#                 },
#         "shelf3":{
#                     "product2":{
#                                 "M":[55,54,61],
#                                 "A":[53,54,55]
#                                 },
#                     "product4":{},
#                     "product6":{}
#                 }

#         }
# # print(store["shelf1"]["product1"]["J"])
# print(store.values())


# arr=[1,2,2,3]
