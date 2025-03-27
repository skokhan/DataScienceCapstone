# Data Collection​

## SpaceX REST API​
The SpaceX launch data used in the analysis is gathered utilizing the GET request for the SpaceX REST API. This API provides data about past launches, including details about the rocket used, the payload delivered, launch specifications, landing specifications, and landing outcomes. ​

We use the endpoint [api.spacexdata.com/v4/launches/past](https://api.spacexdata.com/v4/launches/past) to access launch data. By performing a GET request with the requests library, we retrieve this data, which is provided in a structured JSON format. To make the JSON data more usable for visualization and analysis, we normalize it into a flat table.​ We transform the raw data into a clean dataset by performing data wrangling with the API, sampling the data, and addressing any NULL values. Finally, we convert the cleaned data into a Pandas DataFrame and export it to a CSV file.​

### Space REST API flowchart 
<img src="https://github.com/skokhan/DataScienceCapstone/blob/803d59f0a654bff0aba09b9c01dbeaaf8cfe3cda/Data%20Collection/SpaceX%20API.png" data-canonical-src="https://github.com/skokhan/DataScienceCapstone/blob/803d59f0a654bff0aba09b9c01dbeaaf8cfe3cda/Data%20Collection/SpaceX%20API.png" width="50%"/>

## Web Scraping Falcon 9 Launch Records​
Additionally, data is extracted from related Falcon 9 Wiki pages using the Python BeautifulSoup package. This process involves gathering information from relevant HTML tables that contain important records of Falcon 9 launches. ​

We then parse the data from these tables and convert it into a flat table format, specifically a Pandas DataFrame, ensuring that it is structured for effective analysis and visualization before exporting it to a CSV file.​

### Web Scraping flowchart 
<img src="https://github.com/skokhan/DataScienceCapstone/blob/803d59f0a654bff0aba09b9c01dbeaaf8cfe3cda/Data%20Collection/Web%20Scraping.png" data-canonical-src="https://github.com/skokhan/DataScienceCapstone/blob/803d59f0a654bff0aba09b9c01dbeaaf8cfe3cda/Data%20Collection/Web%20Scraping.png" width="50%"/>
