"""Stores details of movies and displays them on a website."""
import main
import media

def main():
	"""Creates six Movie objects, initialising these objects with title, storyline,
    poster image link, video trailer and link """
    
 	I_Feel_Pretty = media.Movie("I Feel Pretty",
    							"A woman struggling with insecurity wakes from a fall believing she is the most beautiful and capable woman on the planet. Her new confidence empowers her to live fearlessly, but what happens when she realizes her appearance never changed?",
								"https://upload.wikimedia.org/wikipedia/en/2/2b/I_Feel_Pretty.png",
								"https://youtu.be/cVx9EFK3DWE")

	Mission_Impossible = media.Movie("Mission Impossible",
									"Ethan Hunt and his IMF team, along with some familiar allies, race against time after a mission gone wrong.",
									"https://upload.wikimedia.org/wikipedia/en/f/ff/MI_–_Fallout.jpg",
									"https://youtu.be/wb49-oV0F78")

	Avengers =  media.Movie("Avengers",
							"The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe.",
							"https://upload.wikimedia.org/wikipedia/ar/f/f0/Avengers-Infinity_War.jpg",
							"https://youtu.be/6ZfuNTqbHE8")

	Hotel_Transylvania = media.Movie("Hotel Transylvania",
									"Dracula, who operates a high-end resort away from the human world, goes into overprotective mode when a boy discovers the resort and falls for the count's teenaged daughter.",
									"https://upload.wikimedia.org/wikipedia/en/f/f5/HotelTransylvania.jpg",
									"https://youtu.be/Ku52zNnft8k")

	Ocean_Eight = media.Movie("Ocean's Eight ",
							"Debbie Ocean gathers an all-female crew to attempt an impossible heist at New York City's yearly Met Gala.",
							"https://upload.wikimedia.org/wikipedia/ar/d/dd/OceansEightPoster.jpeg",
							"https://youtu.be/n5LoVcVsiSQ")

	Skyscraper = media.Movie("Skyscraper",
							"A security expert must infiltrate a burning skyscraper, 225 stories above ground, when his family is trapped inside by criminals."
							"https://upload.wikimedia.org/wikipedia/en/6/6e/Skyscraper_%282018%29_film_poster.png",
							"https://youtu.be/t9QePUT-Yt8")
	# Store the Movie objects in a list.
	movies = [I_Feel_Pretty,Mission_Impossible,Avengers,Hotel_Transylvania,Ocean_Eight,Skyscraper]
	# Open the movie website in the user's browser, featuring the movies above.
	main.open_movies_page(movies)

if __name__ == '__main__':
    main()