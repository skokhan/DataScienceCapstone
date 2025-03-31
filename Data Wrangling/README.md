# Data Wrangling 

The SpaceX data includes several launch facilities: ​
- Cape Canaveral Space Launch Complex 40 (CCAFS SLC 40);​
- Vandenberg Air Force Base Space Launch Complex 4E (VAFB SLC 4E);​
- Kennedy Space Center Launch Complex 39A (KSC LC 39A). ​

Each launch is aimed at reaching a specific orbit, and a variety of orbit ​types are illustrated in the accompanying plot. ​

The dataset also contains multiple instances where the booster did not land ​successfully. In some cases, a landing was attempted but failed due to an ​accident. ​

As part of our exploratory data analysis, we identify a set of unsuccessful landing outcomes where the second stage did not land successfully. We define both successful and unsuccessful landing outcomes and convert these outcomes into a classification variable. This variable will represent the result of each launch and will serve as the training labels. A label of 1 indicates a successful landing, while a label of 0 signifies an unsuccessful landing.
