# Model Analysis and notes

## Multiclass vs Multilable
- In a **Multiclass** classification only one output can be True.
- In a **Multilable** classification one or more than one outputs can be true.

## Term frequency
- tf(i,d) - Frequency for term (or n-gram) 't' in the document 'd'

- The number of times that a term is present.

```tf = (Number of times term t appears in a document)/(Total number of terms in the document)```

## Term frequency - inverse document frequency
- For document search and information retrieval. 

- It works by increasing proportionally to the number of times a word appears in a document, but is offset by the number of documents that contain the word. **So, words that are common in every document, such as "this", "what", "and" "if", rank low even though they may appear many times, since they don’t mean much to that document in particular**.

- TF-IDF allows us to give give more importance to those terms that are frequent in the current document, but not in all the documents.

### Applications of TF-IDF
- Information retrival
- Keyword extraction
- Help sort data into categories

```Text vectorization transforms text within documents into numbers, so TF-IDF algorithms can rank articles in order of relevance.```

<hr />
ast -> literal evaluation (Converts the string into list data)
lambda function-> iterates over each row and performs a specific operation




## Onehot encoding
- TfidfVectorizer

- MultilabelBinarizer (for multilabel classification)


# ML MODELS USED

## SGDClassifier


## Logistic Regression
- Solver -> lbfgs


## LinearSVC

## OnevsRestClassifier


# MODEL PERFORMANCE METRICS
## Jaccard similarity/index
Size of intersection of the predicted labels and the true labels divided by the size of union of the predicted and true labels. Ranges from 0 to 1, 1 being the perfect score


# SAVING AND LOADING THE MODEL

