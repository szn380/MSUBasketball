
import random

nameList1 = ["Thomas", "Jonathan", "Joe", "Sam", "Magic", "Kevin", "Ken", "Isiah", "Big Ben", "Elmer"]
nameList2 = ["Grant", "Paolo", "Kong", "Darrel", "Shack", "Baron", "Donald", "Harry", "Ron", "Shemp", "Gregor"]
nameList3 = ["Ryan", "Evan", "Joel", "Jacob", "Jeff", "Aaron", "Reggie", "Archie", "The Judge", "Lebron"]
nameList4 = ["Stanley", "Boban", "Brice", "Andre", "Luke", "Blake", "Henry", "Luis", "Walter", "Eric"]
nameList5 = ["Langston", "Willie", "Jon", "Avery", "Jarvis", "Dwight", "Theo", "Tobias", "Keenan", "Dan"]
nameList6 = ["Kyle", "Miles", "Connor", "Kenny", "Jack", "Jaren", "Josh", "Matt", "Gavin", "Xavier"]
nameList7 = ["Jamal", "Alonso", "Adrian", "Tyron", "Leroy", "Angus", "Edward", "Augustus", "Austin", "Avery"]
nameList8 = ["Red", "Gerard", "Caleb", "Cameron", "Clyde", "Duane", "Dudley", "Elijah", "Elwood", "Emery"]
nameList9 = ["Hacksaw", "Bonesaw", "Ace", "Psycho", "Scott", "Logan", "Guido", "Mario", "Luigi", "Dean"]
nameList = nameList1 + nameList2 + nameList3 + nameList4 + nameList5 + nameList6 + nameList7 + nameList8 + nameList9

opponentList = ["CMU", "Indiana", "Illinois", "Purdue", "Ohio State", "Wisconson", "Minnisota", "Northwestern", "Iowa", "UofM"]
NAME = 0                # type string - first name
POSITION = 1            # type string - name of position
OFFENSE = 2             # integer [1..10] -  offense scoring factor (not known to game player)
DEFENSE = 3             # integer [1..10] -  defense factor     (not known to game player)
YEAR = 4                # string [Freshman, Sophomore, Junior, Senior]
GAMESCORE = 5           # integer - points scored in the current game
SEASONTOTAL = 6         # integer - total points scored during the current season
CAREERTOTAL = 7         # float - average points scored per season for the entire career of the player
CAREERGAMES = 8         # integer - number of games a player has played over his career
OFFENSEEST = 9          # integer [1..10] - estimate of OFFENSE scoring factor
DEFENSEEST = 10         # integer [1..10] - estimate of DEFENSE factor
GAMEREBOUNDS = 11       # integer - number of rebounds collected in the current game
SEASONREBOUNDS = 12     # integer - total number of rebounds collected in the current season
CAREERREBOUNDS = 13     # float - average number of rebounds per season over the career of the player
GAMEASSISTS = 14        # integer - number of assists collected in the current game
SEASONASSISTS = 15      # integer - total number of assists collected in the current season
CAREERASSISTS = 16      # float - average number of assists per season over the career of the player
ASSISTS = 17            # integer [1..10] assist factor (not know to game player)
BLOCKS = 18            # integer [1..10] assist factor (not know to game player)
GAMEBLOCKS = 19        # integer - number of assists collected in the current game
SEASONBLOCKS = 20      # integer - total number of assists collected in the current season
CAREERBLOCKS = 21      # float - average number of assists per season over the career of the player
SEASONEXP = 22          # Integer - amount of experienced gained during the current season
PLAYERSTATUS = 23       # integer - 1: Starter  2: Bench Rotation (playing)  3: Benched (not playing)  4: Red Shirt (not playing)
STARTER = 0
ROTATION = 1
BENCHED = 2
REDSHIRT = 3

########################################################
#
#   Update scoring factor estimates
#
#   Given an pointer to a player list, update the OFFENSEEST
#   and DEFENSEEST values based on the real OFFENSE and DEFENSE
#   scoring factors and the use of a random number
#   and probability limits (boundaryLow and boundaryHigh)
#
#   The limit variable is used for the special csae of new recruits
#   for which you do not want too high or too low of estimates
#
#######################################################
def updateOffDeffEstimates(player, boundaryLow, boundaryHigh, limit):
    # update offense and defense estimates
    if not limit:
        randomNumber = random.random()
        player[OFFENSEEST] = player[OFFENSE]
        if randomNumber < boundaryLow:
            player[OFFENSEEST] += 1
        elif randomNumber > boundaryHigh:
            player[OFFENSEEST] -= 1
        randomNumber = random.random()
        player[DEFENSEEST] = player[DEFENSE]
        if randomNumber < boundaryLow:
            player[DEFENSEEST] += 1
        elif randomNumber > boundaryHigh:
            player[DEFENSEEST] -= 1
    else:
        randomNumber = random.random()
        player[OFFENSEEST] = player[OFFENSE]
        if (randomNumber < boundaryLow) and (player[OFFENSE] < 5):
            player[OFFENSEEST] += 1
        elif (randomNumber > boundaryHigh) and (player[OFFENSE] > 3):
            player[OFFENSEEST] -= 1
        randomNumber = random.random()
        player[DEFENSEEST] = player[DEFENSE]
        if (randomNumber < boundaryLow) and (player[DEFENSE] < 5):
            player[DEFENSEEST] += 1
        elif (randomNumber > boundaryHigh) and (player[DEFENSE] > 3):
            player[DEFENSEEST] -= 1
    return

