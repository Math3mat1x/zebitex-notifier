# Zebitex notifier

Change the dictionnary in data.json in order to set a high and low value for a given market (there is an example provided). Once the price of the given markets hits one of either values, you’ll get notified.
Then, the last value of the list for a given market changes to true, which means you won’t be notified again.

Example data.json:

{'btceur': [46000, 38200, false], 'etheur': [3455, 2390, false]}

And:

{'btceur': [46000, 38200, **true**], 'etheur': [3455, 2390, false]}

... means you won't get notified for any price movement in btceur.


You have to manually modify message.py to get notified in your favorite way.
