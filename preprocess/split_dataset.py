__author__ = 'Qiao Jin'

'''
Split the ori dataset to 500 test and 500 CV
Split the 500 CV to 10 folds
'''

from functools import reduce
import json
import math
import os
import random
random.seed(0)
import shutil
import sys

def split(dataset, fold):
    '''
    dataset: dataset dict
    fold: number of splits

    output list of splited datasets

    Split the dataset for each label to ensure label proportion of different subsets are similar
    '''
    add = lambda x: reduce(lambda a, b: a+b, x)
    
    label2pmid = {'yes': [], 'no': [], 'maybe': []}
    for pmid, info in dataset.items():
        label2pmid[info['final_decision']].append(pmid)

    label2pmid = {k: split_label(v, fold) for k, v in label2pmid.items()} # splited

    output = []

    for i in range(fold):
        pmids = add([v[i] for _, v in label2pmid.items()])
        output.append({pmid: dataset[pmid] for pmid in pmids})

    if len(output[-1]) != len(output[0]): # imbalanced: [51, 51, 51, 51, 51, 51, 51, 51, 51, 41]
        # randomly pick one from each to the last
        for i in range(fold-1):
            pmids = list(output[i])
            picked = random.choice(pmids)
            output[-1][picked] = output[i][picked]
            output[i].pop(picked)

    return output

def split_label(pmids, fold):
    '''
    pmids: a list of pmids (of the same label)
    fold: number of splits

    output: list of split lists
    '''
    random.shuffle(pmids)

    num_all = len(pmids)
    num_split = math.ceil(num_all / fold)

    output = []
    for i in range(fold):
        if i == fold - 1:
            output.append(pmids[i*num_split: ])
        else:
            output.append(pmids[i*num_split: (i+1)*num_split])

    return output

def combine_other(cv_sets, fold):
    '''
    combine other cv sets
    '''
    output = {}

    for i in range(10):
        if i != fold:
            for pmid, info in cv_sets[i].items():
                output[pmid] = info

    return output

split_name = sys.argv[1]

if split_name == 'pqal':
    # 500 for 10-CV and 500 for test
    dataset = json.load(open('../data/ori_pqal.json'))

    CV_set, testset = split(dataset, 2)
    with open('../data/test_set.json', 'w') as f:
        json.dump(testset, f, indent=4)

    CV_sets = split(CV_set, 10)
    for i in range(10):
        if os.path.isdir('../data/pqal_fold%d' % i):
            shutil.rmtree('../data/pqal_fold%d' % i)
        os.mkdir('../data/pqal_fold%d' % i)
        with open('../data/pqal_fold%d/dev_set.json' % i, 'w') as f:
            json.dump(CV_sets[i], f, indent=4)
        with open('../data/pqal_fold%d/train_set.json' % i, 'w') as f:
            json.dump(combine_other(CV_sets, i), f, indent=4)

elif split_name == 'pqaa':
    # get 200k for training and rest for dev
    dataset = json.load(open('../data/ori_pqaa.json'))
    
    pmids = list(dataset)
    random.shuffle(pmids)

    train_split = {pmid: dataset[pmid] for pmid in pmids[:200000]}
    dev_split = {pmid: dataset[pmid] for pmid in pmids[200000:]}

    with open('../data/pqaa_train_set.json', 'w') as f:
        json.dump(train_split, f, indent=4)
    with open('../data/pqaa_dev_set.json', 'w') as f:
        json.dump(dev_split, f, indent=4)
