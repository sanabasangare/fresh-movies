import fresh_tomatoes
import media

suicide_squad = media.Movie("Suicide Squad",
                            "A secret government agency recruits"
                            " imprisoned supervillains to execute"
                            " dangerous black ops missions in "
                            "exchange for clemency",
            " https://upload.wikimedia.org/wikipedia/en/5/50/Suicide_Squad_%28film%29_Poster.png",  # NOQA
            "https://www.youtube.com/watch?v=BKMgB01MU-w")
matrix_reloaded = media.Movie("Matrix Reloaded",
                            "Matrix Reloaded is the first sequel to The Matrix,"
                            " and the second installment in The Matrix trilogy",
            "https://upload.wikimedia.org/wikipedia/en/b/ba/Poster_-_The_Matrix_Reloaded.jpg",  # NOQA
            "https://www.youtube.com/watch?v=HVrGMnk5E_M")
nerve = media.Movie("Nerve",
                    "Are you a watcher or a player of the game?",
            "https://upload.wikimedia.org/wikipedia/en/e/e2/Nerve_2016_poster.jpg",  # NOQA
            "https://www.youtube.com/watch?v=2PR9MOPTI7g")
sing = media.Movie("Sing",
                    "In a world populated by all animals,"
                    " a koala named Buster Moon works to keep"
            " his theater from closing down",
            "https://upload.wikimedia.org/wikipedia/en/b/bb/Sing_%282016_film%29_poster.jpg",  # NOQA
            "https://www.youtube.com/watch?v=9qPgK_u4vX8")
ted_2 = media.Movie("Ted 2",
                    "The sequel to the 2012 film Ted by Seth MacFarlane",
            "https://upload.wikimedia.org/wikipedia/en/2/24/Ted_2_poster.jpg",  # NOQA
            "https://www.youtube.com/watch?v=S3AVcCggRnU")
jack_reacher = media.Movie("Jack Reacher",
                            "Jack Reacher returns to the headquarters of his old unit",
            "https://upload.wikimedia.org/wikipedia/en/0/05/Jack_Reacher_Never_Go_Back_poster.jpg",  # NOQA
            "https://www.youtube.com/watch?v=aRwrdbcAh2s")

movies = [suicide_squad, matrix_reloaded, nerve, sing, ted_2, jack_reacher]
fresh_tomatoes.open_movies_page(movies)
