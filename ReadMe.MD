## References

https://towardsdatascience.com/scraping-reddit-data-1c0af3040768- Scrapping data
https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html- Praw
https://medium.com/@RareLoot/using-pushshifts-api-to-extract-reddit-submissions-fb517b286563- Extracting more data
https://www.kdnuggets.com/2018/03/text-data-preprocessing-walkthrough-python.html  -Motivation fro data cleaning
## Data Collection

1)Praw was used to try and get 1000 data points for each flair. It gave only around 200 for each.
2)Currently working on getting more data points using pushshifts.io, using which more data can be accumulated.
3) Data was preprocessed using nltk and other libraries such as contractions

## Initially Logistic regression was applied with features as shown below

| Logistical Regression| Accuracy |
| ------------- | ------------- |
| URL  | 43.39%  |
| body | 32.88%  |
| Title | 46.3%  |
| comments | 62.9%  |
| Title+body+comments+url  | 85.71% |
| Title+body+comments+url +num_comments+score |  84.9%  |

num_comments and score is dropped since they clearly have no relevance with the data

| Naive Bayes| Accuracy |
| ------------- | ------------- |
| URL  | 43.99%  |
| body | 24.47% |
| Title | 50%  |
| comments | 47.29%  |
| Title+body+comments+url  | 60.3% |


| SVM | Accuracy |
| ------------- | ------------- |
| URL  | 46.99%  |
| body | 34.68% |
| Title | 50.6%  |
| comments | 61.41%  |
| Title+body+comments+url  | 77.02% |

| RandomForest | Accuracy |
| ------------- | ------------- |
| URL  | 43.39%  |
| body | 34.98% |
| Title | 48.94%  |
| comments | 57.80%  |
| Title+body+comments+url  | 78.9% |


| PassiveAggresive | Accuracy |
| ------------- | ------------- |
| URL  | 47.29%  |
| body | 31.38% |
| Title | 48.64%  |
| comments | 61.41%  |
| Title+body+comments+url  | 77.02% |

Since Logistic regression showed the best accuracy, it was chosen for our model.
Using l1 penalty suprisingly gave way to better results, probably because of the so called 'inbuilt feature selection' by which it gives 0 weights to some of the features.

GridCV was used to find optimum parameter in all algorithms.

Exploratory Data analysis was done in the jupyter notebook.

Remaining tasks:
1) Accumulate more data(comments and body is remaining in the new data)
2) Create statistics for the website
