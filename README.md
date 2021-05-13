
# Deep Learning Based Morphological Analysis for Bhojpuri (UDA) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

![image](https://github.com/AnonySharma/DL-based-MorphAnalyzer-Bhojpuri/blob/master/front.png)

# Description
## Base
A multi-task learning CNN-RNN model combined together with the potential of task-optimized phonetic features to predict the Lemma, POS category, Gender, Number, Person, Case, and Tense-aspect-mood (TAM) of Hindi words. **(using MT-DMA)**

![image](https://github.com/AnonySharma/DL-based-MorphAnalyzer-Bhojpuri/blob/master/morph_analyzer/src/images/sample.png)

## Improvement
Used Unsupervised Domain Adaptation(UDA) to train the model on the training data of Hindi, and then testing it on Bhojpuri which resulted into around 70% accuracy.


## Report and Presentation
**Report:** [link](https://drive.google.com/file/d/1eLaWkbN1VAmueGimYe4nlvPkkDK6VYxi/view?usp=sharing)

**Presentation:** [link](https://docs.google.com/presentation/d/1Hn_99vbOGmUy2mSKo6tzJixyGDQP0pV6tnliOTlh9Yw/edit?usp=sharing)

# Framework

![image2](https://github.com/AnonySharma/DL-based-MorphAnalyzer-Bhojpuri/blob/master/morph_analyzer/src/images/morph_analyzer_model.png)

# Getting started

### Clone the repository

```
git clone https://github.com/AnonySharma/DL-based-MorphAnalyzer-Bhojpuri.git
cd DL-based-MorphAnalyzer-Bhojpuri
cd morph_analyzer
```
### Install all the dependencies (USE PYTHON 3.7)

```
pip install -r requirements.txt
```
### Preprocess

 - Download the HINDI corpus from [IIITH](http://ltrc.iiit.ac.in/hutb_release/)  and extract it
 - Download the Bhojpuri test data from from [my Google Drive](https://drive.google.com/file/d/1yVYqoi8DX1QqJkEtZtmMUrev1ji3wLYD/view?usp=sharing) and extract it
 - Extract the zip files and save the two folders inside **datasets** folder
 - Run `python wx_converter.py` *(change the paths inside the file if you are doing for any language other than Hindi or Bhojpuri)* 

### Provide the arguments

The file `main.py` takes the following command-line arguments: 

| Argument | Values | Required | Specification |
| ------- | ------- | ------------- | ------------ |
| lang     | hindi, urdu, bhojpuri  | Yes | Language |
| mode     | train, test and predict (i.e., no gold labels required) | Yes |  Training, testing and predictions. |
| phonetic | True/1/yes/y/t and False/0/no/n/f | No (default=`False`) | Use MOO-driven phonological features or not. |
| freezing | "       "      and "       " | No (default=`False`) | Use progressive freezing for training or not (see [FreezeOut](https://arxiv.org/abs/1706.04983)). |

### Run commands: 
Training:
```python
>>> python main.py --lang bhojpuri --mode train --phonetic true --freezing true
```

Testing:
```python
>>> python main.py --lang bhojpuri --mode test --phonetic true --freezing true 
```

Predicting:
```python
>>> python main.py --lang bhojpuri --mode predict --phonetic true --freezing true 
```

For prediction, the plain text should be provided within `src/[lang]_predict_data/test_data.txt`.

### Outputs

For the test mode:

- the predicted roots and features as well as their gold-labelled counterparts are written to separate files within `output/[lang]/roots.txt, feature_0.txt, ..., feature_6.txt`.
- Micro-averaged precision-recall graphs are stored in `graph_outputs/[lang]/`.

For the predict mode, all the predictions (i.e., roots + features) are written to: `output/[lang]/predictions.txt`.

# Extra tools attached

 1. **wx_converter.py** : You can use this to convert any data in CoNLL format, from UTF to WX notation
 2. **results.py** : You can use this to calculate all types of scores like Accuracy, Precision, Recall, F1-Score for the test output generated from any model taking MT-DMA as base

# Base Model

This research paper([MT-DMA](https://arxiv.org/ftp/arxiv/papers/1811/1811.08619.pdf)) was used as a base for the exploratory project. 
```
@article{jha2018multi,
  title={Multi Task Deep Morphological Analyzer: Context Aware Joint Morphological Tagging and Lemma Prediction},
  author={Jha, Saurav and Sudhakar, Akhilesh and Singh, Anil Kumar},
  journal={arXiv preprint arXiv:1811.08619},
  year={2018}
}
```
