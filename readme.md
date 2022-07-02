# Prerequisite

python version: python 3.7.0

download total_word_feature_extractor_zh.dat from **Baidu Netdisk** to directory: /nlpexp-chatbot/data

```bash
链接：https://pan.baidu.com/s/1kNENvlHLYWZIddmtWJ7Pdg 密码：p4vx
```

```bash
# in directory: nlpexp-chatbot
pip install -r requirements.txt
```

# Training

```bash
# in directory: nlpexp-chatbot
python -m rasa train --config configs/zh_jieba_mitie_embeddings_config.yml --domain configs/domain.yml --data data/
```

# Running

1. activate rasa server

   ```bash
   # in directory: nlpexp-chatbot
   python -m rasa run --port 5005 -m models/20220412-024906.tar.gz --endpoints configs/endpoints.yml --credentials configs/credentials.yml --debug --cors "*"
   # 使用新训练的模型可以更改-m参数
   ```

2. activate action server

   ```bash
   # in directory: nlpexp-chatbot
   python -m rasa run actions --port 5055 --actions actions --debug
   ```

3. activate web server

   ```bash
   # in directory: nlpexp-chatbot
   python server.py
   ```

4. activate html
   ```bash
   # in directory: bot-front
   ```
   double-click index.html


# Troubleshooting

## Installing requirements.txt

### If error message: building wheel for mitie (setup.py) ... error

After pip install -r requirements.txt, try:


   ```bash
pip install cmake
pip install boost
git clone https://github.com/mit-nlp/MITIE.git
cd MITIE-master
python setup.py build
python setup.py install
   ```

## Training

### Cannot import name 'WebClient' from slack

```bash
pip uninstall slack
pip uninstall slackclient
pip install slack
pip install slackclient
```

### module 'tensorboard.plugins.pr_curve.summary' has no attribute 'pb'

open File ".../site-packages/tensorboard/summary/v1.py"

comment out the line: pr_curve_pb = _pr_curve_summary.pb

\# pr_curve_pb = _pr_curve_summary.pb

and another error will occur: AttributeError: module 'tensorboard.plugins.pr_curve.summary' has no attribute 'raw_data_pb'

open again and comment out the line:pr_curve_raw_data_pb = _pr_curve_summary.raw_data_pb

\# pr_curve_raw_data_pb = _pr_curve_summary.raw_data_pb
