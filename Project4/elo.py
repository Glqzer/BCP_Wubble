import pandas
import numpy
import matplotlib.pyplot
import random

def calculate_ratings(file_name):
    
    """Parameters:
        file_name: indicates the name of a csv file
        
        Returns:
        Dictionary containing 8 entries where the keys are player names, and the values are the playing ratings"""
    
    #Set initial rating array
    ratings = numpy.array([1500.0, 1500.0, 1500.0, 1500.0, 1500.0, 1500.0, 1500.0, 1500.0])
    
    #Open the csv file
    try:
        dataframe = pandas.read_csv(file_name, index_col = 0)
    
        #Use the data in csv file to update ratings
        for index, row in dataframe.iterrows():
            player_a = row['player_A']
            player_b = row['player_B']
            winner = row['winner']
            
            amount_changed_a = 5 * (1.0 - probability_a(ratings[player_a], ratings[player_b], 100))
            
            amount_changed_b = 5 * (1.0 - probability_b(ratings[player_a], ratings[player_b], 100))
            
            #Adjust ratings if A wins
            if (winner == player_a):
                ratings[player_a] = ratings[player_a] + amount_changed_a
                
                ratings[player_b] = ratings[player_b] - amount_changed_a
        
            #Adjust ratings if B wins
            else:
                ratings[player_b] = ratings[player_b] + amount_changed_b
                
                ratings[player_a] = ratings[player_a] - amount_changed_b
    
    #File Exception Handling
    except:
        print("Error while accessing data in " + file_name)
    
    #Construct the final dictionary
    results = {}
    for i in range(8):
        results[(i)] = ratings[i]
    
    return results

def probability_a(rating_a, rating_b, c):
    
    """Parameters:
        rating_a: rating of player a
        rating_b: rating of player b
        c: scale parameter
    
        Returns:
        Probability that A wins"""
    
    rating_calc = numpy.exp((rating_a - rating_b) / c)
    return rating_calc / (1.0 + rating_calc)

def probability_b(rating_a, rating_b, c):
    
    """Parameters:
        rating_a: rating of player a
        rating_b: rating of player b
        c: scale parameter
    
        Returns:
        Probability that B wins"""
        
    rating_calc = numpy.exp((rating_a - rating_b) / c)
    
    return 1.0 - (rating_calc / (1.0 + rating_calc))

def display_ratings(rating_dict):
    
    """Parameters:
        rating_dict: a dictionary containing 8 entries where the keys are the player names and the values are the player ratings
        
        Returns:
        Creates a bar graph that is projected to a console, and also saved to a new file named projections.pdf displaying the ratinghs of each player"""
    
    fig = matplotlib.pyplot.figure(figsize=(8, 8))
    players = list(rating_dict.keys())
    ratings = list(rating_dict.values())

    # Create a bar graph
    matplotlib.pyplot.bar(players, ratings)
    matplotlib.pyplot.xlabel('Players')
    matplotlib.pyplot.ylabel('Rating')
    matplotlib.pyplot.title('Graph of Player Ratings')
    
    matplotlib.pyplot.tight_layout()
    
    matplotlib.pyplot.savefig('projections.pdf')

    # Show the plot on the console
    matplotlib.pyplot.show()
    
    return

def project_win_probs(rating_dict):
    
    """Parameters: 
        rating_dict: dictionary of 8 entries where the keys are players and the values are their ratings
        
        Returns:
        A dictionary containing 8 entries where they keys are the players and the values are the probabilities of winning the tournament"""
    
    #Create list of player win count
    player_wins = numpy.zeros(8, dtype = numpy.float32)
    
    #Simulate the tournament 100 times
    for i in range(100):
        
        #Player 0 vs 7
        prob_a = probability_a(rating_dict[0], rating_dict[7], 100)
        random_number = random.random()
        if (random_number < prob_a):
            winner_1 = 0
        else:
            winner_1 = 7
        
        #Player 1 vs 6
        prob_a = probability_a(rating_dict[1], rating_dict[6], 100)
        random_number = random.random()
        if (random_number < prob_a):
            winner_2 = 1
        else:
            winner_2 = 6
        
        #Player 2 vs 5
        prob_a = probability_a(rating_dict[2], rating_dict[5], 100)
        random_number = random.random()
        if (random_number < prob_a):
            winner_3 = 2
        else:
            winner_3 = 5
        
        #Player 3 vs 4
        prob_a = probability_a(rating_dict[3], rating_dict[4], 100)
        random_number = random.random()
        if (random_number < prob_a):
            winner_4 = 3
        else:
            winner_4 = 4
        
        #Winner 1 vs Winner 2
        prob_a = probability_a(rating_dict[winner_1], rating_dict[winner_2], 100)
        random_number = random.random()
        if (random_number < prob_a):
            final_1 = winner_1
        else:
            final_1 = winner_2
        
        #Winner 3 vs Winner 4
        prob_a = probability_a(rating_dict[winner_3], rating_dict[winner_4], 100)
        random_number = random.random()
        if (random_number < prob_a):
            final_2 = winner_3
        else:
            final_2 = winner_4
        
        #Final 1 vs Final 2
        prob_a = probability_a(rating_dict[final_1], rating_dict[final_2], 100)
        random_number = random.random()
        if (random_number < prob_a):
            final_winner = final_1
        else:
            final_winner = final_2
            
        #Increment win count
        player_wins[final_winner] += 1
    
    #Create result dictionary
    result = {}
    for i in range(8):
        result[i] = player_wins[i] / 100.0
    
    return result

def display_probs(probs_dict):
    
    """Parameters:
        probs_dict: a dictionary where the keys are the players and values are the probability that the player wins the tournament
        
        Returns:
        None. Creates projections_pie.pdf and probs.csv."""
    
    
    sorted_probs = sorted(probs_dict.values(), reverse = True)
    
    #Turn sorted_probs into a DataFrame, then write it to CSV file
    dfr = pandas.DataFrame(sorted_probs, index = range(8))
    dfr.to_csv('probs.csv')
    
    #Set up figure for pie chart
    fig = matplotlib.pyplot.figure(figsize=(8, 8))
    players = list(probs_dict.keys())
    probs = list(probs_dict.values())

    # Create a pie chart
    matplotlib.pyplot.pie(probs, labels=players, autopct='%1.1f%%', startangle=140, colors=matplotlib.pyplot.cm.Paired.colors)
    matplotlib.pyplot.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    matplotlib.pyplot.title('Tournament Win Probabilities')
    
    matplotlib.pyplot.savefig('projections_pie.pdf')

    # Show the plot on the console
    matplotlib.pyplot.show()

    
    