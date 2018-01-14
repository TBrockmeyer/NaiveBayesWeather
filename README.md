# NaiveBayesWeather

This code snippet provides the statistically most probable human evaluation of a certain weather condition, based on values of four weather-related properties from nine days.
The file trainingsdaten.arff contains data the prediction is based on:
* (      "Overclouding"  "Temperature" "Humidity"     "Wind" "Evaluation")
* 4      b'"sonnig"'  b'"niedrig"'    b'"normal"'    b'"ja"'      b'"-"'
* 5  b'"regnerisch"'  b'"niedrig"'      b'"hoch"'    b'"ja"'      b'"-"'
* 6    b'"bewoelkt"'     b'"hoch"'      b'"hoch"'    b'"ja"'      b'"-"'
* 7      b'"sonnig"'   b'"mittel"'    b'"normal"'  b'"nein"'      b'"+"'
* 8    b'"bewoelkt"'   b'"mittel"'      b'"hoch"'    b'"ja"'      b'"-"'

The code snippet currently "predicts" the human evaluation of the following weather condition pattern:
* regnerisch, mittel, hoch, nein (rainy, medium, high, no)
with Naive Bayes.

Given these conditions, probabilities of positive and negative evaluation are calculated:
* P(plus|regnerisch, mittel, hoch, nein) = 0 %
* P(minus|regnerisch, mittel, hoch, nein) = 100 %

Thus, here, the human evaluation of a rainy day with medium temperature, high humidity and without wind is most probably negative.
