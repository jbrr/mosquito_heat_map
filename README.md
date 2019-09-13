**BZZZZZ**

# Mosquito Heat Map
This is going to map out data from NEON operated CO^2 mosquito traps and plot it on a map. The end goal is we'll be able to see where disease carrying mosquito species have spread to in the US. We'll also be able to see more up-to-date maps of where species are located around the country. With climate change, maps published in identification guides are (apparently) already out of date.

### Requirements
Most dependencies are wrapped up in this repository, but not everything.
* Python 3
* PostGIS Postgres extension (still trying to figure out how to add that extension programatically)
* Raw data. You can download this on the [NEON website](https://data.neonscience.org/browse-data). You'll need to filter on "Organisms, Populations, and Communities", select "Mosquitoes sampled from CO2 traps". Download the expanded data set, then use the `NeonIngestor` to ingest files matching the `*mos_expertTaxonomistIDProcessed*` pattern for identification data, and `*mos_trapping*` for location data. NEON has a slick looking API as well, which might be useful for updating the dataset as more is published, but I didn't want to hit the API a million times for the first, historical ingest.

### Development
There's a bit of weirdness. Hopefully I can get some of this ironed out at some pont.

#### Server
* Because I didn't add the PostGIS extension programatically, `alembic` keeps trying to drop the table that's' created when you install the extension, specifically `spatial_ref_sys`. So every time you create a new migration, you have to go edit it so it doesn't drop the table.
* There are a few required env vars. I use `autoenv` to handle them, but whatevs
* * `DATABASE_URL`: Local Postgres instance for dev.
* * `APP_SETTINGS`: For dev, `"config.DevelopmentConfig"`
* * `FLASK_APP`: `src/server/app.py`
* * `FLASK_ENV`: `development`

#### Client
* I use `dotenv` to handle build variables, but as mentioned, I also use `autoenv` for the server side. Thus, Webpack is configured to look at `src/client/.env` instead of `.env` in the root folder.
* * `API_ROOT`: Your server's local address for dev.

### Acknowledgement
The National Ecological Observatory Network is a program sponsored by the National Science Foundation and operated under cooperative agreement by Battelle Memorial Institute. This material is based in part upon work supported by the National Science Foundation through the NEON Program.
https://neonscience.org