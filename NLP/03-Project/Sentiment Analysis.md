## Sentiment Analysis in Movie reviews

The goal of this project is to build an NLP model that predict the sentiment of a movie review (positive or negative).

### Steps
#### 1. dataset : 

Download the [imdb dataset](http://ai.stanford.edu/~amaas/data/sentiment/) you'll find train and test sets with positive and negative reviews. Format of file names is [[id]_[rating].txt]. 1_6.txt -->text with id 1 and rating 6/10 stars on imdb. The file contains a user's review.

#### 2. peprocessing : 


Get more insights on the dataset (number of unique words, number of average length for the reviews, etc).
Preprocess the data set to be ready for modeling (hint don't forget padding sequences)

You should end with a X_train, y_train and X_test, y_test. 

#### 3. modeling

train a deep learning model for text classification and evaluate it's accuracy. (example of model is to be found [here](imdb.ipynb) )



