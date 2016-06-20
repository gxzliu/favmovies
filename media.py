#********
# George Liu
# 6.20.16
# A class that includes various properties of a movie.
#********

import webbrowser

class Movie():
	
	"""This class stores movie-related information"""

	def __init__(self, movie_title, movie_storyline, poster_image, rt_rating, trailer_youtube):
		
		#instance variables represent various properties of movies
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
		self.rating = rt_rating

	#instance method opens the trailer
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)