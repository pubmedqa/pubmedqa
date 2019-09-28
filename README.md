# PubMedQA

## Download
PQA-L is already in `./data/`

[PQA-U](https://drive.google.com/open?id=1RsGLINVce-0GsDkCLDuLZmoLuzfmoCuQ)

[PQA-A](https://drive.google.com/open?id=15v1x6aQDlZymaHGP7cZJZZYFfeJt2NdS)

## Split the dataset
After downloading PQA-A and PQA-L as `ori_pqaa.json` and `ori_pqau.json` in the `./data/`, enter the `./preprocess/` directory and split the dataset:

```bash
cd preprocess
python split_dataset.py pqaa
python split_dataset.py pqal
```

Please be aware that there is no offical code for splitting PQA-U.

## Human performance
After splitting the PQA-L and having `./data/test_set.json`, one can run the following script to get human performance:

```bash
python get_human_performance.py
```
