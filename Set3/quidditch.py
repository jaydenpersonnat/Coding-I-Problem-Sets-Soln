                                # Quiddtich 

# Goal: Create a program that calculates the score of a quidditch match.

"""
Background: 
    You want to calculate the final score for a team that has just participated 
    in an exciting quidditch match using a program called quidditch.py. If you 
    don’t know about quidditch… Recall that each “goal” in quidditch is worth 
    10 points, and that catching the snitch is worth 150 points.

Your Mission: 
    Building on the code in quidditch.py, implement a function that takes two 
    variables as input — an int indicating the number of times the team got the 
    Quaffle through the other team’s hoops, and an int indicating whether or not 
    they caught the snitch – and returns that team’s final score (what would the return type be?).

"""

# Code goes below 


def main():
    goalNum = int(input("Number of times your chasers got the quaffle through a hoop: "))
    snitchCaught = int(input("Did your team's seeker catch the snitch? Enter 1 if true, 0 otherwise: "))
    score = final_score(goalNum, snitchCaught)
    print("Your team's final score is: " + str(score))

def final_score(goals, snitchCaught): 
    if snitchCaught == 1:
        return goals * 10 + 150
    else: 
        return goals * 10 

if __name__ == "__main__":
    main()