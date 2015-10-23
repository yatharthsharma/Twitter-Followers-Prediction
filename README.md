# Twitter-Followers-Prediction

Problem Statement :
Creation of a regression model that can predict the number of followers of a user on twitter,
given a twitter handle.

// Please see the report for detailed overview of the project

Model Used :

1) Multiple Linear Regression
A linear regression model that contains more than one predictor variable is called a multiple
linear regression model. The following model is a multiple linear regression model with three
predictor variables, X1 ,X2 ,X3
Y = b 0 + b 1 X 1 + b 2 X 2 + b 3 X 3
Y is the value of the Dependent variable (Y), what is being predicted or explained
b 0 is the Constant or intercept
b 1 is the Slope (Beta coefficient) for X 1
X 1 First independent variable that is explaining the variance in Y
b 2 is the Slope (Beta coefficient) for X 2
X 2 Second independent variable that is explaining the variance in Y
b 3 is the Slope (Beta coefficient) for X 3
X 3 Third independent variable that is explaining the variance in Y

2) Non Linear Regression (Log) :
Log(Y) = b 0 + b 1 Log( X 1 ) + b 2 Log(X 2 ) + b 3 Log(X 3 )
Y is the value of the Dependent variable (Y), what is being predicted or explained
b 0 is the Constant or intercept
b 1 is the Slope (Beta coefficient) for Log( X 1 )
X 1 First independent variable that is explaining the variance in Y
b 2 is the Slope (Beta coefficient) for Log( X 2 )
X 2 Second independent variable that is explaining the variance in Y
b 3 is the Slope (Beta coefficient) for Log (X 3 )
X 3 Third independent variable that is explaining the variance in Y

TECHNOLOGIES USED:
1) Python – For data extraction
2) R – For applying the model.

DATA EXTRACTION:
1) Twython (open source library in python) - https://twython.readthedocs.org/en/latest/
for extracting Retweet Data
2) Twitter API
3) Tweepy (open source library in python) - https://github.com/tweepy/tweepy

Method Followed –
1.1) A Multiple linear regression model is created using all the dependent variables – FOLLOWING ,
LISTED, STATUSES ,DAYS and then the model is analyzed using R-Squared , P-VALUE for every
variable . Those variables are removed which do not provide good P-VALUE i.e <0.05 . After
removing the variables , A new model is created using the remaining variables and evaluated
accordingly.

1.2) A non linear logarithmic model is created using the dependent variables – retweet ,
FOLLOWING , LISTED, STATUSES , and then the model is analyzed using R-Squared , P-VALUE for
every variable . Those variables are removed which do not provide good P-VALUE i.e <0.05 .
After removing the variables , A new model is created using the remaining variables and
evaluated accordingly.

2) Correlation values between the variable provide a good evidence of the relationship between
the FOLLOWERS and the dependent variables. Based on the value of correlation coefficient,
variable are added into the model and analyzed using R-Square and P-Value.

