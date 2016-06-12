# kaggle-kobe-bryant-shot-selection
This repository contains the code for the kaggle project Kobe Bryant shot seleciton: 
https://www.kaggle.com/c/kobe-bryant-shot-selection

Here is the description of the competition:
##########
Which shots did Kobe sink?

Kobe Bryant marked his retirement from the NBA by scoring 60 points in his final game as a Los Angeles Laker on Wednesday, April 12, 2016. Drafted into the NBA at the age of 17, Kobe earned the sport’s highest accolades throughout his long career.

Using 20 years of data on Kobe's swishes and misses, can you predict which shots will find the bottom of the net? This competition is well suited for practicing classification basics, feature engineering, and time series analysis. Practice got Kobe an eight-figure contract and 5 championship rings. What will it get you?
##########

To solve the puzzle, I first calculated the success rate of all shots or a specific type of shots (e.g., jump shot) with the python script add-fields.py. Then, I used random forest or lasso regression (sol.R) to predict the probability of successful shots.
