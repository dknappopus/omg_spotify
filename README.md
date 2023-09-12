# Description
Repo for code that uses Spotify API

## Steps to Run - first time
1) Open Terminal and navigate to where you want to store the code
2) Clone Repo `git clone https://github.com/dknappopus/omg_spotify.git`
3) navigate to repo `cd ./omg_spotify`
4) Add input file to repo
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