########################################################
#
#   Initialize team lineups
#
#   Setup team and benchList players for the very beginning
#   of the game. The players are the actual players from the 1979
#   MSU team.
#
#######################################################
def initPlayerLists(team,benchList):

    # [0 - name, 1 - position, 2 - offense, 3 - defense, 4 - year, 5 - game score, 6 - season total,
    # 7 - career total, 8 - career games, 9 - offense estimate, 10 - defense estimate]
    # 11 - game rebounds, 12 - rebound season total, 13 - career rebound total
    team.append(["Ron", "Center", 5, 6, "Senior", 0, 0, 105, 0, 0, 0, 0, 0, 55, 0, 0, 0, 2, 2, 0, 0, 0, 0, STARTER])
    team.append(["Rob", "Forward", 3, 3, "Sophomore", 0, 0, 15, 0, 0, 0, 0, 0, 5, 0, 0, 0,2, 0, 0, 0, 0, 0, STARTER])
    team.append(["Jay", "Forward", 6, 6, "Junior", 0, 0, 157, 0, 0, 0, 0, 0, 65, 0, 0, 0, 2, 0, 0, 0, 0, 0, STARTER])
    team.append(["Mike", "Guard", 4, 3, "Junior", 0, 0, 63, 0, 0, 0, 0, 0, 30, 0, 0, 0, 3, 0, 0, 0, 0, 0, STARTER])
    team.append(["Terry", "Guard", 4, 4, "Senior", 0, 0, 55, 0, 0, 0, 0, 0, 19, 0, 0, 0, 5, 0, 0, 0, 0, 0, STARTER])
    benchList.append(["Steve", "Center", 2, 3, "Sophomore", 0, 0, 7, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 1, 0, 0, 0, 0, ROTATION])
    benchList.append(["Derek", "Forward", 3, 4, "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, ROTATION])
    benchList.append(["Kurt", "Forward", 2, 4, "Junior", 0, 0, 15, 0, 0, 0, 0, 0, 10, 0, 0, 0, 2, 0, 0, 0, 0, 0, ROTATION])
    benchList.append(["Herb", "Guard", 2, 3, "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, BENCHED])
    benchList.append(["Kevin", "Guard", 4, 4, "Sophomore", 0, 0, 25, 0, 0, 0, 0, 0, 20, 0, 0, 0, 4, 0, 0, 0, 0, 0, ROTATION])
    benchList.append(["Don", "Forward", 2, 3, "Sophomore", 0, 0, 7, 0, 0, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0, BENCHED])
    benchList.append(["Bill", "Guard", 2, 3, "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, BENCHED])
    benchList.append(["Mike", "Guard", 3, 3, "Senior", 0, 0, 11, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, ROTATION])
    benchList.append(["Richard", "Forward", 2, 3, "Junior", 0, 0, 8, 0, 0, 0, 0, 0, 4, 0, 0, 0, 2, 0, 0, 0, 0, 0, BENCHED])

    # determine offense and defense score factor estimates
    # only the estimates will be viewed during recruiting
    for player in team:
        updateOffDeffEstimates(player, 0.1, 0.9, False)
    for player in benchList:
        updateOffDeffEstimates(player, 0.1, 0.9, False)

    return;


########################################################
#
#   Provide Opportunity to update offense score factor update
#
#   Input from game player player number of player to update.
#   Input the new offensive factor to use.
#
#######################################################
def updateOffenseEstimate(team, benchList):
    # give option to update offensive scoring factor estimates
    Done = False
    while not Done:
        print("*  Enter player number to be updated or enter 0 to exit")
        response = input()
        if response.isdigit():
            response = int(response)
            if response == 0:
                Done = True
            elif response < 6:
                response1 = int(input("*  Enter new offensive estimate for {} ".format(team[response-1][NAME])))
                team[response-1][OFFENSEEST] = response1
            elif response > 5:
                response1 = int(input("*  Enter new offensive estimate for {} ".format(benchList[response-6][NAME])))
                benchList[response-6][OFFENSEEST] = response1
    return;

def updateDefenseEstimate(team, benchList):
    # give option to update offensive scoring factor estimates
    Done = False
    while not Done:
        print("*  Enter player number to be updated or enter 0 to exit")
        response = input()
        if response.isdigit():
            response = int(response)
            if response == 0:
                Done = True
            elif response < 6:
                response1 = int(input("*  Enter new defensive estimate for {} ".format(team[response-1][NAME])))
                team[response-1][DEFENSEEST] = response1
            elif response > 5:
                response1 = int(input("*  Enter new defensive estimate for {} ".format(benchList[response-6][NAME])))
                benchList[response-6][DEFENSEEST] = response1
    return;

########################################################
#
#   Provide Opportunity to update starting line up
#
#   Input from game player player numbers to swap.
#   Assumption is that first number is from the starting lineup
#   and the second number is from the bench line up.
#
#######################################################
def updateStartingLineup(team, benchList):
    # give option to swap player from starting to bench lineup
    Done = False
    while not Done:
        print("*  Swap a starting player and a bench player?   0 for No  or 1 for Yes ")
        response = input()
        if response.isdigit():
            response = int(response)
            if response == 0:
                Done = True
            else:
                response1,response2 = input("* Input Number of starting player and number of bench player to swap ").split()
                if (response1.isdigit() and response2.isdigit()):
                    response1,response2 = int(response1), int(response2)
                    tempPlayer = list(team[response1-1])
                    team[response1-1] = benchList[response2-6]
                    team[response1-1][PLAYERSTATUS] = STARTER
                    benchList[response2-6] = tempPlayer
                    benchList[response2-6][PLAYERSTATUS] = ROTATION
    return;

########################################################
#
#   Covert Team Stats from Float to Text Assessment
#
#   Assign grades (D, C, B, A-, A) for team statistics
#
#######################################################
def convertTeamStatsToText(assistFactor, teamOffense, teamDefense, topThreeOff, topThreeDef, blockFactor):

    passingSummary = "D"
    if assistFactor <= 3:
        passingSummary = "C"
    elif assistFactor <= 5:
        passingSummary = "B"
    elif assistFactor <= 7:
        passingSummary = "A-"
    else:
        passingSummary = "A"

    blockSummary = "D"
    if blockFactor <= 3:
        blockSummary = "C"
    elif blockFactor <= 5:
        blockSummary = "B"
    elif blockFactor <= 7:
        blockSummary = "A-"
    else:
        blockSummary = "A"

    startingOffSummary = "D"
    if teamOffense <= 4:
        startingOffSummary = "C"
    elif teamOffense <= 4.5:
        startingOffSummary = "B"
    elif teamOffense <= 5:
        startingOffSummary = "A-"
    else:
        startingOffSummary = "A"

    startingDefSummary = "D"
    if teamDefense <= 4:
        startingDefSummary = "C"
    elif teamDefense <= 4.5:
        startingDefSummary = "B"
    elif teamDefense <= 5:
        startingDefSummary = "A-"
    else:
        startingDefSummary = "A"

    benchOffSummary = "D"
    if topThreeOff <= 4:
        benchOffSummary = "C"
    elif topThreeOff <= 4.5:
        benchOffSummary = "B"
    elif topThreeOff <= 5:
        benchOffSummary = "A-"
    else:
        benchOffSummary = "A"

    benchDefSummary = "D"
    if topThreeDef <= 4:
        benchDefSummary = "C"
    elif topThreeDef <= 4.5:
        benchDefSummary = "B"
    elif topThreeDef <= 5:
        benchDefSummary = "A-"
    else:
        benchDefSummary = "A"
    return(passingSummary, startingOffSummary, startingDefSummary, benchOffSummary, benchDefSummary, blockSummary)


########################################################
#
#   Update team overall statistics for evaluating game results
#
#   Four factors are used to determine the outcome of games.
#   The first two are the average offense and defense scoring factors
#   for the starting players.
#   The second two factors are based on the average of the top
#   three bench players for offense and defense respectively
#
#######################################################
def updateTeamOffDefStats(team, benchList, resultList):
    #   resultList[0] = teamOffense
    #   resultList[1] = teamDefense
    #   resultList[2] = topThreeOff
    #   resultList[3] = topThreeDef
    #   resultList[4] = teamAssist
    #   resultList[5] = teamBlocks

    teamOffense = 0     # average offensive factor of the starters
    teamDefense = 0     # average defensive factor of the starters
    teamAssistMax = 0      # max assist factor of the starters
    teamAssist = 0      # average assist factor of the starters
    teamBlocks = 0
    rotationCount = 0
    for player in team:
        if (player[PLAYERSTATUS] == STARTER) or True:       #JGD
            teamOffense += player[OFFENSE]/5
            teamDefense += player[DEFENSE]/5
            teamAssistMax = max(teamAssistMax, player[ASSISTS])
            teamAssist += player[ASSISTS]/5
    #     elif (player[PLAYERSTATUS] == ROTATION) or False:   #JGD
    #         benchOffense += player[OFFENSE]
    #         benchDefense += player[DEFENSE]
    #         rotationCount += 1
    # benchOffense = benchOffense / rotationCount
    # benchDefense = benchDefense / rotationCount

    # determine how many players are at each scoring factor level
    # for example, 3 players at level 4, ...
    # these two list keep count of the number at each level
    benchOffense = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    benchDefense = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for player in benchList:
        benchOffense[player[OFFENSE]] += 1
        benchDefense[player[DEFENSE]] += 1

    topThreeOffIncr = 0
    topThreeDefIncr = 0
    topThreeOff = 0     # average offensive factor of the top 3 bench players
    topThreeDef = 0     # average defensive factor of the top 3 bench players
    for index in range(9,-1,-1):
        # print("Index {}".format(index))
        if benchOffense[index] != 0:
            while (topThreeOffIncr < 3) and (benchOffense[index] > 0):
                # print("OFF While Loop topThreeOffIncr {}  benchOffense index {}".format(topThreeOffIncr, benchOffense[index]))
                topThreeOffIncr += 1
                benchOffense[index] -= 1
                topThreeOff += index
        if benchDefense[index] != 0:
            while (topThreeDefIncr < 3) and (benchDefense[index] > 0):
                # print("DEF While Loop topThreeOffIncr {}  benchOffense index {}".format(topThreeOffIncr, benchOffense[index]))
                topThreeDefIncr += 1
                benchDefense[index] -= 1
                topThreeDef += index
    topThreeOff /= 3
    topThreeDef /=3

    assistFactor = (2*teamAssistMax + teamAssist)/3

    if assistFactor > 5:
        resultList[4] = 10
    elif assistFactor > 4.75:
        resultList[4] = 7
    elif assistFactor > 4.5:
        resultList[4] = 5
    elif assistFactor > 4:
        resultList[4] = 2
#    print("DEBUG assistFactor {}  result {}".format(assistFactor,resultList[4]))

    teamBlocks = 0
    for player in team:
        if (player[PLAYERSTATUS] == STARTER) or True:       #JGD
            teamBlocks += player[BLOCKS]

    resultList[0] = teamOffense
    resultList[1] = teamDefense
    #      resultList[2] = benchOffense         JGD
    #       resultList[3] = benchDefense       JGD
    resultList[2] = topThreeOff
    resultList[3] = topThreeDef
    resultList[5] = teamBlocks

    return;

##################################################
# Determine Opponent offense / defense factor and their record
#
# several random numbers are used to determine the team off/def scoring factors (values 2.7..5.8)
# The teams win / loss record is based on the total of the score factors and several random numbers
# compared to a default number
#
##################################################
class opponentInfo:
    def __init__(self, gameNumber):
        self.gameNumber = gameNumber
        self.opponentOffense = 0
        self.opponentDefense = 0
        self.wins = 0

        section = random.randint(1, 10)
        if section == 1:
            self.opponentOffense = 2.7 + random.random()
        elif section < 4:
            self.opponentOffense = 3.4 + random.random()
        elif section < 8:
            self.opponentOffense = 3.65 + random.random()
        elif section < 10:
            self.opponentOffense = 4.4 + random.random()
        else:
            self.opponentOffense = 4.8 + random.random()

        section = random.randint(1, 10)
        if section == 1:
            self.opponentDefense = 2.7 + random.random()
        elif section < 4:
            self.opponentDefense = 3.4 + random.random()
        elif section < 8:
            self.opponentDefense = 3.65 + random.random()
        elif section < 10:
            self.opponentDefense = 4.4 + random.random()
        else:
            self.opponentDefense = 4.8 + random.random()

        for index in range(1,self.gameNumber+1):
            if ((self.opponentOffense + self.opponentDefense)/8 + random.random() > 1 + random.random()):
                self.wins += 1

    def Offense(self):
        return(self.opponentOffense)

    def Defense(self):
        return(self.opponentDefense)

    def Wins(self):
        return(self.wins)


def displayMenu(team, benchList, gameNumber):
    print("*******************************************************")
    print("*")
    print("* Select Option")
    print("*\t\t0 or Enter:\t\tContinue")
    print("*\t\t1:\t\t\t\tUpdate starting lineup")
    print("*\t\t2:\t\t\t\tList player statistics")
    print("*\t\t3:\t\t\t\tUpdate player offense factor")
    print("*\t\t4:\t\t\t\tUpdate player defense factor")
    print("*")
    print("*******************************************************")

    if gameNumber <= 0:
        gameNumber = 1
    Done = False
    while not Done:
        response = input()
        if response.isdigit():
            response = int(response)
            if response == 0:
                Done = True
            elif response ==1:
                response1,response2 = input("* Input Number of starting player and number of bench player to swap ").split()
                if (response1.isdigit() and response2.isdigit()):
                    response1,response2 = int(response1), int(response2)
                    tempPlayer = list(team[response1-1])
                    team[response1-1] = benchList[response2-6]
                    benchList[response2-6] = tempPlayer
            elif response == 2:
                index1 = 1
                for player in team:
                    print("*\t{}\t{:10}\t\tAvg: {:4.3}\t\tReb Avg: {:4.3}\t\tAst: Avg: {:4.3}\t\tBlk Avg: {:4.3}\t{}\t\t{:10}\tOff: {}\t\t Def: {}"
                          "".format(index1, player[NAME], player[SEASONTOTAL]/gameNumber, player[SEASONREBOUNDS]/gameNumber,
                                    player[SEASONASSISTS]/gameNumber, player[SEASONBLOCKS]/gameNumber, player[POSITION], player[YEAR], player[OFFENSEEST], player[DEFENSEEST]))
                    index1 += 1
                for player in benchList:
                    print("*\t{}\t{:10}\t\tAvg: {:4.3}\t\tReb Avg: {:4.3}\t\tAst: Avg: {:4.3}\t\tBlk Avg: {:4.3}\t{}\t\t{:10}\tOff: {}\t\t Def: {}"
                          "".format(index1, player[NAME], player[SEASONTOTAL]/gameNumber, player[SEASONREBOUNDS]/gameNumber,
                                    player[SEASONASSISTS]/gameNumber, player[SEASONBLOCKS]/gameNumber, player[POSITION], player[YEAR], player[OFFENSEEST], player[DEFENSEEST]))
                    index1 += 1
            elif response == 3:
                updateOffenseEstimate(team, benchList)
            elif response == 4:
                updateDefenseEstimate(team, benchList)
        else:
            Done = True
    return;


########################################################
#
#   Main Game Loop
#
#   After setting up the original team players, then
#   loop through for each season (indefinite number of seasons),
#   determining results for each individual game of that season.
#
#######################################################
team = []   # List of the starting players for the MSU team
benchList = []  # List of the bench players for the MSU team
initPlayerLists(team, benchList)    # add the original players to the team

print("*******************************************************")
print("*")
print("*\tMSU Spartan Bastketball")
print("*")
print("*\t\tNow that Magic has left for the NBA")
print("*\t\tCan you go undefeated within 5 seasons of taking over the floundering program?")
print("*")
print("*******************************************************")

print("*******************************************************")
print("*")
print("*\tStarting Lineup")
print("*")
print("*******************************************************")
for player in team:
    print("*\tName: {:10}  \tPosition: {}  \tOffense: {}  \tDefense: {} \tYear: {}\tAve: {:4.3}\tCareer: {:4.3}\tReb Ave: {:4.3}\tAst Avg: {:4.3}\tBlk Avg: {:4.3}"
          "".format(player[NAME], player[POSITION], player[OFFENSEEST], player[DEFENSEEST], player[YEAR], player[SEASONTOTAL]/10,
                    player[CAREERTOTAL]/10, player[CAREERREBOUNDS]/10, player[CAREERASSISTS]/10, player[CAREERBLOCKS]/10))

print("*******************************************************")
print("*")
print("*\tBench Players")
print("*")
print("*******************************************************")
for player in benchList:
    print("*\tName: {:10}  \tPosition: {}  \tOffense: {}  \tDefense: {} \tYear: {}\tAve: {:4.3}\tCareer: {:4.3}\tReb Ave: {:4.3}\tAst Avg: {:4.3}\tBlk Avg: {:4.3}"
          "".format(player[NAME], player[POSITION], player[OFFENSEEST], player[DEFENSEEST], player[YEAR], player[SEASONTOTAL]/10,
                    player[CAREERTOTAL]/10, player[CAREERREBOUNDS]/10, player[CAREERASSISTS]/10, player[CAREERBLOCKS]/10))

# since lineup may have changed, need to update team stats
resultList = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
updateTeamOffDefStats(team, benchList, resultList)
teamOffense, teamDefense, topThreeOff, topThreeDef  = resultList[0], resultList[1], resultList[2], resultList[3]
assistFactor = resultList[4]
blockFactor = resultList[5]


passingSummary, startingOffSummary, startingDefSummary, benchOffSummary, benchDefSummary, blockSummary = convertTeamStatsToText(assistFactor, teamOffense, teamDefense, topThreeOff, topThreeDef, blockFactor)

print("*******************************************************")
print("*")
print("*\tTeam Scorecard")
print("*")
print("*\tStarting Offense: \t{} \tStarting Defense: \t{}".format(startingOffSummary, startingDefSummary))
print("*\tBench Offense: \t\t{}  \tBench Defense: \t\t{}".format(benchOffSummary, benchDefSummary))
print("*\tPassing Report\t\t{} \tBlocking Report: \t{}".format(passingSummary, blockSummary))
print("*")
print("*******************************************************")

for year in range(1, 21):

    print("*******************************************************")
    print("*")
    print("*\tSeason #{}".format(year))
    print("*")
    print("*******************************************************")
    teamWins = 0
    teamLoses = 0
    for gameNumber in range(1, 11):
        opponent = opponentInfo(gameNumber)  # create opponent
        print("*")
        print("*\tNext Game against {}".format(opponentList[gameNumber-1]))
        print("*")
        print("*")
        print("*\t\tMSU {}-{} vs. {} {}-{}".format(teamWins, gameNumber-1-teamWins, opponentList[gameNumber-1],
                                                   opponent.Wins(), gameNumber-opponent.Wins()))
        print("*")


        ##################################################
        # Swami pick
        #
        # the Swami pick is just based on playing a (unofficial) game between the teams and reporting the difference in the score
        # the Swami picks who ever wins the unofficial game to win the real game
        # teamOffense, topThreeOff, and homeOffense are all score factor scores (value 3..9) that represent
        # the average for the team starters or top three bench players.
        ##################################################
        homeOffense = (teamOffense*2 + topThreeOff)/3 + random.random()*3 - 1.5
        homeDefense = (teamDefense*2 + topThreeDef)/3 + random.random()*3 - 1.5
        teamScore = int((homeOffense - opponent.Defense())*10 + 60)  + int(assistFactor)
        opponentScore = int((opponent.Offense() - homeDefense)*10 + 65)
        if teamScore - opponentScore >= 0:
            print("*  Swami Predicts: MSU by {}".format(teamScore - opponentScore))
        else:
            print("*  Swami Predicts: {} by {}".format(opponentList[gameNumber-1], opponentScore - teamScore))

        # give option to change starting lineup
        # updateStartingLineup(team, benchList)
        displayMenu(team, benchList, gameNumber-1)
        # since lineup may have changed, need to update team stats
        resultList = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        updateTeamOffDefStats(team, benchList, resultList)
        teamOffense, teamDefense, topThreeOff, topThreeDef,  = resultList[0], resultList[1], resultList[2], resultList[3]
        assistFactor = resultList[4]
        blockFactor = resultList[5]

        passingSummary, startingOffSummary, startingDefSummary, benchOffSummary, benchDefSummary, blockSummary = convertTeamStatsToText(assistFactor, teamOffense, teamDefense, topThreeOff, topThreeDef, blockFactor)

        print("*******************************************************")
        print("*")
        print("*\tTeam Scorecard")
        print("*")
        print("*\tStarting Offense: \t{} \tStarting Defense: \t{}".format(startingOffSummary, startingDefSummary))
        print("*\tBench Offense: \t\t{}  \tBench Defense: \t\t{}".format(benchOffSummary, benchDefSummary))
        print("*\tPassing Report\t\t{} \tBlocking Report: \t{}".format(passingSummary, blockSummary))
        print("*")
        print("*******************************************************")

        ##################################################
        # Real Game
        #
        # Determine home team offense and defense factors for this game
        # teamOffense, topThreeOff, and homeOffense are all score factor scores (value 3..9) that represent
        # the average for the team starters or top three bench players.
        ##################################################
        homeOffense = (teamOffense*2 + topThreeOff)/3 + random.random()*2 - 1
        homeDefense = (teamDefense*2 + topThreeDef)/3 + random.random()*2 - 1

        # determine points scored for this game
        teamScore = int((homeOffense - opponent.Defense())*10 + 60) + int(assistFactor)
        opponentScore = int((opponent.Offense() - homeDefense)*10 + 65) - int(blockFactor)*2
        teamRebounds = int(teamScore/2)
        # adjust score if it is a tied score
        if teamScore == opponentScore:
            teamScore += 1
        print("*******************************************************")
        print("*")
        # print results and accumulate win / loss
        print("*\tMSU: {}  {}: {}".format(teamScore, opponentList[gameNumber-1], opponentScore))
        if teamScore > opponentScore:
            teamWins += 1
        else:
            teamLoses += 1

        ##################################################
        # Determine Players Chance of Being Allocated Field Goals (Baskets)
        #
        # startingScore and benchScore are the scores of the starting and bench players respectively
        # different factors are used depending on the players offense rating (high factors for starter
        # and those with higher offense ratings
        # scoring factors are determined for each player, then the total score of the game is allocated
        # to each player based on the the players scoring factor divided by the sum of the teams
        ##################################################
        startingScore = []  # list containing the scoring factor for this game for the starting players
        benchScore = []     # list containing the scoring factor for this game for the bench players
        for player in team:
            if player[OFFENSE] > 7:
                startingScore.append(9*(player[OFFENSE] + 3*random.random()))
            elif player[OFFENSE] > 6:
                startingScore.append(7*(player[OFFENSE] + 3*random.random()))
            elif player[OFFENSE] > 5:
                startingScore.append(5*(player[OFFENSE] + 3*random.random()))
            elif player[OFFENSE] > 4:
                startingScore.append(3*(player[OFFENSE] + 3*random.random()))
            else:
                startingScore.append(2*(player[OFFENSE] + 3*random.random()))
        for player in benchList:
            if player[OFFENSE] > 4:
                benchScore.append((2*player[OFFENSE] + 4*random.random()))
            elif player[OFFENSE] > 3:
                benchScore.append(0.5*(player[OFFENSE] + 2*random.random()))
            elif (random.random() > 0.5):
                benchScore.append(0.5*(player[OFFENSE] + 2*random.random()))
            else:
                benchScore.append(0)

        # determine total scoreing factor for the entire team for this game
        totalScoreFactor = 0
        for scoreFactor in startingScore:
            totalScoreFactor += scoreFactor
        for scoreFactor in benchScore:
            totalScoreFactor += scoreFactor

        ###################################################
        # Determine Players Chance of Being Allocated Rebounds
        ###################################################
        startingRebounds = []  # list containing the rebound factor for this game for the starting players
        benchRebounds = []     # list containing the rebound factor for this game for the bench players
        for player in team:
            if player[DEFENSE] > 7:
                startingRebounds.append(9*(player[DEFENSE] + 3*random.random()))
            elif player[DEFENSE] > 6:
                startingRebounds.append(7*(player[DEFENSE] + 3*random.random()))
            elif player[OFFENSE] > 5:
                startingRebounds.append(5*(player[DEFENSE] + 3*random.random()))
            elif player[OFFENSE] > 4:
                startingRebounds.append(3*(player[DEFENSE] + 3*random.random()))
            else:
                startingRebounds.append(2*(player[DEFENSE] + 3*random.random()))
        for player in benchList:
            if player[DEFENSE] > 4:
                benchRebounds.append((2*player[DEFENSE] + 4*random.random()))
            elif player[DEFENSE] > 3:
                benchRebounds.append(0.5*(player[DEFENSE] + 2*random.random()))
            elif (random.random() > 0.5):
                benchRebounds.append(0.5*(player[DEFENSE] + 2*random.random()))
            else:
                benchRebounds.append(0)

        # determine total rebound factor for the entire team for this game
        totalReboundsFactor = 0
        for reboundFactor in startingRebounds:
            totalReboundsFactor += reboundFactor
        for reboundFactor in benchRebounds:
            totalReboundsFactor += reboundFactor

        ###################################################
        #  Determine Players Chance of Being Allocated Assists
        ###################################################
        # assign assists
        assistsTotal = 10 + assistFactor
        startingAssists = []  # list containing the rebound factor for this game for the starting players
        benchAssists = []     # list containing the rebound factor for this game for the bench players
        for player in team:
            if player[ASSISTS] > 7:
                startingAssists.append(9*(player[ASSISTS] + 3*random.random()))
            elif player[ASSISTS] > 6:
                startingAssists.append(7*(player[ASSISTS] + 3*random.random()))
            elif player[ASSISTS] > 5:
                startingAssists.append(5*(player[ASSISTS] + 3*random.random()))
            elif player[ASSISTS] > 4:
                startingAssists.append(3*(player[ASSISTS] + 3*random.random()))
            else:
                startingAssists.append(2*(player[ASSISTS] + 3*random.random()))
        for player in benchList:
            if player[ASSISTS] > 4:
                benchAssists.append((2*player[ASSISTS] + 4*random.random()))
            elif player[ASSISTS] > 3:
                benchAssists.append(0.5*(player[ASSISTS] + 2*random.random()))
            elif (random.random() > 0.5):
                benchAssists.append(0.5*(player[ASSISTS] + 2*random.random()))
            else:
                benchAssists.append(0)

        # determine total assist factor for the entire team for this game
        totalAssistsFactor = 0
        for assistFactor1 in startingAssists:
            totalAssistsFactor += assistFactor1
        for assistFactor1 in benchAssists:
            totalAssistsFactor += assistFactor1

        ###################################################
        #  Determine Players Chance of Being Allocated Blocks
        ###################################################
        # Note: the block factor is only based on the starting players
        # so only loop through the starting team players
        blocksTotal = 3 + blockFactor
        startingBlocks = []  # list containing the rebound factor for this game for the starting players
        for player in team:
            if player[BLOCKS] > 7:
                startingBlocks.append(9*(player[BLOCKS] + 3*random.random()))
            elif player[BLOCKS] > 6:
                startingBlocks.append(7*(player[BLOCKS] + 3*random.random()))
            elif player[BLOCKS] > 5:
                startingBlocks.append(5*(player[BLOCKS] + 3*random.random()))
            elif player[BLOCKS] > 4:
                startingBlocks.append(3*(player[BLOCKS] + 3*random.random()))
            else:
                startingBlocks.append(2*(player[BLOCKS] + 3*random.random()))

        # determine total block factor for the entire team for this game
        totalBlockFactor = 0
        for blockFactor1 in startingBlocks:
            totalBlockFactor += blockFactor1

        ###################################################
        #  Determine Player Game Statistics and Update Season Statistics
        ###################################################
        #   player score is based on the ratio of their individual score factor to the sum of the teams
        #   The approach is that the total game score is already determined, and now must be allocated
        #   across the individual players
        index = 0
        for player in team:
            player[GAMESCORE] = int(startingScore[index]/totalScoreFactor*teamScore)
            player[SEASONTOTAL] += player[GAMESCORE]  # accumlate scores across games
            player[GAMEREBOUNDS] = int(startingRebounds[index]/totalReboundsFactor*teamRebounds)
            player[SEASONREBOUNDS] += player[GAMEREBOUNDS]  # accumlate scores across games
            player[GAMEASSISTS] = int(startingAssists[index]/totalAssistsFactor*assistsTotal)
            player[SEASONASSISTS] += player[GAMEASSISTS]  # accumlate scores across games
            player[GAMEBLOCKS] = int(startingBlocks[index]/totalBlockFactor*blocksTotal)
            player[SEASONBLOCKS] += player[GAMEBLOCKS]  # accumlate scores across games
            index +=1
        index = 0
        for player in benchList:
            if int(benchScore[index]/totalScoreFactor*teamScore) == 1:
                if random.random() > 0.3:
                    benchScore[index] *= 2
            player[GAMESCORE] = int(benchScore[index]/totalScoreFactor*teamScore)
            player[SEASONTOTAL] += player[GAMESCORE]  # accumlate scores across games
            player[GAMEREBOUNDS] = int(benchRebounds[index]/totalReboundsFactor*teamRebounds)
            player[SEASONREBOUNDS] += player[GAMEREBOUNDS]  # accumlate scores across games
            player[GAMEASSISTS] = int(benchAssists[index]/totalAssistsFactor*assistsTotal)
            player[SEASONASSISTS] += player[GAMEASSISTS]  # accumlate scores across games
            index +=1


        ###################################################
        #  Determine Player Experience
        ###################################################
        #   Current methods for determine experience is that
        #   starting players get 3 experience points for each game, while
        #   bench players either get 1 or 2, depending on if they
        #   contributed to game results
        for player in team:
            player[SEASONEXP] += 3
        for player in benchList:
            player[SEASONEXP] +=1
            if ((player[GAMESCORE] > 0) or (player[GAMEREBOUNDS] > 0) or (player[GAMEASSISTS] > 0) or (player[GAMEBLOCKS] > 0)):
                player[SEASONEXP] +=1

        ###################################################
        #  Display Team Roster & Statistics
        ###################################################
        print("*\tPlayer Scores")
        index1 = 1
        for player in team:
            print("*\t{}\t{:10}\t{}\t\tAvg: {:4.1f}\t\tReb: {}\t\tAvg: {:4.1f}\t\tAst: {}\t\tAvg: {:4.1f}\t\tBlk: {}\t\tAvg: {:4.1f}\t{}\t\t{:10}\tOff: {}\tDef: {}\tExp: {}"
                  "".format(index1, player[NAME], player[GAMESCORE], round(player[SEASONTOTAL]/gameNumber, 2), player[GAMEREBOUNDS], round(player[SEASONREBOUNDS]/gameNumber, 2),
                            player[GAMEASSISTS], round(player[SEASONASSISTS]/gameNumber, 2),  player[GAMEBLOCKS], round(player[SEASONBLOCKS]/gameNumber, 2),
                            player[POSITION], player[YEAR], player[OFFENSEEST], player[DEFENSEEST], player[SEASONEXP]))
            index1 += 1
        for player in benchList:
            print("*\t{}\t{:10}\t{}\t\tAvg: {:4.1f}\t\tReb: {}\t\tAvg: {:4.1f}\t\tAst: {}\t\tAvg: {:4.1f}\t\tBlk: {}\t\tAvg: {:4.1f}\t{}\t\t{:10}\tOff: {}\tDef: {}\tExp: {}"
                  "".format(index1, player[NAME], player[GAMESCORE], round(player[SEASONTOTAL]/gameNumber, 2), player[GAMEREBOUNDS], round(player[SEASONREBOUNDS]/gameNumber, 2),
                            player[GAMEASSISTS], round(player[SEASONASSISTS]/gameNumber, 2),  player[GAMEBLOCKS], round(player[SEASONBLOCKS]/gameNumber, 2),
                            player[POSITION], player[YEAR], player[OFFENSEEST], player[DEFENSEEST], player[SEASONEXP]))
            index1 += 1
        print("*")

        displayMenu(team, benchList, gameNumber)
        # since lineup may have changed, need to update team stats
        resultList = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        updateTeamOffDefStats(team, benchList, resultList)
        teamOffense, teamDefense, topThreeOff, topThreeDef,  = resultList[0], resultList[1], resultList[2], resultList[3]
        assistFactor = resultList[4]
        blockFactor = resultList[5]

        passingSummary, startingOffSummary, startingDefSummary, benchOffSummary, benchDefSummary, blockSummary = convertTeamStatsToText(assistFactor, teamOffense, teamDefense, topThreeOff, topThreeDef, blockFactor)

        print("*******************************************************")
        print("*")
        print("*\tTeam Scorecard")
        print("*")
        print("*\tStarting Offense: \t{} \tStarting Defense: \t{}".format(startingOffSummary, startingDefSummary))
        print("*\tBench Offense: \t\t{}  \tBench Defense: \t\t{}".format(benchOffSummary, benchDefSummary))
        print("*\tPassing Report\t\t{} \tBlocking Report: \t{}".format(passingSummary, blockSummary))
        print("*")
        print("*******************************************************")


    print("*******************************************************")
    print("*")
    print("Final Record: {}-{}".format(teamWins, teamLoses))
    print("*")
    print("*******************************************************")
    input("\nType Enter to Continue: ")

    print("*******************************************************")
    print("*\tOld Team")
    for player in team:
        # update career statistics
        player[CAREERTOTAL] = (player[SEASONTOTAL] + player[CAREERTOTAL]*player[CAREERGAMES])/(1+player[CAREERGAMES])
        player[CAREERGAMES] += 1
        # print("*\tName: {:10}  \tPosition: {}  \tOffense: {}  \tDefense: {} \tYear: {}\tAve: {:4.3}\tCareer: {:4.3}"
        #       "".format(player[NAME], player[POSITION], player[OFFENSEEST], player[DEFENSEEST], player[YEAR], player[SEASONTOTAL]/10, player[CAREERTOTAL]/10))

        print("*\t{:10}\t\tAvg: {:4.1f}\t\tCareer: {:4.1f}\t\tReb: {:4.1f}\t\tCareer: {:4.1f}\t\tAst: {:4.1f}\t\tAvg: {:4.1f}\t\tBlk: {:4.1f}\t\tAvg: {:4.1f}\t{:10}\t{}"
              "".format(player[NAME], player[SEASONTOTAL]/10, player[CAREERTOTAL]/10, player[SEASONREBOUNDS]/10, player[CAREERREBOUNDS]/10,
                        player[SEASONASSISTS]/10,  player[CAREERASSISTS]/10, player[SEASONBLOCKS]/10, player[CAREERBLOCKS]/10,
                        player[POSITION], player[YEAR]))

    for player in benchList:
        # update career statistics
        player[CAREERTOTAL] = (player[SEASONTOTAL] + player[CAREERTOTAL]*player[CAREERGAMES])/(1+player[CAREERGAMES])
        player[CAREERGAMES] += 1
        # print("*\tName: {:10}  \tPosition: {}  \tOffense: {}  \tDefense: {} \tYear: {}\tAve: {:4.3}\tCareer: {:4.3}"
        #       "".format(player[NAME], player[POSITION], player[OFFENSEEST], player[DEFENSEEST], player[YEAR], player[SEASONTOTAL]/10, player[CAREERTOTAL]/10))
        print("*\t{:10}\t\tAvg: {:4.1f}\t\tCareer: {:4.1f}\t\tReb: {:4.1f}\t\tCareer: {:4.1f}\t\tAst: {:4.1f}\t\tAvg: {:4.1f}\t\tBlk: {:4.1f}\t\tAvg: {:4.1f}\t{:10}\t{}"
              "".format(player[NAME], player[SEASONTOTAL]/10, player[CAREERTOTAL]/10, player[SEASONREBOUNDS]/10, player[CAREERREBOUNDS]/10,
                        player[SEASONASSISTS]/10,  player[CAREERASSISTS]/10, player[SEASONBLOCKS]/10, player[CAREERBLOCKS]/10,
                        player[POSITION], player[YEAR]))

    # advance starting players
    print("*******************************************************")
    print("*\tNew Team")
    teamOffense = 0
    teamDefense = 0
    removeList = []
    for player in team:
        if player[YEAR] == "Senior":
            removeList.append(list(player))
            print("*\t{} has graduated".format(player[NAME]))
        else:
            player[OFFENSE] += random.randint(0, 1)
            player[DEFENSE] += random.randint(0, 1)
            player[ASSISTS] += random.randint(0, 1)

            if (player[POSITION] != "GUARD"):
                player[BLOCKS] += random.randint(0, 1)

            if player[YEAR] == "Freshman":
                player[YEAR] = "Sophomore"
            elif player[YEAR] == "Sophomore":
                player[YEAR] = "Junior"
            else:
                player[YEAR] = "Senior"

            # update offense and defense estimates
            updateOffDeffEstimates(player, 0.1, 0.9, False)

            # update career statistics
            player[CAREERTOTAL] = (player[SEASONTOTAL] + player[CAREERTOTAL]*player[CAREERGAMES])/(1+player[CAREERGAMES])
            player[CAREERREBOUNDS] = (player[SEASONREBOUNDS] + player[CAREERREBOUNDS]*player[CAREERGAMES])/(1+player[CAREERGAMES])
            player[CAREERASSISTS] = (player[SEASONASSISTS] + player[CAREERASSISTS]*player[CAREERGAMES])/(1+player[CAREERGAMES])
            player[CAREERBLOCKS] = (player[SEASONBLOCKS] + player[CAREERBLOCKS]*player[CAREERGAMES])/(1+player[CAREERGAMES])
            player[CAREERGAMES] += 1

            print("*\tName: {:10}  \tPosition: {}  \tOffense: {}  \tDefense: {} \tYear: {}\tAve: {:4.3}\tCareer: {:4.3}\tReb Ave: {:4.3}\tAst Avg: {:4.3}"
                  "".format(player[NAME], player[POSITION], player[OFFENSEEST], player[DEFENSEEST], player[YEAR], player[SEASONTOTAL]/10,
                            player[CAREERTOTAL]/10, player[CAREERREBOUNDS]/10, player[CAREERASSISTS]/10))

            player[SEASONTOTAL] = 0  # reset season average
            player[SEASONREBOUNDS] = 0  # reset season average
            player[SEASONASSISTS] = 0  # reset season average
            player[SEASONBLOCKS] = 0  # reset season average
            player[SEASONEXP] = 0   # reset season experience

    for player in removeList:
        team.remove(player)

    # advance bench list
    removeList = []
    for player in benchList:
        if player[YEAR] == "Senior":
            removeList.append(list(player))
            print("*\t{} has graduated".format(player[NAME]))
        else:
            player[OFFENSE] += random.randint(0, 1)
            player[DEFENSE] += random.randint(0, 1)
            player[ASSISTS] += random.randint(0, 1)
            if (player[POSITION] != "GUARD"):
                player[BLOCKS] += random.randint(0, 1)

            if player[YEAR] == "Freshman":
                player[YEAR] = "Sophomore"
            elif player[YEAR] == "Sophomore":
                player[YEAR] = "Junior"
            else:
                player[YEAR] = "Senior"

            # update offense and defense estimates
            updateOffDeffEstimates(player, 0.1, 0.9, False)

            # update career statistics
            player[CAREERTOTAL] = (player[SEASONTOTAL] + player[CAREERTOTAL]*player[CAREERGAMES])/(1+player[CAREERGAMES])
            player[CAREERREBOUNDS] = (player[SEASONREBOUNDS] + player[CAREERREBOUNDS]*player[CAREERGAMES])/(1+player[CAREERGAMES])
            player[CAREERASSISTS] = (player[SEASONASSISTS] + player[CAREERASSISTS]*player[CAREERGAMES])/(1+player[CAREERGAMES])
            player[CAREERBLOCKS] = (player[SEASONBLOCKS] + player[CAREERBLOCKS]*player[CAREERGAMES])/(1+player[CAREERGAMES])
            player[CAREERGAMES] += 1

            print("*\tName: {:10}  \tPosition: {}  \tOffense: {}  \tDefense: {} \tYear: {}\tAve: {:4.3}\tCareer: {:4.3}\tReb Ave: {:4.3}\tAst Avg: {:4.3}"
                  "".format(player[NAME], player[POSITION], player[OFFENSEEST], player[DEFENSEEST], player[YEAR], player[SEASONTOTAL]/10,
                            player[CAREERTOTAL]/10, player[CAREERREBOUNDS]/10, player[CAREERASSISTS]/10))
            player[SEASONTOTAL] = 0  # reset season average
            player[SEASONREBOUNDS] = 0  # reset season average
            player[SEASONASSISTS] = 0  # reset season average
            player[SEASONBLOCKS] = 0  # reset season average
            player[SEASONEXP] = 0   # reset season experience

    for player in removeList:
        benchList.remove(player)

    print("*")

    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit1 = [name1, "Center", 3 + random.randint(0, 1), 3 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, BENCHED]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit2 = [name1, "Forward", 3 + random.randint(0, 1), 3 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, BENCHED]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit3 = [name1, "Forward", 3 + random.randint(0, 1), 3 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, BENCHED]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit4 = [name1, "Guard", 3 + random.randint(0, 1), 3 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, BENCHED]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit5 = [name1, "Guard", 3 + random.randint(0, 1), 3 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, BENCHED]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit6 = [name1, "Center", 3 + random.randint(0, 1), 3 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, BENCHED]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit7 = [name1, "Forward", 3 + random.randint(0, 1), 3 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, BENCHED]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit8 = [name1, "Guard", 3 + random.randint(0, 1), 3 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, BENCHED]

    recruits = [recruit1, recruit2, recruit3, recruit4, recruit5, recruit6, recruit7, recruit8]

    # boost some recruit candidates scores
    index = 1
    for player in recruits:
        index += 1
    for player in recruits:
        boostCheck = random.random()
        if boostCheck >= 0.8:
            player[OFFENSE] += 1
        boostCheck = random.random()
        if boostCheck >= 0.8:
            player[DEFENSE] += 1

    # Assign assist factor for each new recruit
    for player in recruits:
        if player[POSITION] == "Guard":
            player[ASSISTS] = 3 + random.randint(0,2)
        else:
            player[ASSISTS] = 1 + random.randint(0,2)

    # Assign block factor for each new recruit
    for player in recruits:
        if player[POSITION] == "Center":
            player[BLOCKS] = 1 + random.randint(0,2)
        elif player[POSITION] == "Forward":
            player[BLOCKS] = random.randint(0,1)

    # determine offense and defense score factor estimates
    # only the estimates will be viewed during recruiting
    for player in recruits:
        updateOffDeffEstimates(player, 0.25, 0.75, True)

    print("*******************************************************")
    print("*")
    print("*\tRecruiting Time!")
    print("*")
    print("*******************************************************")
    index = 1
    for player in recruits:
        print("#{} \tName: {:10}  \tPosition: {}  \tOffense: {}  \tDefense: {} \tYear: {}"
              "".format(index, player[NAME], player[POSITION], player[OFFENSEEST], player[DEFENSEEST], player[YEAR]))
        index += 1

    selectedRecruits = []
    for i in range(0, 4):
        noInput = True
        while noInput == True:
            print("Select Recruit #{}".format(i+1))
            numberValue = input()
            # if numberValue in "12345678":
            if numberValue.isdigit():
                number = int(numberValue)
                if 1 <= number <= 8:
                    noInput = False

        selectedRecruits.append(list(recruits[number-1]))
        print("Selected: {}".format(recruits[number-1][NAME]))


    # put all the team members (prior starters, prior bench, new recruits) into one list
    for player in benchList:
        team.append(list(player))
    benchList = []
    print("Here are the selected recruits:")
    for player in selectedRecruits:
        print("Name: {:10}  \tPosition: {}  \tOffense: {}  \tDefense: {} \tYear: {}"
              "".format(player[NAME], player[POSITION], player[OFFENSEEST], player[DEFENSEEST], player[YEAR]))
        team.append(list(player))

    input("Type Enter to Continue")

    # sort the team
    newTeamOrder = []
    for player in team:
        if player[POSITION] == "Center":
            newTeamOrder.append(list(player))
    for player in team:
        if player[POSITION] == "Forward":
            newTeamOrder.append(list(player))
    for player in team:
        if player[POSITION] == "Guard":
            newTeamOrder.append(list(player))
    team = newTeamOrder

    done = False
    removeList = []
    while not done:
        print()
        print("*******************************************************")
        print("*")
        print("*\tHere is the new team")
        print("*")
        print("*******************************************************")
        for player in team:
            print("*\t{:10}\t\tAvg: {:4.1f}\t\tReb Avg: {:4.1f}\t\tAst Avg: {:4.1f}\t\tBlk Avg: {:4.1f}\t{}\t\t{:10}\tOff: {}\t\t Def: {}"
                  "".format(player[NAME], player[CAREERTOTAL]/gameNumber, player[CAREERREBOUNDS]/gameNumber,
                            player[CAREERASSISTS]/gameNumber, player[CAREERBLOCKS]/gameNumber, player[POSITION], player[YEAR], player[OFFENSEEST], player[DEFENSEEST]))

        print("Decide who to bench for the next season")

        for player in team:
            print("Bench {}? Y or N".format(player[NAME]))
            answer = input()
            if (answer == "Y") or (answer == 'y'):
                removeList.append(list(player))
        for player in removeList:
            if player in team:
                team.remove(player)

        if len(team) == 5:
            done = True

        benchList = list(removeList)

    print("*******************************************************")
    print("*")
    print("*\tStarting Team")
    print("*")
    print("*******************************************************")
    teamOffense = 0
    teamDefense = 0
    for player in team:
        print("Name: {:10}  \tPosition: {}  \tOffense: {}  \tDefense: {} \tYear: {}"
              "".format(player[NAME], player[POSITION], player[OFFENSEEST], player[DEFENSEEST], player[YEAR]))
        teamOffense += player[OFFENSE]/5
        teamDefense += player[DEFENSE]/5

    print("*******************************************************")
    print("*")
    print("*\tBench Team")
    print("*")
    print("*******************************************************")
    for player in benchList:
        print("Name: {:10}  \tPosition: {}  \tOffense: {}  \tDefense: {} \tYear: {}"
              "".format(player[NAME], player[POSITION], player[OFFENSEEST], player[DEFENSEEST], player[YEAR]))


    benchOffense = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    benchDefense = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for player in benchList:
        benchOffense[player[OFFENSE]] += 1
        benchDefense[player[DEFENSE]] += 1
        # print("Offense Vector", benchOffense)
        # print("Defense Vector", benchDefense)

    topThreeOffIncr = 0
    topThreeDefIncr = 0
    topThreeOff = 0
    topThreeDef = 0
    for index in range(9,-1,-1):
        # print("Index {}".format(index))
        if benchOffense[index] != 0:
            while (topThreeOffIncr < 3) and (benchOffense[index] > 0):
                # print("OFF While Loop topThreeOffIncr {}  benchOffense index {}".format(topThreeOffIncr, benchOffense[index]))
                topThreeOffIncr += 1
                benchOffense[index] -= 1
                topThreeOff += index
        if benchDefense[index] != 0:
            while (topThreeDefIncr < 3) and (benchDefense[index] > 0):
                # print("DEF While Loop topThreeOffIncr {}  benchOffense index {}".format(topThreeOffIncr, benchOffense[index]))
                topThreeDefIncr += 1
                benchDefense[index] -= 1
                topThreeDef += index
    topThreeOff /= 3
    topThreeDef /=3

    # print("Average Bench Offense {}".format(topThreeOff))
    # print("Average Bench Defense {}".format(topThreeDef))

    resultList = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    updateTeamOffDefStats(team, benchList, resultList)
    teamOffense, teamDefense, topThreeOff, topThreeDef,  = resultList[0], resultList[1], resultList[2], resultList[3]
    assistFactor = resultList[4]
    blockFactor = resultList[5]
    passingSummary, startingOffSummary, startingDefSummary, benchOffSummary, benchDefSummary, blockSummary = convertTeamStatsToText(assistFactor, teamOffense, teamDefense, topThreeOff, topThreeDef, blockFactor)

    print("*******************************************************")
    print("*")
    print("*\tTeam Scorecard")
    print("*")
    print("*\tStarting Offense: \t{:2}\tStarting Defense: \t{:2}".format(startingOffSummary, startingDefSummary))
    print("*\tBench Offense: \t\t{:2}\tBench Defense: \t\t{:2}".format(benchOffSummary, benchDefSummary))
    print("*\tPassing Report\t\t{:2}\tBlocking Report: \t{:2}".format(passingSummary, blockSummary))
    print("*")
    print("*******************************************************")

    input("Type Enter to Continue: ")
