#********
# George Liu
# 6.20.16
# A list of objects of movie class that connects to fresh_tomatoes.py
#********

import media
import fresh_tomatoes

#movies and their specific info
inception = media.Movie("Inception",
						"Inception is about implanting ideas into the subconscious.", 
						"http://www.impawards.com/2010/posters/inception.jpg", 
						"Rotten Tomato Rating: 86%",
						"https://www.youtube.com/watch?v=8hP9D6kZseM")

giftshop = media.Movie("Exit Through The Gift Shop", 
						"Exit Through The Gift Shop is about a street artist named Thierry Guetta.", 
						"https://filmwonk.files.wordpress.com/2011/01/2010glennies-bp-05-exitthroughthegiftshop.jpg",
						"Rotten Tomato Rating: 96%", 
						"https://www.youtube.com/watch?v=oHJBdDSTbLw")

interstellar = media.Movie("Interstellar", 
							"Interstellar is about astronauts that look for a new home for humanity.", 
							"http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/interstellar3.jpg",
							"Rotten Tomato Rating: 71%", 
							"https://www.youtube.com/watch?v=Lm8p5rlrSkY")

dope = media.Movie("Dope", 
					"Dope is a coming-of-age film about a high school geek from Inglewood.",
					"http://www.impawards.com/2015/posters/dope_ver2.jpg",
					"Rotten Tomato Rating: 88%",
					"https://www.youtube.com/watch?v=strEm9amZuo")

inherent = media.Movie("Inherent Vice", 
					"Inherent Vice is about a detective that investigates the LA criminal underworld.",
					"http://ia.media-imdb.com/images/M/MV5BMjI2ODQ2NzUwMl5BMl5BanBnXkFtZTgwNjU3NTE4MjE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
					"Rotten Tomato Rating: 74%",
					"https://www.youtube.com/watch?v=wZfs22E7JmI")

wolf = media.Movie("The Wolf of Wall Street", 
					"The Wolf of Wall Street is about the excesses of Wall Street greed.",
					"http://www.yifysub.com/wp-content/uploads/2015/08/Wolf_Wallstreet_itunes_Movie_Pack.jpg",
					"Rotten Tomato Rating: 77%",
					"https://www.youtube.com/watch?v=iszwuX1AK6A")

#gather movies into list to feed into fresh_tomatoes
movies = [inception, interstellar, dope, inherent, wolf, giftshop]

#feed into open_movies_page() function that generates an html file 
fresh_tomatoes.open_movies_page(movies)