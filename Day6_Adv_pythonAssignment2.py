class MovieLibrary:
    available_movies = ["Inception", "Titanic", "Avatar"]

    def __init__(self, member_name):
        self.member_name = member_name
        self.borrowed_movies = []

    def borrow_movie(self, movie):
        # Borrow movie if available
        if movie in MovieLibrary.available_movies:
            MovieLibrary.available_movies.remove(movie)
            self.borrowed_movies.append(movie)
            print(f"{self.member_name} borrowed '{movie}'.")
        else:
            print(f"'{movie}' not available.")

    def return_movie(self, movie):
        # Return movie to library
        if movie in self.borrowed_movies:
            self.borrowed_movies.remove(movie)
            MovieLibrary.available_movies.append(movie)
            print(f"{self.member_name} returned '{movie}'.")

    def view_borrowed_movies(self):
        # Show borrowed movies
        print(f"{self.member_name}'s borrowed movies: {self.borrowed_movies}")

# Test case
user = MovieLibrary("John")
user.borrow_movie("Inception")
user.view_borrowed_movies()
user.return_movie("Inception")
user.view_borrowed_movies()

'''
John borrowed 'Inception'.
John's borrowed movies: ['Inception']
John returned 'Inception'.
John's borrowed movies: []
'''
