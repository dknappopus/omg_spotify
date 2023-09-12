# Description
Repo for code that uses Spotify API

How it works: given a record, the code will generate queries to execute in the spotify search API. For example, if the song name is 'Hotel in Sydney' and the artist is 'Hopsin', then the code will create a query, 'track: Hotel in Sydney artist: Hospin' and return the resulting ISRC. The code executes this for all records in the input file, and outputs a csv with the ISRC filled in. If there is an error or no match is found, the resulting ISRC will be 'Not Found'
Sometimes there may be issues where multiple artists are on a song. In this case, a query is constructed for each artist on the song. For example, in the song 'FV Till I Die' with the artst 'Hopsin, SwizZz', two queries are constructed, one where the artist is Hopsin and one where the artist is SwizZz. This should increase the chances of a successful search.

If there are 'Not Found' ISRCs in the output file, you should verify that the titles and artists are correct or manually look up the ISRCs.

## Steps to Run - first time
1) Open Terminal and navigate to where you want to store the code
2) Clone Repo `git clone https://github.com/dknappopus/omg_spotify.git`
3) navigate to repo `cd ./omg_spotify`
4) Add input file `<input_file_name.xlsx>` to repo
5) Open Terminal
6) Create virtual environment
   `python -m venv spotify_venv`
7) Activate virtual environment
   `./spotify_venv/Scripts/activate`
8) Install required packages (this will take a few minutes on first install)
    `pip install -r requirements.txt`
9) Run python
    `python spotify_isrc_lookup.py <input_file_name.xslx>`
10) file will be saved as input_data_isrc.csv

## known issues
- you may have to edit your registry if you get a 'file path too long error' on install. steps to do that:
  1) Press `Win + R` on your keyboard to open the Run dialog box
  2) Type `regedit` and press Enter to open the Windows Registry Editor
  3) In the Registry Editor, navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem
  4) In the right pane, find (or create if it doesn't exist, but most likely should exist) a DWORD (32-bit) Value named 'LongPathsEnable'
  5) Set its value data to '1'
  6) Click OK
  7) Restart Computer
- you must have a role in azure assigned to be able to use Azure Secrets. This is how we securely share credentials like the Spotify API password
