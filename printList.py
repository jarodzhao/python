def print_movie (the_movies, level=0):
    for movie in the_movies:
        if isinstance(movie,list):
            print_movie(movie,level+1)
        else:
            for tab in range(level):
                print('\t', end='')
            print(movie)