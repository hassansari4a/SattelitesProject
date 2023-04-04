import requests
import os
from dotenv import load_dotenv
from spacetrack import SpaceTrackClient

load_dotenv()

# st = SpaceTrackClient(os.getenv('SPACE_TRACK_USERNAME'), os.getenv('SPACE_TRACK_PASSWORD'))
st = SpaceTrackClient('hassansari4a@gmail.com', '9817377317NCELL')

print(st.tle_latest(norad_cat_id=[25544, 41335], ordinal=1, format='tle'))