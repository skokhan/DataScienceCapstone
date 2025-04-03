# Interactive Visual Analytics with Folium

The success rate of rocket launches may depend on the location and proximity of the launch site, particularly concerning the initial trajectories of the rockets. Identifying an optimal location for building a launch site involves many factors, and analyzing existing launch site locations may help us uncover some of these factors. ​
To illustrate our findings, we use Folium to create an interactive map, marking the locations of the launch sites and their nearby areas. We follow these key steps:​

- ### Mark All Launch Sites​
  We add the locations of each site on the map using their latitude and longitude coordinates, marking each site with a circle.​

- ### Mark Success and Failed Launches for Each Site​
  Each launch occurs at one of the four launch sites, which means that many launch records will share the same coordinates. To simplify the map clutter caused by overlapping markers, we employ marker clusters. Successful launches are represented with green markers, while failed launches are indicated by red markers. This allows us to easily identify which sites have high success rates.​
- ### Calculate Distances Between Launch Sites and Nearby Locations​
  We explore the map for significant nearby proximities and use the Haversine formula to compute distances between locations. Polylines are added to the map to annotate proximities along with their respective distances.​

Ultimately, our goal is to explain how to choose an optimal launch site.​

# Interactive Dashboard with Ploty Dash
