
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
ASSISTEST = 24          # Estimate of Assists Factor, visible to the game player
BLOCKEST = 25           # Estimate of Block Factor, visible to the game player
REDSHIRTSEASON =26      # Boolean indicating if this player has been red shirted
RECRUITCOST = 27        # Integer - how many recruiting tokens does it take to recruit this player
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

        randomNumber = random.random()
        player[ASSISTEST] = player[ASSISTS]
        if randomNumber < boundaryLow:
            player[ASSISTEST] += 1
        elif randomNumber > boundaryHigh:
            player[ASSISTEST] = max(0, player[ASSISTEST]-1)

        randomNumber = random.random()
        player[BLOCKEST] = player[BLOCKS]
        if randomNumber < boundaryLow:
            player[BLOCKEST] += 1
        elif randomNumber > boundaryHigh:
            player[BLOCKEST] = max(0, player[BLOCKEST]-1)
    else:
        randomNumber = random.random()
        player[OFFENSEEST] = player[OFFENSE]
        if (randomNumber < boundaryLow) and (player[OFFENSE] < 6):
            player[OFFENSEEST] += 1
        elif (randomNumber > boundaryHigh) and (player[OFFENSE] > 3):
            if player[RECRUITCOST] != 6:
                player[OFFENSEEST] -= 1

        randomNumber = random.random()
        player[DEFENSEEST] = player[DEFENSE]
        if (randomNumber < boundaryLow) and (player[DEFENSE] < 6):
            player[DEFENSEEST] += 1
        elif (randomNumber > boundaryHigh) and (player[DEFENSE] > 3):
            if player[RECRUITCOST] != 6:
                player[DEFENSEEST] -= 1

        randomNumber = random.random()
        player[ASSISTEST] = player[ASSISTS]
        if (randomNumber < boundaryLow) and (player[ASSISTS] < 6):
            player[ASSISTEST] += 1
        elif (randomNumber > boundaryHigh) and (player[ASSISTS] > 3):
            if player[RECRUITCOST] != 6:
                player[ASSISTEST] -= 1

        randomNumber = random.random()
        player[BLOCKEST] = player[BLOCKS]
        if (randomNumber < boundaryLow) and (player[BLOCKS] < 6):
            player[BLOCKEST] += 1
        elif (randomNumber > boundaryHigh) and (player[BLOCKS] > 3):
            if player[RECRUITCOST] != 6:
                player[BLOCKEST] -= 1

    return

