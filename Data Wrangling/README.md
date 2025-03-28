# Data Wrangling 

The data set includes various instances where the booster did not land successfully. In some cases, a landing was attempted but failed due to an accident. Here are the definitions of the outcomes:

- "True Ocean" indicates that the mission successfully landed in a specific region of the ocean, while "False Ocean" means the mission did not land successfully in that area;
- "True RTLS" means the mission successfully landed on a ground pad, while "False RTLS" indicates an unsuccessful landing on a ground pad;
- "True ASDS" signifies that the mission successfully landed on a drone ship, whereas "False ASDS" means the mission did not land successfully on a drone ship.

We primarily convert these outcomes into training labels, where a label of 1 signifies a successful landing and a label of 0 indicates an unsuccessful landing.
