# IMPORTING LIBRARIES
import pandas as pd
import numpy as np

# IMPORTING DATASET
tsv_file='data/train.tsv'

# CONVERTIVE TSV TO CSV
csv_table=pd.read_table(tsv_file,sep='\t')
csv_table.to_csv('output.csv',index=False)

# READ DATA
df = pd.read_csv('output.csv')
df.head()

# Tags columns is a string. We must convert it to a list.
import ast
df['tags'] = df['tags'].apply(lambda x: ast.literal_eval(x))
df.head()

# IMPORTING ALL THE NECESSART MODELS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split

from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

from sklearn.multiclass import OneVsRestClassifier

# OBTAINING y AS TARGET VARIABLE
y = df['tags']
y

# CONVERT Y COLUMN TO CLASSES
multilabel = MultiLabelBinarizer()
y = multilabel.fit_transform(y)

# THE CLASSES 
multilabel.classes_

pd.DataFrame(y , columns=multilabel.classes_)

# USING TF-IDF VECTORIZER
tfidf = TfidfVectorizer(analyzer = 'word' , max_features=10000, ngram_range=(1,3) , stop_words='english')
X = tfidf.fit_transform(df['title'])

X.shape , y.shape

# SPLITING DATA INTO TEST AND TRAIN SETS
X_train, X_test, y_train , y_test = train_test_split(X , y, test_size = 0.2, random_state= 0)
tfidf.vocabulary_

# BUILD MODEL
sgd = SGDClassifier()
lr = LogisticRegression(solver = 'lbfgs')
svc = LinearSVC()

# JACCARD SCORE IS USED TO CHECK THE ACCURACY OF A MULTILABLE CLASSIFICATION MODEL
def j_score(y_true, y_pred):
  jaccard = np.minimum(y_true, y_pred).sum(axis=1)/np.maximum(y_true, y_pred).sum(axis=1)
  return jaccard.mean()*100

def print_score(y_pred,clf):
  print("CLF: ",clf.__class__.__name__)
  print("Jaccard score: {}".format(j_score(y_test,y_pred)))
  print("-----")

for classifier in [sgd,lr, svc]:
   clf = OneVsRestClassifier(classifier)
   clf.fit(X_train, y_train)
   y_pred = clf.predict(X_test)
   print_score(y_pred ,classifier)

# EXPORTING MODEL 
import joblib
joblib_file = "tagPredictor.pkl"  
joblib.dump(clf, joblib_file)


# Load from file
tagPredictorModel = joblib.load('tagPredictor.pkl')

def getTags(question):
	question = tfidf.transform(question)
	tags = multilabel.inverse_transform(tagPredictorModel.predict(question))
	print(tags)
