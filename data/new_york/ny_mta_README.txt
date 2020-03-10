The data containing information about New York MTA subway turnstile usage is in the folder "ny_turnstile_2019" on the Repo. This folder contains 12 separate files, each containing information on New York subway turnstile usage for a month in 2019. There is also a sample of the data in turnstile_sample.tsv

The ridership data was publicly available on New York MTA's website as text files. Sources: http://web.mta.info/developers/turnstile.html
http://web.mta.info/developers/MTA-Subway-Time-historical-data.html
We downloaded all the files for 2019 MTA ridership information. We also downloaded data from the same site containing information of MTA stations across the city. We joined these two datasets by matching each entry in the ridership data with the corresponding longitude/latitude coordinate from the station information data. The subway data was hosted on AWS and was available in gtfs-realtime format. 


—————————————————————————————————————
Columns:
- location: the name of the subway station
- entries: the number of entries at turnstiles of this station, over the course of the month that the dataset encompasses
- exits: the number of exits at turnstiles of this station, over the course of the month that the dataset encompasses
- latitude/longitude: coordinate of the subway station

—————————————————————————————————————
Sample file:
The sample includes the first 20 rows of turnstile_1912.tsv, which represents turnstile usage for these 20 stations over the month of December, 2019. This sample is 20 rows out of 250 rows of this dataset for December turnstile usage. The sample should be representative of the entire New York subway turnstile data, since the population (eg. residents and tourists) in a metropolis as New York across a year does not vary too much. 
