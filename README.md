# Custom-Marketing-Campaign

## Dataset
https://www.kaggle.com/datasets/manishabhatt22/marketing-campaign-performance-dataset

## Working
Trained Logistic Regression on the given dataset to predict Campaign Type using Target Audience and Channel Used
Flask website contains a form user can use to input values for the two features and see the best campaign type for that data

## Security
Maximum session time: 30 minutes
Rate limiter on predict function: 15 times per minute
Validate inputs from forms
Redirect to different website in case of error
Run with debug=False to hide any sensitive information that might surface
