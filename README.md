# dashboard

This will hopefully evolve into a personal "magic mirror" style dashboard. Currently, it's a partial python implementation of the BusTime API as used by http://portauthority.org.

## Configuration Files

### config.py
The script pulls API information from here.  You'll need an API key for your preferred provider's feed.  See `config.sample.py`. 

### routes.csv

The script will read a `routes.csv` file that is comma-separated, with one triple on each line, as follows:

    rt,stpid,dir

That is, Route (in my case, the route number, e.g. 71A), numeric Stop ID, which can actually be found at most stops on the BusStop sign; and Direction (Though, this currently does nothing.)  See `routes.csv.sample`.