########################################################
#
#   Initialize team lineups
#
#   Setup team players for the very beginning
#   of the game. The players are the actual players from the 1979
#   MSU team.
#
#######################################################
def initPlayerLists(team):

    # [0 - name, 1 - position, 2 - offense, 3 - defense, 4 - year, 5 - game score, 6 - season total,
    # 7 - career total, 8 - career games, 9 - offense estimate, 10 - defense estimate]
    # 11 - game rebounds, 12 - rebound season total, 13 - career rebound total
    team.append(["Ron", "Center", 5, 6, "Senior", 0, 0, 105, 0, 0, 0, 0, 0, 55, 0, 0, 0, 2, 2, 0, 0, 0, 0, STARTER, 0, 0, 0, 0])
    team.append(["Rob", "Forward", 3, 3, "Sophomore", 0, 0, 15, 0, 0, 0, 0, 0, 5, 0, 0, 0,2, 0, 0, 0, 0, 0, STARTER, 0, 0, 0, 0])
    team.append(["Jay", "Forward", 6, 6, "Junior", 0, 0, 157, 0, 0, 0, 0, 0, 65, 0, 0, 0, 2, 0, 0, 0, 0, 0, STARTER, 0, 0, 0, 0])
    team.append(["Mike", "Guard", 4, 3, "Junior", 0, 0, 63, 0, 0, 0, 0, 0, 30, 0, 0, 0, 3, 0, 0, 0, 0, 0, STARTER, 0, 0, 0, 0])
    team.append(["Terry", "Guard", 4, 4, "Senior", 0, 0, 55, 0, 0, 0, 0, 0, 19, 0, 0, 0, 5, 0, 0, 0, 0, 0, STARTER, 0, 0, 0, 0])
    team.append(["Steve", "Center", 2, 3, "Sophomore", 0, 0, 7, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 1, 0, 0, 0, 0, ROTATION, 0, 0, 0, 0])
    team.append(["Derek", "Forward", 3, 4, "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 0])
    team.append(["Kurt", "Forward", 2, 4, "Junior", 0, 0, 15, 0, 0, 0, 0, 0, 10, 0, 0, 0, 2, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 0])
    team.append(["Herb", "Guard", 2, 3, "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, BENCHED, 0, 0, 0, 0])
    team.append(["Kevin", "Guard", 4, 4, "Sophomore", 0, 0, 25, 0, 0, 0, 0, 0, 20, 0, 0, 0, 4, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 0])
    team.append(["Don", "Forward", 2, 3, "Sophomore", 0, 0, 7, 0, 0, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0, 0, 0, BENCHED, 0, 0, 0, 0])
    team.append(["Bill", "Guard", 2, 3, "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, BENCHED, 0, 0, 0, 0])
    team.append(["Mike", "Guard", 3, 3, "Senior", 0, 0, 11, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 0])
    team.append(["Richard", "Forward", 2, 3, "Junior", 0, 0, 8, 0, 0, 0, 0, 0, 4, 0, 0, 0, 2, 0, 0, 0, 0, 0, BENCHED, 0, 0, 0, 0])

    # determine offense and defense score factor estimates
    # only the estimates will be viewed during recruiting
    for player in team:
        updateOffDeffEstimates(player, 0.1, 0.9, False)

    return


########################################################
#
#   Provide Opportunity to update offense score factor update
#
#   Input from game player player number of player to update.
#   Input the new offensive factor to use.
#
#######################################################
def updateOffenseEstimate(team):
    # give option to update offensive scoring factor estimates
    Done = False
    while not Done:
        print("*  Enter player number to be updated or enter 0 to exit")
        response = input()
        if response.isdigit():
            response = int(response)
            if response == 0:
                Done = True
            else:
                response1 = int(input("*  Enter new offensive estimate for {} ".format(team[response-1][NAME])))
                team[response-1][OFFENSEEST] = response1
    return

def updateDefenseEstimate(team):
    # give option to update offensive scoring factor estimates
    Done = False
    while not Done:
        print("*  Enter player number to be updated or enter 0 to exit")
        response = input()
        if response.isdigit():
            response = int(response)
            if response == 0:
                Done = True
            else:
                response1 = int(input("*  Enter new defensive estimate for {} ".format(team[response-1][NAME])))
                team[response-1][DEFENSEEST] = response1

    return

########################################################
#
#   Provide Opportunity to update starting line up
#
#   Input from game player player numbers to swap.
#   Assumption is that first number is from the starting lineup
#   and the second number is from the bench line up.
#
#######################################################
def updateStartingLineup(team):
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
                    team[response1-1][PLAYERSTATUS] =  ROTATION
                    team[response2-1][PLAYERSTATUS] = STARTER
                    tempPlayer = list(team[response1-1])
                    team[response1-1] = team[response2]
                    team[response2-1] = tempPlayer
    return

########################################################
#
#   Covert Team Stats from Float to Text Assessment
#
#   Assign grades (D, C, B, A-, A) for team statistics
#
#######################################################
def convertTeamStatsToText(assistFactor, teamOffense, teamDefense, topThreeOff, topThreeDef, blockFactor):

    if assistFactor <= 1:
        passingSummary = "E"
    elif assistFactor <= 2:
        passingSummary = "D"
    elif assistFactor <= 3:
        passingSummary = "C"
    elif assistFactor <= 5:
        passingSummary = "B"
    elif assistFactor <= 7:
        passingSummary = "A-"
    else:
        passingSummary = "A"

    if teamDefense <= 2.5:
        blockSummary = "E"
    elif blockFactor <= 3:
        blockSummary = "D"
    elif blockFactor <= 3.5:
        blockSummary = "C"
    elif blockFactor <= 5:
        blockSummary = "B"
    elif blockFactor <= 7:
        blockSummary = "A-"
    else:
        blockSummary = "A"

    if teamOffense <= 3.0:
        startingOffSummary = "E"
    elif teamOffense <= 3.5:
        startingOffSummary = "D"
    elif teamOffense <= 4:
        startingOffSummary = "C"
    elif teamOffense <= 4.5:
        startingOffSummary = "B"
    elif teamOffense <= 5:
        startingOffSummary = "A-"
    else:
        startingOffSummary = "A"

    if teamDefense <= 3.0:
        startingDefSummary = "E"
    elif teamDefense <= 3.5:
        startingDefSummary = "D"
    elif teamDefense <= 4.0:
        startingDefSummary = "C"
    elif teamDefense <= 4.5:
        startingDefSummary = "B"
    elif teamDefense <= 5:
        startingDefSummary = "A-"
    else:
        startingDefSummary = "A"

    if topThreeOff <= 3.0:
        benchOffSummary = "E"
    elif topThreeOff <= 3.5:
        benchOffSummary = "D"
    elif topThreeOff <= 4:
        benchOffSummary = "C"
    elif topThreeOff <= 4.5:
        benchOffSummary = "B"
    elif topThreeOff <= 5:
        benchOffSummary = "A-"
    elif topThreeOff <= 5.5:
        benchOffSummary = "A"
    else:
        benchOffSummary = "A+"

    if topThreeDef <= 3.0:
        benchDefSummary = "E"
    elif topThreeDef <= 3.5:
        benchDefSummary = "D"
    elif topThreeDef <= 4:
        benchDefSummary = "C"
    elif topThreeDef <= 4.5:
        benchDefSummary = "B"
    elif topThreeDef <= 5:
        benchDefSummary = "A-"
    elif topThreeDef <= 5.5:
        benchDefSummary = "A"
    else:
        benchDefSummary = "A+"

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
def updateTeamOffDefStats(team, resultList):
    #   resultList[0] = teamOffense
    #   resultList[1] = teamDefense
    #   resultList[2] = topThreeOff
    #   resultList[3] = topThreeDef
    #   resultList[4] = teamAssist
    #   resultList[5] = teamBlocks

    teamOffense = 0     # average offensive factor of the starters
    teamDefense = 0     # average defensive factor of the starters
    benchOffense = 0     # average offensive factor of the starters
    benchDefense = 0     # average defensive factor of the starters
    teamAssistMax = 0      # max assist factor of the starters
    teamAssist = 0      # average assist factor of the starters
    teamBlocks = 0
    rotationCount = 0
    for player in team:
        if (player[PLAYERSTATUS] == STARTER):
            teamOffense += player[OFFENSE]/5
            teamDefense += player[DEFENSE]/5
            teamAssistMax = max(teamAssistMax, player[ASSISTS])
            teamAssist += player[ASSISTS]/5
        elif (player[PLAYERSTATUS] == ROTATION):
            benchOffense += player[OFFENSE]
            benchDefense += player[DEFENSE]
            rotationCount += 1
    benchOffense = benchOffense / rotationCount
    benchDefense = benchDefense / rotationCount

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
        if (player[PLAYERSTATUS] == STARTER):
            teamBlocks += player[BLOCKS]

    resultList[0] = teamOffense
    resultList[1] = teamDefense
    resultList[2] = benchOffense
    resultList[3] = benchDefense
    resultList[2] = benchOffense
    resultList[3] = benchDefense
    resultList[5] = teamBlocks

    return

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

def convertStatus(statusNumber):
    if statusNumber == 0:
        return ("Starter")
    elif statusNumber == 1:
        return("Rotation")
    elif statusNumber == 2:
        return("Benched")
    elif statusNumber == 3:
        return("Red Shirt")
    else:
        return("ERROR")

def conODA(number):
    grade = ["E", "D", "C", "B", "B+","A-", "A", "A+", "A++", "A+++"]
    return(grade[number-1])

def conBlock(number):
    grade = ["D", "C", "B", "B+","A-", "A", "A+", "A++", "A+++"]
    return(grade[number])

def conExp(experience, gameNumber):
    if gameNumber == 0:
        print("ERROR gameNumber cannot be zero")
        return
    if (experience/gameNumber == 3):
        return("A")
    elif (experience/gameNumber >= 2.25):
        return("A-")
    elif (experience/gameNumber >= 2):
        return("B")
    elif (experience/gameNumber >= 1.5):
        return("C")
    elif (experience/gameNumber >= 1.0):
        return("D")
    else:
        return("E")


def bubbleSortTeam(team):
    done = False
    while not done:
        swappedPlayers = False
        for index in range (1,len(team)):
            if team[index][PLAYERSTATUS] < team[index-1][PLAYERSTATUS]:
                tempPlayer = team[index-1]
                team[index-1] = team[index]
                team[index] = tempPlayer
                swappedPlayers = True
            elif (team[index][PLAYERSTATUS] == team[index-1][PLAYERSTATUS]) and (team[index][POSITION] == "Center" and ((team[index-1][POSITION] == "Forward") or ((team[index-1][POSITION] == "Guard")))):
                tempPlayer = team[index-1]
                team[index-1] = team[index]
                team[index] = tempPlayer
                swappedPlayers = True
            elif (team[index][PLAYERSTATUS] == team[index-1][PLAYERSTATUS]) and (team[index][POSITION] == "Forward" and (team[index-1][POSITION] == "Guard")):
                tempPlayer = team[index-1]
                team[index-1] = team[index]
                team[index] = tempPlayer
                swappedPlayers = True
        if not swappedPlayers:
            done = True


def sortTeamOrder(team):
    done = False
    while not done:
        # find last player with status rotation
        index = 0
        rotationIndex = 0
        for player in team:
            if (player[PLAYERSTATUS] == ROTATION):
                rotationIndex = index
            index += 1
        # find first player with status Benched
        index = 0
        benchedIndex = 0
        found = False
        for player in team:
            if (player[PLAYERSTATUS] == BENCHED) and (not found):
                benchedIndex = index
                found = True
            index += 1
        if (benchedIndex < rotationIndex):
            tempPlayer = team[rotationIndex]
            team[rotationIndex] = team[benchedIndex]
            team[benchedIndex] = tempPlayer
        else:
            done = True
    return()


def displayMenu(team, gameNumber):
    print("*******************************************************")
    print("*")
    print("* Select Option")
    print("*\t\t0 or Enter:\t\tContinue")
    print("*\t\t1:\t\t\t\tChange playing status of a player")
    print("*\t\t2:\t\t\t\tList Roster with Statistics")
    print("*\t\t3:\t\t\t\tUpdate player offense factor")
    print("*\t\t4:\t\t\t\tUpdate player defense factor")
    print("*")
    print("*******************************************************")

    if gameNumber <= 0:
        gameNumber = 1
    Done = False
    while not Done:
        response = input(">")
        if response.isdigit():
            response = int(response)
            if response == 0:
                Done = True
            elif response == 1:
                response = input(">> Input Number of player and new status (0 - Starter, 1 - Rotation, 2 - Benched, 3 - Red Shirt ")
                if len(response) >= 3:
                    noLetters = True
                    for character in response:
                        if character.isalpha():
                            noLetters = False
                    if noLetters:
                        response1, response2 = response.split()
                        if response1.isdigit():
                            response1 = int(response1)
                            if response2 in ["0", "1", "2"]:
                                response2 = int(response2)
                                team[response1-1][PLAYERSTATUS] = response2
                            elif (response2 == "3") and (not team[response1-1][REDSHIRTSEASON]) and \
                                    (gameNumber < 3) and (team[response1-1][YEAR] == "Freshman"):
                                # only assign the player to REDSHIRT if less than 3 games have been played,
                                # and the player has not been a redshirt before (only 1 season as a red shirt is allowed),
                                # and the player is a freshman
                                team[response1-1][PLAYERSTATUS] = REDSHIRT
                                team[response1-1][REDSHIRTSEASON] = 1
            elif response == 2:
                bubbleSortTeam(team)
                index1 = 1
                for player in team:
                    print("*\t{}\t{:10}\t\tAvg: {:4.1f}\t\tReb Avg: {:4.1f}\t\tAst: Avg: {:4.1f}\t\tBlk Avg: {:4.1f}\t{}\t\t{:10}\tOff: {:2}\t\t Def: {:2}\tAsst: {:2}\t\tBlk: {:2}\t\tExp: {}\tStatus: {}"
                          "".format(index1, player[NAME], player[SEASONTOTAL]/gameNumber, player[SEASONREBOUNDS]/gameNumber,
                                    player[SEASONASSISTS]/gameNumber, player[SEASONBLOCKS]/gameNumber, player[POSITION],
                                    player[YEAR], conODA(player[OFFENSEEST]), conODA(player[DEFENSEEST]),
                                    conODA(player[ASSISTEST]), conBlock(player[BLOCKEST]),
                                    conExp(player[SEASONEXP],gameNumber), convertStatus(player[PLAYERSTATUS])))
                    index1 += 1
            elif response == 3:
                updateOffenseEstimate(team)
            elif response == 4:
                updateDefenseEstimate(team)
        else:
            Done = True
    return


def playGreenAndWhiteGame(team):
    gameNumber = 0 # as this game happens before the first game, but do not want divide by zero error
    greenTeam = []
    whiteTeam = []
    index = 0
    greenStarterCount = 0
    whiteStarterCount = 0
    for player in team:
        if (index%2 == 0):
            greenTeam.append(list(player))
            if greenStarterCount < 5:
                greenTeam[greenStarterCount][PLAYERSTATUS] = STARTER
            else:
                greenTeam[greenStarterCount][PLAYERSTATUS] = ROTATION
            greenStarterCount += 1
        else:
            whiteTeam.append(list(player))
            if whiteStarterCount < 5:
                whiteTeam[whiteStarterCount][PLAYERSTATUS] = STARTER
            else:
                whiteTeam[whiteStarterCount][PLAYERSTATUS] = ROTATION
            whiteStarterCount += 1
        index  += 1

    print("*")
    print("*\tGreen and White Scrimmage Game")
    print("*")
    print("*******************************************************")
    print("*")
    print("*\tSetup Green Team")
    print("*")

    displayMenu(greenTeam, gameNumber)
    # since lineup may have changed, need to update team stats
    resultList = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    updateTeamOffDefStats(greenTeam, resultList)
    greenTeamOffense, greenTeamDefense, greenBenchOffense, greenBenchDefense,  = resultList[0], resultList[1], resultList[2], resultList[3]
    greenAssistFactor = resultList[4]
    greenBlockFactor = resultList[5]

    greenPassingSummary, greenStartingOffSummary, greenStartingDefSummary, greenBenchOffSummary, greenBenchDefSummary, greenBlockSummary = \
        convertTeamStatsToText(greenAssistFactor, greenTeamOffense, greenTeamDefense, greenBenchOffense, greenBenchDefense, greenBlockFactor)

    print("*******************************************************")
    print("*")
    print("*\tGreen Team Scorecard")
    print("*")
    print("*\tStarting Offense: \t{} \tStarting Defense: \t{}".format(greenStartingOffSummary, greenStartingDefSummary))
    print("*\tBench Offense: \t\t{}  \tBench Defense: \t\t{}".format(greenBenchOffSummary, greenBenchDefSummary))
    print("*\tPassing Report\t\t{} \tBlocking Report: \t{}".format(greenPassingSummary, greenBlockSummary))
    print("*")
    print("*******************************************************")
    print("*")
    print("\tSet up White Team")
    print("*")

    displayMenu(whiteTeam, gameNumber)
    # since lineup may have changed, need to update team stats
    resultList = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    updateTeamOffDefStats(whiteTeam, resultList)
    whiteTeamOffense, whiteTeamDefense, whiteBenchOffense, whiteBenchDefense,  = resultList[0], resultList[1], resultList[2], resultList[3]
    whiteAssistFactor = resultList[4]
    whiteBlockFactor = resultList[5]

    whitePassingSummary, whiteStartingOffSummary, whiteStartingDefSummary, whiteBenchOffSummary, whiteBenchDefSummary, whiteBlockSummary = \
        convertTeamStatsToText(whiteAssistFactor, whiteTeamOffense, whiteTeamDefense, whiteBenchOffense, whiteBenchDefense, whiteBlockFactor)

    print("*******************************************************")
    print("*")
    print("*\tWhite Team Scorecard")
    print("*")
    print("*\tStarting Offense: \t{} \tStarting Defense: \t{}".format(whiteStartingOffSummary, whiteStartingDefSummary))
    print("*\tBench Offense: \t\t{}  \tBench Defense: \t\t{}".format(whiteBenchOffSummary, whiteBenchDefSummary))
    print("*\tPassing Report\t\t{} \tBlocking Report: \t{}".format(whitePassingSummary, whiteBlockSummary))
    print("*")
    print("*******************************************************")
    print("*")
    print("* Type enter to play game")
    print("*")
    print("*******************************************************")
    input()

    greenOffense = (greenTeamOffense*2 + greenBenchOffense)/3 + random.random()*2 - 1
    greenDefense = (greenTeamDefense*2 + greenBenchDefense)/3 + random.random()*2 - 1
    whiteOffense = (whiteTeamOffense*2 + whiteBenchOffense)/3 + random.random()*2 - 1
    whiteDefense = (whiteTeamDefense*2 + whiteBenchDefense)/3 + random.random()*2 - 1

    # determine points scored for this game
    greenTeamScore = int((greenOffense - whiteDefense)*10 + 60) + min(int(greenAssistFactor),8)  - min(int(whiteBlockFactor)*2,8)
    whiteTeamScore = int((whiteOffense - greenDefense)*10 + 60) + min(int(whiteAssistFactor),8)  - min(int(greenBlockFactor)*2,8)

    greenTeamRebounds = int(greenTeamScore/2)
    whiteTeamRebounds = int(whiteTeamScore/2)

    print("*******************************************************")
    print("*")
    print("*\tGreen: {}\t\tWhite:  {}".format(greenTeamScore, whiteTeamScore ))
    print("*")

    allocateStatsToPlayers(greenTeam, greenTeamScore, greenAssistFactor, greenBlockFactor)

    gameNumber = 1  # set to one to avoid divide by zero errors (even though this game does not count)
    print("*******************************************************")
    print("* Green Team Results")
    for player in greenTeam:
        print("*\t{:10}\t\tAvg: {:4.1f}\t\tReb Avg: {:4.1f}\t\tAst: Avg: {:4.1f}\t\tBlk Avg: {:4.1f}\t{}\t\t{:10}\tOff: {:2}\t\t Def: {:2}\tAsst: {:2}\t\tBlk: {:2}\t\tExp: {}\tStatus: {}"
              "".format(player[NAME], player[SEASONTOTAL]/gameNumber, player[SEASONREBOUNDS]/gameNumber,
                        player[SEASONASSISTS]/gameNumber, player[SEASONBLOCKS]/gameNumber, player[POSITION],
                        player[YEAR], conODA(player[OFFENSEEST]), conODA(player[DEFENSEEST]),
                        conODA(player[ASSISTEST]), conBlock(player[BLOCKEST]),
                    conExp(player[SEASONEXP],gameNumber), convertStatus(player[PLAYERSTATUS])))
        # do not count this game towards season totals
        player[SEASONEXP] = 0
        player[SEASONTOTAL] = 0
        player[SEASONREBOUNDS] = 0
        player[SEASONASSISTS] = 0
        player[SEASONBLOCKS] = 0
    print("*******************************************************")
    print("* White Team Results")
    allocateStatsToPlayers(whiteTeam, whiteTeamScore, whiteAssistFactor, whiteBlockFactor)
    for player in whiteTeam:
        print("*\t{:10}\t\tAvg: {:4.1f}\t\tReb Avg: {:4.1f}\t\tAst: Avg: {:4.1f}\t\tBlk Avg: {:4.1f}\t{}\t\t{:10}\tOff: {:2}\t\t Def: {:2}\tAsst: {:2}\t\tBlk: {:2}\t\tExp: {}\tStatus: {}"
              "".format(player[NAME], player[SEASONTOTAL]/gameNumber, player[SEASONREBOUNDS]/gameNumber,
                        player[SEASONASSISTS]/gameNumber, player[SEASONBLOCKS]/gameNumber, player[POSITION],
                        player[YEAR], conODA(player[OFFENSEEST]), conODA(player[DEFENSEEST]),
                        conODA(player[ASSISTEST]), conBlock(player[BLOCKEST]),
                        conExp(player[SEASONEXP],gameNumber), convertStatus(player[PLAYERSTATUS])))
        # do not count this game towards season totals
        player[SEASONEXP] = 0
        player[SEASONTOTAL] = 0
        player[SEASONREBOUNDS] = 0
        player[SEASONASSISTS] = 0
        player[SEASONBLOCKS] = 0
    print("*******************************************************")

    response = input("* Type ENTER to continue")
    return



    ##################################################
    # Determine Players Chance of Being Allocated Field Goals (Baskets)
    #
    # startingScore and benchScore are the scores of the starting and bench players respectively
    # different factors are used depending on the players offense rating (high factors for starter
    # and those with higher offense ratings
    # scoring factors are determined for each player, then the total score of the game is allocated
    # to each player based on the the players scoring factor divided by the sum of the teams
    ##################################################
def allocateStatsToPlayers(team, teamScore,  assistFactor, blockFactor):
    startingScore = []  # list containing the scoring factor for this game for the starting players
    benchScore = []     # list containing the scoring factor for this game for the bench players
    for player in team:
        if (player[PLAYERSTATUS] == STARTER):
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
        elif (player[PLAYERSTATUS]) == ROTATION:
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
        if (player[PLAYERSTATUS] == STARTER):
            if player[DEFENSE] > 7:
                startingRebounds.append(9*(player[DEFENSE] + 3*random.random()))
            elif player[DEFENSE] > 6:
                startingRebounds.append(7*(player[DEFENSE] + 3*random.random()))
            elif player[DEFENSE] > 5:
                startingRebounds.append(5*(player[DEFENSE] + 3*random.random()))
            elif player[DEFENSE] > 4:
                startingRebounds.append(3*(player[DEFENSE] + 3*random.random()))
            else:
                startingRebounds.append(2*(player[DEFENSE] + 3*random.random()))
        elif (player[PLAYERSTATUS]) == ROTATION:
            if player[DEFENSE] > 4:
                benchRebounds.append((3*player[DEFENSE] + 4*random.random()))
            elif player[DEFENSE] > 3:
                benchRebounds.append((1.5*player[DEFENSE] + 2*random.random()))
            elif (random.random() > 0.5):
                benchRebounds.append((player[DEFENSE] + 2*random.random()))
            else:
                benchRebounds.append(0)

    # determine total rebound factor for the entire team for this game
    totalReboundsFactor = 0
    for reboundFactor in startingRebounds:
        totalReboundsFactor += reboundFactor
    for reboundFactor in benchRebounds:
        totalReboundsFactor += reboundFactor

    teamRebounds = int(teamScore/2)

    ###################################################
    #  Determine Players Chance of Being Allocated Assists
    ###################################################
    # assign assists
    assistsTotal = 10 + assistFactor
    startingAssists = []  # list containing the rebound factor for this game for the starting players
    benchAssists = []     # list containing the rebound factor for this game for the bench players
    for player in team:
        if (player[PLAYERSTATUS] == STARTER):
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
        elif (player[PLAYERSTATUS]) == ROTATION:
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
        if (player[PLAYERSTATUS] == STARTER):
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
        if player[PLAYERSTATUS] == STARTER:
            player[GAMESCORE] = int(round(startingScore[index]/totalScoreFactor*teamScore))
            player[SEASONTOTAL] += player[GAMESCORE]  # accumlate scores across games
            player[GAMEREBOUNDS] = int(round(startingRebounds[index]/totalReboundsFactor*teamRebounds))
            player[SEASONREBOUNDS] += player[GAMEREBOUNDS]  # accumlate scores across games
            player[GAMEASSISTS] = int(round(startingAssists[index]/totalAssistsFactor*assistsTotal))
            player[SEASONASSISTS] += player[GAMEASSISTS]  # accumlate scores across games
            player[GAMEBLOCKS] = int(round(startingBlocks[index]/totalBlockFactor*blocksTotal))
            player[SEASONBLOCKS] += player[GAMEBLOCKS]  # accumlate scores across games
            index +=1
    index = 0
    for player in team:
        if player[PLAYERSTATUS] == ROTATION:
            if int(benchScore[index]/totalScoreFactor*teamScore) == 1:
                if random.random() > 0.3:
                    benchScore[index] *= 2
            player[GAMESCORE] = int(round(benchScore[index]/totalScoreFactor*teamScore))
            player[SEASONTOTAL] += player[GAMESCORE]  # accumlate scores across games
            player[GAMEREBOUNDS] = int(round(benchRebounds[index]/totalReboundsFactor*teamRebounds))
            player[SEASONREBOUNDS] += player[GAMEREBOUNDS]  # accumlate scores across games
            player[GAMEASSISTS] = int(round(benchAssists[index]/totalAssistsFactor*assistsTotal))
            player[SEASONASSISTS] += player[GAMEASSISTS]  # accumlate scores across game
            index +=1
    for player in team:
        if (player[PLAYERSTATUS] == BENCHED) or (player[PLAYERSTATUS] == REDSHIRT):
            player[GAMESCORE] = 0
            player[GAMEREBOUNDS] = 0
            player[GAMEASSISTS] = 0
            index +=1
    return


#****************************************
#
# return the "grade" of the number of wins
#
#****************************************
def conTeamWins(teamWins):
    if teamWins >= 10:
        return("A+")
    elif teamWins >= 9:
        return("A")
    elif teamWins >= 8:
        return("A-")
    elif teamWins >= 7:
        return("B")
    elif teamWins >= 6:
        return("B-")
    elif teamWins >= 5:
        return("C")
    elif teamWins >= 4:
        return("D")
    elif teamWins >= 3:
        return("D-")
    else:
        return("E")

#****************************************
#
# return the "grade" of the team's experienced gained
# during the current season
#
#****************************************
def conTeamExp(teamExperience):
    if teamExperience >= 2.35:
        return("A+")
    elif teamExperience >= 2.25:
        return("A")
    elif teamExperience >= 2.1:
        return("A-")
    elif teamExperience >= 2.0:
        return("B")
    elif teamExperience >= 1.9:
        return("B-")
    elif teamExperience >= 1.7:
        return("C")
    elif teamExperience >= 1.6:
        return("D")
    elif teamExperience >= 1.5:
        return("D-")
    else:
        return("E")

def overallRating(teamWins, teamExperience, lastGameWin):
    lastGame = 0
    if lastGameWin == "A":
        lastGame = 2
    rating = teamWins + teamExperience + lastGame
    if rating >= 14:
        return("A+")
    elif rating >= 13:
        return("A")
    elif rating >= 12:
        return("A-")
    elif rating >= 11:
        return("B+")
    elif rating >= 10:
        return("B")
    elif rating >= 9:
        return("B-")
    elif rating >= 8:
        return("C")
    elif rating >= 7:
        return("D")
    elif rating >= 6:
        return("D-")
    else:
        return("E")


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
initPlayerLists(team)    # add the original players to the team

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
print("*\tPlayer Lineup")
print("*")
print("*******************************************************")
for player in team:
    if player[PLAYERSTATUS] == STARTER:
        print("*\tName: {:10}  \tPosition: {}  \tOffense: {:2}  \tDefense: {:2} \tYear: {}\tAve: {:4.1f}\tCareer: {:4.1f}\tReb Ave: {:4.1f}\tAst Avg: {:4.1f}\tBlk Avg: {:4.1f}\t{}"
              "".format(player[NAME], player[POSITION], conODA(player[OFFENSEEST]), conODA(player[DEFENSEEST]),
                        player[YEAR], player[SEASONTOTAL]/10, player[CAREERTOTAL]/10, player[CAREERREBOUNDS]/10,
                        player[CAREERASSISTS]/10, player[CAREERBLOCKS]/10, "Starter"))
for player in team:
    if player[PLAYERSTATUS] == ROTATION:
        print("*\tName: {:10}  \tPosition: {}  \tOffense: {:2}  \tDefense: {:2} \tYear: {}\tAve: {:4.1f}\tCareer: {:4.1f}\tReb Ave: {:4.1f}\tAst Avg: {:4.1f}\tBlk Avg: {:4.1f}\t{}"
              "".format(player[NAME], player[POSITION], conODA(player[OFFENSEEST]), conODA(player[DEFENSEEST]), player[YEAR], player[SEASONTOTAL]/10,
                        player[CAREERTOTAL]/10, player[CAREERREBOUNDS]/10, player[CAREERASSISTS]/10, player[CAREERBLOCKS]/10, "Bench Rotation"))
for player in team:
    if player[PLAYERSTATUS] == BENCHED:
        print("*\tName: {:10}  \tPosition: {}  \tOffense: {:2}  \tDefense: {:2} \tYear: {}\tAve: {:4.1f}\tCareer: {:4.1f}\tReb Ave: {:4.1f}\tAst Avg: {:4.1f}\tBlk Avg: {:4.1f}\t{}"
              "".format(player[NAME], player[POSITION], conODA(player[OFFENSEEST]), conODA(player[DEFENSEEST]), player[YEAR], player[SEASONTOTAL]/10,
                        player[CAREERTOTAL]/10, player[CAREERREBOUNDS]/10, player[CAREERASSISTS]/10, player[CAREERBLOCKS]/10, "Benched"))
for player in team:
    if player[PLAYERSTATUS] == REDSHIRT:
        print("*\tName: {:10}  \tPosition: {}  \tOffense: {:2}  \tDefense: {:2} \tYear: {}\tAve: {:4.1f}\tCareer: {:4.1f}\tReb Ave: {:4.1f}\tAst Avg: {:4.1f}\tBlk Avg: {:4.1f}\t{}"
              "".format(player[NAME], player[POSITION], conODA(player[OFFENSEEST]), conODA(player[DEFENSEEST]), player[YEAR], player[SEASONTOTAL]/10,
                        player[CAREERTOTAL]/10, player[CAREERREBOUNDS]/10, player[CAREERASSISTS]/10, player[CAREERBLOCKS]/10, "Red Shirt"))

# since lineup may have changed, need to update team stats
resultList = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
updateTeamOffDefStats(team, resultList)
teamOffense, teamDefense, benchOffense, benchDefense  = resultList[0], resultList[1], resultList[2], resultList[3]
assistFactor = resultList[4]
blockFactor = resultList[5]


passingSummary, startingOffSummary, startingDefSummary, benchOffSummary, benchDefSummary, blockSummary = convertTeamStatsToText(assistFactor, teamOffense, teamDefense, benchOffense, benchDefense, blockFactor)

print("*******************************************************")
print("*")
print("*\tTeam Scorecard")
print("*")
print("*\tStarting Offense: \t{} \tStarting Defense: \t{}".format(startingOffSummary, startingDefSummary))
print("*\tBench Offense: \t\t{}  \tBench Defense: \t\t{}".format(benchOffSummary, benchDefSummary))
print("*\tPassing Report\t\t{} \tBlocking Report: \t{}".format(passingSummary, blockSummary))
print("*")
print("*******************************************************")

overallYear = 1978
gameRecord = []
for year in range(1, 21):
    overallYear += 1
    print("*******************************************************")
    print("*")
    print("*\tSeason #{}".format(year))
    print("*")
    print("*******************************************************")
    teamWins = 0
    teamLoses = 0
    playGreenAndWhiteGame(team)
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
        homeOffense = (teamOffense*2 + benchOffense)/3 + random.random()*3 - 1.5
        homeDefense = (teamDefense*2 + benchDefense)/3 + random.random()*3 - 1.5
        teamScore = int((homeOffense - opponent.Defense())*10 + 60)  + min(int(assistFactor),8)
        opponentScore = int((opponent.Offense() - homeDefense)*10 + 65) - min(int(blockFactor)*2,8)
        if teamScore - opponentScore >= 0:
            print("*  Swami Predicts: MSU by {}".format(teamScore - opponentScore))
        else:
            print("*  Swami Predicts: {} by {}".format(opponentList[gameNumber-1], opponentScore - teamScore))

        # give option to change starting lineup
        # updateStartingLineup(team)
        displayMenu(team, gameNumber-1)
        # since lineup may have changed, need to update team stats
        resultList = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        updateTeamOffDefStats(team, resultList)
        teamOffense, teamDefense, benchOffense, benchDefense,  = resultList[0], resultList[1], resultList[2], resultList[3]
        assistFactor = resultList[4]
        blockFactor = resultList[5]

        passingSummary, startingOffSummary, startingDefSummary, benchOffSummary, benchDefSummary, blockSummary = convertTeamStatsToText(assistFactor, teamOffense, teamDefense, benchOffense, benchDefense, blockFactor)

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
        homeOffense = (teamOffense*2 + benchOffense)/3 + random.random()*2 - 1
        homeDefense = (teamDefense*2 + benchDefense)/3 + random.random()*2 - 1

        # determine points scored for this game
        teamScore = int((homeOffense - opponent.Defense())*10 + 60) + min(int(assistFactor),8)
        opponentScore = int((opponent.Offense() - homeDefense)*10 + 65) - min(int(blockFactor)*2,8)
        teamRebounds = int(teamScore/2)
        # adjust score if it is a tied score
        if teamScore == opponentScore:
            teamScore += 1

        allocateStatsToPlayers(team, teamScore,  assistFactor, blockFactor)
        # due to rounding, need to recalculate team score from actual results so that the team score
        # sum of player scores match
        teamScore = 0
        for players in team:
            teamScore += players[GAMESCORE]
        if teamScore == opponentScore:
            teamScore -= 1

        print("*******************************************************")
        print("*")
        # print results and accumulate win / loss
        print("*\tMSU: {}  {}: {}".format(teamScore, opponentList[gameNumber-1], opponentScore))
        if teamScore > opponentScore:
            teamWins += 1
            lastGameWin = "A"
        else:
            teamLoses += 1
            lastGameWin = "E"



        ###################################################
        #  Determine Player Experience
        ###################################################
        #   Current methods for determine experience is that
        #   starting players get 3 experience points for each game, while
        #   bench players either get 1 or 2, depending on if they
        #   contributed to game results
        for player in team:
            if player[PLAYERSTATUS] == STARTER:
                player[SEASONEXP] += 3
            elif player[PLAYERSTATUS] == ROTATION:
                player[SEASONEXP] += 2
            elif player[PLAYERSTATUS] == REDSHIRT:
                player[SEASONEXP] += 1.5
            else:
                player[SEASONEXP] += 1

        ###################################################
        #  Display Team Roster & Statistics
        ###################################################
        print("*\tPlayer Scores")
        index1 = 1
        for player in team:
            print("*\t{}\t{:10}\t{}\t\tAvg: {:4.1f}\t\tReb: {}\t\tAvg: {:4.1f}\t\tAst: {}\t\tAvg: {:4.1f}\t\tBlk: {}\t\tAvg: {:4.1f}\t{}\t\t{:10}\tOff: {:2}\tDef: {:2}\tExp: {}\t{}"
                  "".format(index1, player[NAME], player[GAMESCORE], round(player[SEASONTOTAL]/gameNumber, 2), player[GAMEREBOUNDS], round(player[SEASONREBOUNDS]/gameNumber, 2),
                            player[GAMEASSISTS], round(player[SEASONASSISTS]/gameNumber, 2),  player[GAMEBLOCKS], round(player[SEASONBLOCKS]/gameNumber, 2),
                            player[POSITION], player[YEAR], conODA(player[OFFENSEEST]), conODA(player[DEFENSEEST]), conExp(player[SEASONEXP],gameNumber), convertStatus(player[PLAYERSTATUS])))
            index1 += 1
        print("*")

        displayMenu(team, gameNumber)
        # since lineup may have changed, need to update team stats
        resultList = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        updateTeamOffDefStats(team, resultList)
        teamOffense, teamDefense, benchOffense, benchDefense,  = resultList[0], resultList[1], resultList[2], resultList[3]
        assistFactor = resultList[4]
        blockFactor = resultList[5]

        passingSummary, startingOffSummary, startingDefSummary, benchOffSummary, benchDefSummary, blockSummary = convertTeamStatsToText(assistFactor, teamOffense, teamDefense, benchOffense, benchDefense, blockFactor)

        print("*******************************************************")
        print("*")
        print("*\tTeam Scorecard")
        print("*")
        print("*\tStarting Offense: \t{} \tStarting Defense: \t{}".format(startingOffSummary, startingDefSummary))
        print("*\tBench Offense: \t\t{}  \tBench Defense: \t\t{}".format(benchOffSummary, benchDefSummary))
        print("*\tPassing Report\t\t{} \tBlocking Report: \t{}".format(passingSummary, blockSummary))
        print("*")
        print("*******************************************************")

    ###################################################
    #   End of Season
    ###################################################
    print("*******************************************************")
    print("*")
    print("Final Record: {}-{}".format(teamWins, teamLoses))
    print("*")
    print("*******************************************************")
    input("\nType Enter to Continue: ")

    ###################################################
    #   To support determining Coaches Score, evaluate player experience gained during the season
    ###################################################
    teamExperience = 0
    numPlayers = 0
    for player in team:
        numPlayers += 1
        teamExperience += player[SEASONEXP]
    if numPlayers != 0:
        teamExperience = teamExperience / numPlayers / 10   # this is average player experience per game
    else:
        print("FATAL ERROR: Divide by Zero - numPlayers")

    ###################################################
    #   Display Coach's Score
    ###################################################
    print("*******************************************************")
    print("*")
    print("*\tCoach's Score")
    print("*\tGames Won: {}\t\tPlayer Development: {}".format(conTeamWins(teamWins),conTeamExp(teamExperience)))
    print("\tUofM Game: {}".format(lastGameWin))
    print("\tOverall Rating: {}".format(overallRating(teamWins, teamExperience, lastGameWin)))
    print("*")
    print("*******************************************************")
    input("\nType Enter to Continue: ")

    ###################################################
    #   Display History of Team Record
    ###################################################
    gameRecord.append([overallYear, teamWins, teamLoses, overallRating(teamWins, teamExperience, lastGameWin)])
    print("*******************************************************")
    print("*")
    print("*\tHistory")
    for historyIndex in gameRecord:
        print("*\tYear: {}\tRecord: {}-{}\tCoaches Rating: {}".format(historyIndex[0], historyIndex[1], historyIndex[2], historyIndex[3]))
    print("*")
    print("*******************************************************")
    input("\nType Enter to Continue: ")

    print("*******************************************************")
    print("*\tOld Team")
    for player in team:
        # update career statistics
        player[CAREERTOTAL] = (player[SEASONTOTAL] + player[CAREERTOTAL]*player[CAREERGAMES])/(1+player[CAREERGAMES])
        player[CAREERREBOUNDS] = (player[SEASONREBOUNDS] + player[CAREERREBOUNDS]*player[CAREERGAMES])/(1+player[CAREERGAMES])
        player[CAREERASSISTS] = (player[SEASONASSISTS] + player[CAREERASSISTS]*player[CAREERGAMES])/(1+player[CAREERGAMES])
        player[CAREERBLOCKS] = (player[SEASONBLOCKS] + player[CAREERBLOCKS]*player[CAREERGAMES])/(1+player[CAREERGAMES])
        player[CAREERGAMES] += 1
        # print("*\tName: {:10}  \tPosition: {}  \tOffense: {}  \tDefense: {} \tYear: {}\tAve: {:4.3}\tCareer: {:4.3}"
        #       "".format(player[NAME], player[POSITION], player[OFFENSEEST], player[DEFENSEEST], player[YEAR], player[SEASONTOTAL]/10, player[CAREERTOTAL]/10))

        print("*\t{:10}\t\tAvg: {:4.1f}\t\tCareer: {:4.1f}\t\tReb: {:4.1f}\t\tCareer: {:4.1f}\t\tAst: {:4.1f}\t\tAvg: {:4.1f}\t\tBlk: {:4.1f}\t\tAvg: {:4.1f}\t{:10}\t{}"
              "".format(player[NAME], player[SEASONTOTAL]/10, player[CAREERTOTAL]/10, player[SEASONREBOUNDS]/10, player[CAREERREBOUNDS]/10,
                        player[SEASONASSISTS]/10,  player[CAREERASSISTS]/10, player[SEASONBLOCKS]/10, player[CAREERBLOCKS]/10,
                        player[POSITION], player[YEAR]))

    ###################################################
    #   Update Players Skills Based In Part on Experience Gained
    ###################################################
    print("*******************************************************")
    print("*\tNew Team")
    # teamOffense = 0
    # teamDefense = 0
    removeList = []
    for player in team:
        if player[YEAR] == "Senior":
            removeList.append(player)
            print("*\t{} has graduated".format(player[NAME]))
        else:
            if player[SEASONEXP]/10 >= 3:
                if random.random() > 0.35:
                    player[OFFENSE] += 1
                if random.random() > 0.35:
                    player[DEFENSE] += 1
                if random.random() > 0.35:
                    player[ASSISTS] += 1
                if (player[POSITION] != "GUARD"):
                    if random.random() > 0.35:
                        player[BLOCKS] += 1
            elif player[SEASONEXP]/10 >= 2.25:
                if random.random() > 0.42:
                    player[OFFENSE] += 1
                if random.random() > 0.42:
                    player[DEFENSE] += 1
                if random.random() > 0.42:
                    player[ASSISTS] += 1
                if (player[POSITION] != "GUARD"):
                    if random.random() > 0.42:
                        player[BLOCKS] += 1
            elif player[SEASONEXP]/10 >= 2:
                if random.random() > 0.5:
                    player[OFFENSE] += 1
                if random.random() > 0.5:
                    player[DEFENSE] += 1
                if random.random() > 0.5:
                    player[ASSISTS] += 1
                if (player[POSITION] != "GUARD"):
                    if random.random() > 0.5:
                        player[BLOCKS] += 1
            elif player[SEASONEXP]/10 >= 1.5:
                if random.random() > 0.55:
                    player[OFFENSE] += 1
                if random.random() > 0.55:
                    player[DEFENSE] += 1
                if random.random() > 0.55:
                    player[ASSISTS] += 1
                if (player[POSITION] != "GUARD"):
                    if random.random() > 0.55:
                        player[BLOCKS] += 1
            else:
                if random.random() > 0.65:
                    player[OFFENSE] += 1
                if random.random() > 0.65:
                    player[DEFENSE] += 1
                if random.random() > 0.65:
                    player[ASSISTS] += 1
                if (player[POSITION] != "GUARD"):
                    if random.random() > 0.65:
                        player[BLOCKS] += 1

            if (player[OFFENSE] >= 7) and (player[DEFENSE] >=7):
                # Very good players quite the team and enter the NBA draft
                print("*\t{} has entered the NBA draft".format(player[NAME]))
                removeList.append(player)
            else:
                # update which class the player is for the new year
                # if a freshman was redshirted, then they are still a freshman
                if (player[YEAR] == "Freshman") and (player[PLAYERSTATUS] != REDSHIRT):
                    player[YEAR] = "Sophomore"
                elif player[YEAR] == "Sophomore":
                    player[YEAR] = "Junior"
                else:
                    player[YEAR] = "Senior"
                if (player[PLAYERSTATUS] == REDSHIRT):
                    player[YEAR] = "Freshman"
                    player[PLAYERSTATUS] = ROTATION

                # update offense and defense estimates
                updateOffDeffEstimates(player, 0.1, 0.9, False)

                print("*\tName: {:10}  \tPosition: {}  \tOffense: {:2}  \tDefense: {:2} \tYear: {}\tAve: {:4.1f}\tCareer: {:4.1f}\tReb Ave: {:4.1f}\tAst Avg: {:4.1f}\tStatus: {}"
                        "".format(player[NAME], player[POSITION], conODA(player[OFFENSEEST]), conODA(player[DEFENSEEST]), player[YEAR], player[SEASONTOTAL]/10,
                                player[CAREERTOTAL]/10, player[CAREERREBOUNDS]/10, player[CAREERASSISTS]/10, convertStatus(player[PLAYERSTATUS])))
                player[SEASONTOTAL] = 0  # reset season average
                player[SEASONREBOUNDS] = 0  # reset season average
                player[SEASONASSISTS] = 0  # reset season average
                player[SEASONBLOCKS] = 0  # reset season average
                player[SEASONEXP] = 0   # reset season experience

    for player in removeList:
        if player in team:
            team.remove(player)
    print("*******************************************************")
    print("*")
    print("*\tConsider updating player status before recruiting")
    print("*")
    displayMenu(team, 1)

    resultList = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    updateTeamOffDefStats(team, resultList)
    teamOffense, teamDefense, benchOffense, benchDefense,  = resultList[0], resultList[1], resultList[2], resultList[3]
    assistFactor = resultList[4]
    blockFactor = resultList[5]
    passingSummary, startingOffSummary, startingDefSummary, benchOffSummary, benchDefSummary, blockSummary = convertTeamStatsToText(assistFactor, teamOffense, teamDefense, benchOffense, benchDefense, blockFactor)
    print("*******************************************************")
    print("*")
    print("*\tTeam Scorecard")
    print("*")
    print("*\tStarting Offense: \t{:2} \tStarting Defense: \t{}".format(startingOffSummary, startingDefSummary))
    print("*\tBench Offense: \t\t{:2} \tBench Defense: \t\t{}".format(benchOffSummary, benchDefSummary))
    print("*\tPassing Report\t\t{:2} \tBlocking Report: \t{}".format(passingSummary, blockSummary))
    print("*")
    print("*******************************************************")

    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit1 = [name1, "Center", 3 + random.randint(0, 1), 3 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 3]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit2 = [name1, "Forward", 3 + random.randint(0, 1), 3 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 3]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit3 = [name1, "Forward", 3 + random.randint(0, 1), 3 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 3]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit4 = [name1, "Guard", 3 + random.randint(0, 1), 3 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 3]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit5 = [name1, "Guard", 3 + random.randint(0, 1), 3 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 3]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit6 = [name1, "Center", 3 + random.randint(0, 1), 3 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 3]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit7 = [name1, "Forward", 3 + random.randint(0, 1), 3 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 3]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit8 = [name1, "Guard", 3 + random.randint(0, 1), 3 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 3]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit9 = [name1, "Center", 4 + random.randint(0, 1), 4 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 6]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit10 = [name1, "Forward", 4 + random.randint(0, 1), 4 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 6]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    recruit11 = [name1, "Guard", 4 + random.randint(0, 1), 4 + random.randint(0, 1), "Freshman", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 6]
    name1 = nameList[random.randint(0, len(nameList)-1)]
    if random.randint(0,1):
        recruit12 = [name1, "Guard", 4 + random.randint(0, 1), 4 + random.randint(0, 1), "Junior", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 3]
    elif random.randint(0,1):
        recruit12 = [name1, "Forward", 4 + random.randint(0, 1), 4 + random.randint(0, 1), "Junior", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 3]
    else:
        recruit12 = [name1, "Center", 4 + random.randint(0, 1), 4 + random.randint(0, 1), "Junior", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ROTATION, 0, 0, 0, 3]

    recruits = [recruit1, recruit2, recruit3, recruit4, recruit5, recruit6, recruit7, recruit8, recruit9, recruit10, recruit11, recruit12]

    # boost some recruit candidates scores
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

    recruitingTokens = 12
    print("*******************************************************")
    print("*")
    print("*\tRecruiting Time!\t\t{} Recruting Tokens Available".format(recruitingTokens))
    print("*")
    print("*******************************************************")
    index = 1
    for player in recruits:
        print("#{:2}\tName: {:10}\t\tPosition: {:10}\t\tOffense: {:2}\t\tDefense: {:2}\t\tAssits: {:2}\t\tBlocks: {:2}\t\tYear: {}\tTokens {}"
              "".format(index, player[NAME], player[POSITION], conODA(player[OFFENSEEST]), conODA(player[DEFENSEEST]),
                        conODA(player[ASSISTEST]), conBlock(player[BLOCKEST]), player[YEAR], player[RECRUITCOST]))
        index += 1

    selectedRecruits = []
    for i in range(0, 4):
        noInput = True
        while noInput == True:
            print("Select Recruit #{}\t or 99 to exit".format(i+1))
            numberValue = input()
            # if numberValue in "12345678":
            if numberValue.isdigit():
                number = int(numberValue)
                if (1 <= number <= 12) or (number == 99):
                    noInput = False

        # add token logic here
        if (number == 99) or (recruitingTokens <= 0):
            break
        elif (recruitingTokens >= recruits[number-1][RECRUITCOST]):
            recruitingTokens -= recruits[number-1][RECRUITCOST]
            selectedRecruits.append(list(recruits[number-1]))
            print("Selected: {}\t\tTokens Left {}".format(recruits[number-1][NAME], recruitingTokens))
        if (recruitingTokens <= 0):
            break

    # put all the team members (prior starters, prior bench, new recruits) into one list
    print("Here are the selected recruits:")
    for player in selectedRecruits:
        print("Name: {:10}  \tPosition: {}  \tOffense: {:2}  \tDefense: {:2}\tAssists: {:2}\tBlocks: {:2} \tYear: {}"
              "".format(player[NAME], player[POSITION], conODA(player[OFFENSEEST]), conODA(player[DEFENSEEST]),
                        conODA(player[ASSISTEST]), conBlock(player[BLOCKEST]), player[YEAR]))
        team.append(list(player))

    input("Type Enter to Continue")

    resultList = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    updateTeamOffDefStats(team, resultList)
    teamOffense, teamDefense, benchOffense, benchDefense,  = resultList[0], resultList[1], resultList[2], resultList[3]
    assistFactor = resultList[4]
    blockFactor = resultList[5]
    passingSummary, startingOffSummary, startingDefSummary, benchOffSummary, benchDefSummary, blockSummary = convertTeamStatsToText(assistFactor, teamOffense, teamDefense, benchOffense, benchDefense, blockFactor)

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
