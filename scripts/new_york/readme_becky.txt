### Instructions for scraping MTA data ###
-- Historical Bus Time --
1. Download data from AWS (links are in MTA data portal) into a directory on the department machine. Or, download it on your local machine and SCP it over to the department machine.
2. Run ```unxz filename.txt.xz``` in the terminal to decompress it into filename.txt.
3. Run scripts/new_york/mta_bus_time.py to read it in to a Pandas dataframe. This might be slow, since the data is large. You'll have to change the filepath to read in your particular file. The script currently just prints descriptive statistics of the data.

Note: You cannot upload the .xz files to GitHub, because they're huge.

-- Historical Subway Time --
1. Use the script mta_subway_time.py to print the gtfs-realtime data for 09:31 AM on Sep 17, 2014. I'm not too familiar with the gtfs-realtime data, but I think we can turn into a JSON format and then use Pandas with it.
  a. You might need to set your Google authorization and ```pip install --upgrade gtfs-realtime-bindings``` for this to work.

Note: I was trying to work with the "roll-up" data (instructions below), but I don't know how to use the gtfs files after they've been extracted. The Google documentation is all about making API calls to a URL, so I'm not certain what to do with the files themselves.
    1. The documentation on the website is wrong. The link to get "roll-up" data for a day is https://datamine-history.s3.amazonaws.com/gtfs-2014-09-17.tgz (replacing the date with your desired YYYY-MM-DD). Download this data onto the department machine, or SCP it over to a department machine.
    2. Run ```tar -xf filename.tgz``` in the terminal to extract it to all of the files associated with that date.
    3. ???

-- Station locations --
Data is directly available at http://web.mta.info/developers/data/nyct/subway/Stations.csv. I didn't bother downloading it, but we can easily download it and mess around with it on Pandas.

-- Fares --
Data is available as CSVs online (here's Feb 22, 2020: http://web.mta.info/developers/data/nyct/fares/fares_200222.csv). Didn't download, can easily work with it on Pandas.

-- Turnstile usage --
Data is available at http://web.mta.info/developers/data/nyct/turnstile/turnstile_200222.txt (and for various other dates). You can get other dates at http://web.mta.info/developers/turnstile.html. For whatever foolish reason, it's a txt file that's comma-separated. Not really a problem, we can still download it and use pd.read_csv. Haven't downloaded it.
