# Data Wrangling 

In the data set, there are several different cases where the booster did not land successfully. Sometimes a landing was attempted but failed due to an accident. For example, 

- True Ocean means the mission outcome was successfully landed to a specific region of the ocean, while False Ocean means the mission outcome was unsuccessfully landed to a specific region of the ocean.
- True RTLS means the mission outcome was successfully landed to a ground pad, while False RTLS means the mission outcome was unsuccessfully landed to a ground pad.
- True ASDS means the mission outcome was successfully landed on a drone ship False ASDS means the mission outcome was unsuccessfully landed on a drone ship.

We mainly convert those outcomes into Training Labels with 1 means the booster successfully landed 0 means it was unsuccessful.
