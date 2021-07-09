# Let's import our libraries
import numpy as np
import pandas as pd
import seaborn as sns
import joblib
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

house = pd.read_csv(r'Maison.csv')

# Since the columns are in french, in order to make them more readable, let's translate them into English
house = house.rename(index = str, columns = {'PRIX':'price','SUPERFICIE': 'area','CHAMBRES': 'rooms', 
                         'SDB': 'bathroom', 'ETAGES': 'floors','ALLEE': 'driveway',
                         'SALLEJEU':'game_room', 'CAVE': 'cellar', 
                         'GAZ': 'gas', 'AIR':'air', 'GARAGES': 'garage', 'SITUATION': 'situation'})

# We now instatiate a Linear Regression object
lm = LinearRegression()

# let's do the split of the dataset
house.columns
house.head()
X = house[['area', 'rooms', 'bathroom', 'floors', 'driveway', 'game_room',
       'cellar', 'gas', 'air', 'garage', 'situation']]
y = house['price']

# X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.3, random_state=101)

# Now let's build the model using sklearn
# lm.fit(X_test,y_test)

# predictions = lm.predict(X_test)

# joblib.dump(lm,'regression_model.pkl')
