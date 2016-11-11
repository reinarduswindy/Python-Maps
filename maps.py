import googlemaps
from datetime import datetime

def get_direction(origin, destination, mode):
	gmaps = googlemaps.Client(key='AIzaSyC8aRFSQ2raJvoIJn22RqvtzR-ou4Lo1MY')
	now = datetime.now()
	if not mode:
		mode = "walking"

	directions_result = gmaps.directions(origin, destination, mode=mode, departure_time=now)
	return directions_result
