import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

def train_model():
    df = pd.read_csv('datasets/marketing_campaign_dataset.csv') #Load dataset

    #Drop unnecessary columns
    df = df.drop(columns=['Campaign_ID', 'Company', 'Duration', 'Acquisition_Cost', 'Location', 'Language', 'Customer_Segment', 'Date'])

    #Encode categorical feature values into numeric values
    le = LabelEncoder()
    df['Campaign_Type'] = le.fit_transform(df['Campaign_Type'])
    df['Target_Audience'] = le.fit_transform(df['Target_Audience'])
    df['Channel_Used'] = le.fit_transform(df['Channel_Used'])

    X = df[['Target_Audience', 'Channel_Used']]
    y = df['Campaign_Type']

    #Split dataset into training and testing set
    X_train, X_test, y_train, y_test = train_test_split (X, y, random_state=42, test_size=0.3) 

    #Train logistic regression model
    logreg = LogisticRegression(max_iter=1000)
    logreg.fit(X_train, y_train)
    
    joblib.dump(logreg, 'models/trained_model.pkl') #Save trained model

train_model()
