# Hannah Hodges
# CS 151, Dr. Rajeev
# Lab 9
# 11/ 18/2021
# main function to run the program
def main():
    load_movie_data()


# function to get input and sort movie data into lists
def load_movie_data():
    file = input("Enter the name:")
    titles = []
    movie_list = []
#try and except used and excpet if the file is not found
    try:
        with open(file, 'r') as moviesdata:
            movies = moviesdata
            titles = movies.split(",")
            count = 1
            for movie in movies:
                movie_list = []
                movie_details = movie.split(",")
                try:
                    movie_list.append(movie_list)
                except:
                    print("Data error")
    except:
        print("No file found")
        # column to add profits
        add_profit_column(titles, movie_list)


# sorts movie data based off of gross and the budget of the movies
def add_profit_column(titles, movie_list):
    titles.append("Profit")
    for movie in movie_list:
        print_min_and_max_profit(titles, movie_list)


# function to sort the movies based off of the highest and lowest profit
def print_min_and_max_profit(titles, movie_list):
    # to find the minimum and maximum profit
    min_profit = float("")
    max_profit = float("")
    count = 0
    for movie in movie_list:
        if (movie > max_profit):
            max_profit = movie
        if (movie < min_profit):
            min_profit = movie
            count += 1
    highest = ''
    lowest = ''
    print("The highest profit movie", highest)
    print("The lowest profit movie", lowest)
    save_movie_data(titles, movie_list)

# saves data
def save_movie_data(titles, movie_list):
    output = input("Enter the filename to save the movie data with .csv extension: ")
    titles = ("," + (titles))


main()
