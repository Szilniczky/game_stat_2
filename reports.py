import math
# Report functions


def get_most_played(file_name):
    with open(file_name, "r") as f:
        topTitle = 0
        topCopiesSold = 0
        for line in f:
            title = line.split("\t")[0]
            copiesSold = line.split("\t")[1]
            if float(copiesSold) > float(topCopiesSold):
                topCopiesSold = copiesSold
                topTitle = title
        return topTitle


def sum_sold(file_name):
    with open(file_name, "r") as f:
        sumOfCopies = 0
        for line in f:
            copies = line.split("\t")[1]
            sumOfCopies = sumOfCopies + float(copies)
        return sumOfCopies


def get_selling_avg(file_name):
    with open(file_name, "r") as f:
        sumOfCopies = 0
        countOfGames = 0
        for line in f:
            copies = line.split("\t")[1]
            sumOfCopies = sumOfCopies + float(copies)
            countOfGames = countOfGames + 1
        return float(sumOfCopies) / float(countOfGames)


def count_longest_title(file_name):
    with open(file_name, "r") as f:
        longestTitle = ""
        longestTitleLength = 0
        for line in f:
            title = line.split("\t")[0]
            if len(title) > longestTitleLength:
                longestTitleLength = len(title)
                longestTitle = title
        return longestTitleLength


def get_date_avg(file_name):
    with open(file_name, "r") as f:
        sumOfYears = 0
        countOfGames = 0
        for line in f:
            copies = line.split("\t")[2]
            sumOfYears = sumOfYears + float(copies)
            countOfGames = countOfGames + 1
        return math.ceil(sumOfYears / countOfGames)


def get_game(file_name, title):
    with open(file_name, "r") as f:
        for line in f:
            currentTitle = line.split("\t")[0]
            if currentTitle == title:
                gameCopiesSold = line.split("\t")[1]
                gameYear = line.split("\t")[2]
                gameGenre = line.split("\t")[3]
                # we use strip() because we want to get rid of the "\n"
                gamePublisher = line.split("\t")[4].strip()
                game = [currentTitle, float(gameCopiesSold), int(
                    gameYear), gameGenre, gamePublisher]
                return game
