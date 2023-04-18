# PubMedQA

## Download
PQA-L is already in `./data/`

[PQA-U](https://drive.google.com/open?id=1RsGLINVce-0GsDkCLDuLZmoLuzfmoCuQ)

[PQA-A](https://drive.google.com/open?id=15v1x6aQDlZymaHGP7cZJZZYFfeJt2NdS)

## Split the dataset
After downloading PQA-A and PQA-U as `ori_pqaa.json` and `ori_pqau.json` in the `./data/`, enter the `./preprocess/` directory and split the dataset:

```bash
cd preprocess
python split_dataset.py pqaa
python split_dataset.py pqal
```

Please be aware that there is no offical code for splitting PQA-U.

## Evaluation and submission
To evaluate your model predictions, please prepare the results in a json format where the key is PMID and value is one of "yes", "no", and "maybe". Run the following script to get the performance:

```bash
python evaluation.py PREDICTIONS_PATH
```

To submit a system on the Leaderboard, please send an email that contains the model predictions and a brief description of the system to Qiao Jin via [qiaojin.andy@gmail.com](mailto:qiaojin.andy@gmail.com).


## Human performance
After splitting the PQA-L and having `./data/test_set.json`, one can run the following script to get human performance:

```bash
python get_human_performance.py
```

## Citation
If you use PubMedQA in your research, please cite our paper by:
```
@inproceedings{jin2019pubmedqa,
  title={PubMedQA: A Dataset for Biomedical Research Question Answering},
  author={Jin, Qiao and Dhingra, Bhuwan and Liu, Zhengping and Cohen, William and Lu, Xinghua},
  booktitle={Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)},
  pages={2567--2577},
  year={2019}
}
```
