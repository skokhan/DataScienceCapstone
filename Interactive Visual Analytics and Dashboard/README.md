# Interactive Visual Analytics with Folium

The success rate of rocket launches may depend on the location and proximity of the launch site, particularly concerning the initial trajectories of the rockets. Identifying an optimal location for building a launch site involves many factors, and analyzing existing launch site locations may help us uncover some of these factors.

To illustrate our findings, we use Folium to create an interactive map, marking the locations of the launch sites and their nearby areas. We follow these key steps:​

- ### Mark All Launch Sites​
  We add the locations of each site on the map using their latitude and longitude coordinates, marking each site with a circle.​

- ### Mark Success and Failed Launches for Each Site​
  Each launch occurs at one of the four launch sites, which means that many launch records will share the same coordinates. To simplify the map clutter caused by overlapping markers, we employ marker clusters. Successful launches are represented with green markers, while failed launches are indicated by red markers. This allows us to easily identify which sites have high success rates.​
- ### Calculate Distances Between Launch Sites and Nearby Locations​
  We explore the map for significant nearby proximities and use the Haversine formula to compute distances between locations. Polylines are added to the map to annotate proximities along with their respective distances.​

Ultimately, our goal is to explain how to choose an optimal launch site.​

# Interactive Dashboard with Ploty Dash

By utilizing an interactive analytics approach, we can quickly and effectively identify visual patterns. We develop a dashboard application using the Python Plotly Dash package. This dashboard enables us to extract insights from the SpaceX dataset more easily compared to traditional static graphs.

The dashboard features input components, including a dropdown list for launch sites and a slider for payload range, enabling interaction with a pie chart and a scatter plot.​

- ### Launch Site Dropdown List​
  There are four different launch sites, and we would like to first determine which one has the highest success count. After that, we can select a specific site to examine its detailed success rate. ​
- ### Payload Range Slider​
  We explore whether the variable payload is correlated with mission outcomes. Using the dashboard, we can easily select different payload ranges to identify any visual patterns. ​
- ### Pie Chart​
  We utilize a pie chart to visualize the total number of successful launches. If a specific launch site is selected, the pie chart displays both the success count and the failure count for that site.​
- ### Scatter Plot​
  The scatter plot allows us to visually observe the correlation between payload and mission outcomes for selected sites. Additionally, we incorporate color labels for each scatter point based on the booster version, enabling us to observe mission outcomes across different boosters.​
