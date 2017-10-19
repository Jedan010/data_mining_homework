
# coding: utf-8

# In[1]:

def apriori(data_set, min_support, min_confidence, print_result=True):
    
    import itertools
    num = len(data_set)
    min_s = min_support * num
    data_list = set(item for data in data_set for item in data)
    k = num
    items = {}
    C = {}

    L = {}
    L_rule = {}


    for i in range(1,k+1):

        ##用于计算C
        items['item_' + str(i)] = set(itertools.combinations(data_list,i))
        C['C_'+str(i)] = {}
        L['L_'+str(i)] = {}
        for item in items['item_' + str(i)]:
            s = 0
            for data in data_set:
                if set(item).issubset(data):
                    s += 1 
            C['C_'+str(i)][item] = s
        ## 用于计算L
        for item in C['C_'+str(i)]:
            if C['C_'+str(i)][item] >= min_s:
                L['L_'+str(i)][item] = C['C_'+str(i)][item]
        
        ## 用于终止频繁项集的迭代
        if not L['L_'+str(i)]:
            break

        ## 用于计算强相关规则
        L_rule['L_'+str(i)] = []
        for m in L['L_'+str(i)]:
            for n in range(1,i):
                for j in itertools.combinations(m,n):
                    x = j
                    y = set(m) - set(x)      
                    x_num = L['L_'+str(len(x))].get(tuple(x))
                    y_num = L['L_'+str(len(m))][m]

                    support = x_num / num *100
                    confidence = y_num / x_num *100

                    if confidence >= min_confidence*100:
                        L_rule['L_'+str(i)].append([set(x) , y, str(round(support, 2))+'%', str(round(confidence, 2))+'%'])
                        
                        if print_result:
                            print(set(x) , '==>' , y, end='\t\t')
                            print('support: %.2f%%' %float(support), end='\t\t')
                            print('confidence: %.2f%%' %float(confidence))
    return L_rule, L
                    
   


# In[11]:

## test 1:
data = [['l1', 'l2', 'l5'], ['l2', 'l4'], ['l2', 'l3'],
        ['l1', 'l2', 'l4'], ['l1', 'l3'], ['l2', 'l3'],
        ['l1', 'l3'], ['l1', 'l2', 'l3', 'l5'], ['l1', 'l2', 'l3']]

min_support = 0.22
min_confidence = 0.7

rule, l = apriori(data, min_support, min_confidence, print_result=False)

import pprint
print('rule关联规则的结果：')
pprint.pprint(rule)
print()
print('l频繁项级的结果：')
pprint.pprint(l)


# In[12]:

## test 2:
data_set = ['monkey','donkey', 'make', 'mucky', 'cookie']
data = [[_ for _ in d] for d in data_set]
min_support = 0.6
min_confidence = 0.8

rule, l = apriori(data, min_support, min_confidence)


# In[ ]:



