import media
import fresh_tomatoes

deadpool = media.Movie(
        "Deadpool",
        "Man get cures from cancer resulting in super powers",
        "https://www.cinematerial.com/media/posters/md/7a/7ajvdavw.jpg?v=1456368002", # noqa
        "https://www.youtube.com/watch?v=ZIM1HydF9UA")

hunger_games = media.Movie(
        "Hunger Games",
        "In corrupt society, a girl starts a rebellion",
        "https://images-na.ssl-images-amazon.com/images/I/51OGv-AnD6L.jpg", # noqa
        "https://www.youtube.com/watch?v=mfmrPu43DF8")

avengers = media.Movie(
        "Avengers",
        "Group of super heroes group together to defeat a common enemy",
        "http://screencrush.com/files/2015/02/avengers-2-poster-hi-res.jpg", # noqa
        "https://www.youtube.com/watch?v=eOrNdBpGMv8")

doctor_strange = media.Movie(
        "Doctor Strange",
        "Prestigous doctor loses his ability to use his hands, but gains supernatural powers",
        "http://static.srcdn.com/wp-content/uploads/Doctor-Strange-Poster.jpg", # noqa
        "https://www.youtube.com/watch?v=HSzx-zryEgM")

star_trek = media.Movie(
        "Star Trek",
        "Admiral of a starship goes on a journey",
        "http://3.bp.blogspot.com/-UB3u4fAXFJY/UemEN-dZSiI/AAAAAAAATLw/ZzTeo3EPln0/s1600/Star+Trek+Into+Darkness+DVD.jpg", # noqa
        "https://www.youtube.com/watch?v=QAEkuVgt6Aw")

dark_knight = media.Movie(
        "Dark Knight",
        "Batman saves the day from Joker",
        "http://host.trivialbeing.org/up/tdk-jul1-dark-knight-poster-stupidbats.jpg", # noqa
        "https://www.youtube.com/watch?v=EXeTwQWrcwY")

movies = [
        deadpool,
        hunger_games,
        avengers,
        doctor_strange,
        star_trek,
        dark_knight]

#Create website based on movies
fresh_tomatoes.open_movies_page(movies)
