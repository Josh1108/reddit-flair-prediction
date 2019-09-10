https://towardsdatascience.com/scraping-reddit-data-1c0af3040768- Scrapping data
https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html- Praw

initially Logistic regression was applied with features as shown below

| Logistical Regression| Accuracy |
| ------------- | ------------- |
| URL  | 43.39%  |
| body | 32.88%  |
| Title+body+comments+url  | 85.13% |
| Title | 46.3%  |
| comments | 62.9%  |
| Title+body+comments+url +num_comments+score |  84.9%  |

num_comments and score is dropped since they clearly have no relevance with the data

| Naive Bayes| Accuracy |
| ------------- | ------------- |
| URL  | 43.99%  |
| body | 24.47% |
| Title+body+comments+url  | 60.3% |
| Title | 50%  |
| comments | 47.29%  |


| SVM | Accuracy |
| ------------- | ------------- |
| URL  | 46.99%  |
| body | 34.68% |
| Title+body+comments+url  | 77.02% |
| Title | 50.6%  |
| comments | 61.41%  |


| RandomForest | Accuracy |
| ------------- | ------------- |
| URL  | 43.39%  |
| body | 34.98% |
| Title+body+comments+url  | 78.9% |
| Title | 48.94%  |
| comments | 57.80%  |

| passiveAggresive | Accuracy |
| ------------- | ------------- |
| URL  | 47.29%  |
| body | 31.38% |
| Title+body+comments+url  | 77.02% |
| Title | 48.64%  |
| comments | 61.41%  |
