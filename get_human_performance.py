__author__ = 'Qiao Jin'

'''
Calculate human performance on test set
'''

import json
from sklearn.metrics import f1_score, accuracy_score

test_set = json.load(open('data/test_set.json'))

labels = []
r_free = []
r_req = []

for pmid, info in test_set.items():
    labels.append(info['final_decision'])
    r_free.append(info['reasoning_free_pred'])
    r_req.append(info['reasoning_required_pred'])

maj = ['yes' for _ in labels]

print('====Majority Performance====')
print('Accuracy %f' % accuracy_score(labels, maj))
print('Macro-F1 %f' % f1_score(labels, maj, average='macro'))

print('====Reasoning-Free Human Performance====')
print('Accuracy %f' % accuracy_score(labels, r_free))
print('Macro-F1 %f' % f1_score(labels, r_free, average='macro'))

print('====Reasoning-Required Human Performance====')
print('Accuracy %f' % accuracy_score(labels, r_req))
print('Macro-F1 %f' % f1_score(labels, r_req, average='macro'))
