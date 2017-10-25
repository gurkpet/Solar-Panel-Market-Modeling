# Predicting Solar Panel Installation Markets

In this project, a model was built using demographic data including median age, home value, income, as well as percent of homes lived in by owner and enviornmental data referencing amount of solar radiation for each zip code in the model. The intent of the project is to identify zip codes where the population had a higher rate of solar panels per capita than the rest of the country based on the previously mentioned inputs, thus ideally identifying the type of market where the sale of solar panels would be easier than others.

In this project a [2 class version of the map](http://htmlpreview.github.io/?https://github.com/gurkpet/Solar-Panel-Market-Modeling/blob/master/2classmarketprediction.html) and a [3 class version of the map](http://htmlpreview.github.io/?https://github.com/gurkpet/Solar-Panel-Market-Modeling/blob/master/3classmarketprediction.html) were generated.  Green and red in both maps identifying good and bad markets respectively.  In the 3 class version, a medium market class was added to identify markets that straddle the line between the two classes.  

As contrast [here is a plot of just the training data](http://htmlpreview.github.io/?https://github.com/gurkpet/Solar-Panel-Market-Modeling/blob/master/3classmarketpredictionalltrain.html)

Also generated is a [3 class version of the map, training data included in plotting](https://github.com/gurkpet/Solar-Panel-Market-Modeling/blob/master/3classmarketpredictionwithtrain.html).  The training data was plotted along with the predicted data in this map because from a business perspective it still generates interesting information as a whole.  This map is too complex to be rendered through the github html previewer.  Feel free to download and explore locally but be aware it will be computationally expensive for your computer and it might hang when you zoom too close.  For those of you with limited computational power a screenshot of the map zoomed out is available below.

![This was a fun project, thanks for checking it out](Model_with_training_data.jpg?raw=true "3 class version of the map, training data included in plotting")
