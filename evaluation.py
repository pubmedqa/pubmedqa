__author__ = 'Qiao Jin'

import json
from sklearn.metrics import accuracy_score, f1_score
import sys

pred_path = sys.argv[1]

ground_truth = json.load(open('data/test_ground_truth.json')) 
predictions = json.load(open(pred_path))

assert set(list(ground_truth)) == set(list(predictions)), 'Please predict all and only the instances in the test set.'

pmids = list(ground_truth)
truth = [ground_truth[pmid] for pmid in pmids]
preds = [predictions[pmid] for pmid in pmids]

acc = accuracy_score(truth, preds)
maf = f1_score(truth, preds, average='macro')

print('Accuracy %f' % acc)
print('Macro-F1 %f' % maf)
