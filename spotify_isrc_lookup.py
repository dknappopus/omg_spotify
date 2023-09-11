import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import json
import numpy as np
import pandas as pd
import requests

import openpyxl
from openpyxl import load_workbook
import os

from itertools import product

import sys


os.getcwd()

def config_spotify():
    config = '{"cid": "a8a94da4709b43a9a97f09ebe3f7f5c7"\
                    ,"secret": "6e19fc0b10234e4283dd9a02b5f88aa0"}'
    return json.loads(config)

cred_sp = config_spotify()

cid = cred_sp["cid"]
secret = cred_sp["secret"]
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret,requests_timeout = 10)
# client_credentials_manager.get_access_token()
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

df = pd.read_excel(sys.argv[1],sheet_name="Input Details")

def isrc_spotify_lookup(input_record):
    # get song from row of input file
    input_song = input_record['song_name_api_opus']
    print(input_song)
    # get artists from row of input file
    input_artists = input_record['artist_name_opus'].split(',')
    input_artists = [a.strip() for a in input_artists]
    
    # for a song with multiple artists, create one query for each combination of song title, artist
    query_tuples = list(product([input_song],input_artists))
    sp_query = f'track:{query_tuples[0][0]} artist: {query_tuples[0][1]}'
    # remove apostrophes from query to improve results
    sp_queries = [f'track:{qt[0]} artist: {qt[1]}'.replace("'","") for qt in query_tuples]

    all_matches = list()

    for sq in sp_queries:
        track_results = sp.search(q = sq, type = 'track')
        track_list = track_results['tracks']['items']

        # filter on exact match
        if len(track_list) > 0:
            print(f'At least one match found for query {sq}')
            track_hits = [(t['name'],t['popularity'],t['external_ids']['isrc']) for t in track_list]
            track_hits
            for t in track_hits:
                all_matches.append(t)
        else:
            print(f'No Match Found for query {sq}')
        

    isrc_df = pd.DataFrame(all_matches)
    # break ties if more than one result using highest popularity
    if isrc_df.shape[0] > 0:
        isrc_max_indx = isrc_df[1].idxmax()
        selected_isrc = isrc_df[2][isrc_max_indx]
    else:
        selected_isrc = 'Not Found'
        
    return selected_isrc

isrcs = [isrc_spotify_lookup(row) for idx, row in df.iterrows()]

df['isrc_opus'] = isrcs
df.to_csv('./input_data_isrc.csv')