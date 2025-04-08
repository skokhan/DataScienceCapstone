# Data Collection​

## SpaceX REST API​
The SpaceX launch data used in the analysis is gathered utilizing the GET request for the SpaceX REST API. This API provides data about past launches, including details about the rocket used, the payload delivered, launch specifications, landing specifications, and landing outcomes. ​

We use the API endpoints to access specific data for each launch. By performing a GET request with the requests library, we retrieve data, which is provided in a structured JSON format. To make the JSON data more usable for visualization and analysis, we normalize it into a flat table. We transform the raw data into a clean dataset. Filter the data focusing solely on Falcon 9 booster launches. Address any NULL values by replacing them with the mean values and applying a one-hot encoding algorithm. Finally, we convert the cleaned data into a Pandas DataFrame and export it to a CSV file.​

### Data Collection by using SpaceX REST API flowchart 
<img alt="SpaceX REST API flowchart" src="https://github.com/skokhan/DataScienceCapstone/blob/090b6c1cd8e9bed3189cb58e976f7360f275d351/Data%20Collection/SpaceX%20API.png" data-canonical-src="https://github.com/skokhan/DataScienceCapstone/blob/090b6c1cd8e9bed3189cb58e976f7360f275d351/Data%20Collection/SpaceX%20API.png" width="50%"/>

## Web Scraping Falcon 9 Launch Records​
Additionally, data is extracted from related Falcon 9 Wiki pages using the Python BeautifulSoup package. This process involves gathering information from relevant HTML tables that contain important records of Falcon 9 launches. ​

We then parse the data from these tables and convert it into a flat table format, specifically a Pandas DataFrame, ensuring that it is structured for effective analysis and visualization before exporting it to a CSV file.​

### Data Collection by using Web Scraping flowchart 
<img alt="Web scraping flowchart" src="https://github.com/skokhan/DataScienceCapstone/blob/af372f8b6426a32c8c19fb9123ef2903f95170c9/Data%20Collection/Web%20Scraping.png" data-canonical-src="https://github.com/skokhan/DataScienceCapstone/blob/af372f8b6426a32c8c19fb9123ef2903f95170c9/Data%20Collection/Web%20Scraping.png" width="50%"/>
