# Stock Moving Average

This [repo](https://github.com/JordiCorbilla/stock-moving-average) contains the implementation of 3 well-known Moving Average calculations using the built-in methods that Pandas provides. The first method called SMA (Simple Moving Average) can be easily calculated using the rolling method over a specified time step. The second one CMA (Cumulative Moving Average) uses the expanding method which in the calculaiton window includes all the data points until the current point in the calculation. Finally, the third one EMA (Exponential Moving Average) which uses the EWM method (Entropy Weight Method).

Most of the source code is based on my previous work here [Stock prediction using deep neural learning](https://github.com/JordiCorbilla/stock-prediction-deep-neural-learning)

## 1) Simple Moving Average

90 day SMA on Google's stock Price

![](https://github.com/JordiCorbilla/stock-moving-average/raw/master/Alphabet%20Inc_price_SMA.png)

## 2) Cumulative Moving Average

![](https://github.com/JordiCorbilla/stock-moving-average/raw/master/Alphabet%20Inc_price_CMA.png)

## 3) Exponential Moving Average

![](https://github.com/JordiCorbilla/stock-moving-average/raw/master/Alphabet%20Inc_price_EMA.png)
