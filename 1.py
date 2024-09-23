# My first commit file
'''Students would like to go on a school trip at the end of the year, but they
need money to pay for it. To raise money, they have organized a brunch. To
attend the brunch, a student in their first year pays $12, a student in their
second year pays $10, a student in their third year pays $7, and a student in
their fourth year pays $5.
Of all of the money raised at the brunch, 50 percent of it can be used to
pay for the school trip (the other 50 percent is used to pay for the brunch
itself).
We are told the cost of the school trip, the proportion of students in
each year, and the total number of students. Determine whether the students
need to raise more money for the school trip.
Input
The input consists of 10 test cases, with three lines per test case (30 lines in
all). Here are the three lines for each test case:
• The first line contains the cost in dollars of the school trip; it’s an
integer between 50 and 50,000.
• The second line contains four numbers indicating the proportion of
brunching students who are in first, second, third, and fourth year,
respectively. There is a space between each pair of numbers. Each
number is between 0 and 1, and their sum is 1 (for 100 percent).
• The third line contains integer n, the number of students attending
the brunch. n is between 4 and 2,000.
Output
For each test case: if the students need to raise more money for the school
trip, output YES; otherwise, output NO.'''
# schoolTripPrice = float(input('The cost in dollars of the school trip (Between 50$ - 50000$)'))
# proportions = input('Input four number separated with whitespace and indicating the proportion of the students are in first, second, third and fourth year.')
# studentsCount = int(input('How many students are the members of the school trip?'))
# proportionsList = []
# proportionsResult = []
# costsPerYear = [12, 10, 7, 5]
# everyonesCosts = []
#
# for i in proportions.split():
#     proportionsList.append(float(i))
# if sum(proportionsList) != 1:
#     print('The sum of every number should be equal to 1 (100%).')
# else:
#     pass
# print(proportionsList)
# for i in proportionsList:
#     proportionsResult.append(int(studentsCount * i))
# print(proportionsResult)
# for i in range(4):
#     everyonesCosts.append(costsPerYear[i] * proportionsResult[i])
# print(everyonesCosts)
# if sum(everyonesCosts) < schoolTripPrice:
#     print(sum(everyonesCosts))
#     print('YES')
# else:
#     print(sum(everyonesCosts))
#     print('NO')
# ======================================================================================================================
'''Two players, A and B, are playing a card game. (You don’t need to know
about playing cards or card games to understand this problem.)
The game starts with a deck of 52 cards. Player A takes a card from the
deck, then player B takes a card from the deck, then player A, then player B,
until there are no cards left in the deck.
There are 13 types of cards in the deck. These types are as follows: two,
three, four, five, six, seven, eight, nine, ten, jack, queen, king, ace.
There are four cards of each of these types in the deck. For example, there are four
twos, four threes, and so on, all the way up to four aces. (That’s why there
are 52 cards in the deck: 13 types times 4 cards per type.)
A high card is a card that is a jack, queen, king, or ace.
When a player takes a high card, they may score some points. Here are
the rules by which points are scored:
• If a player takes a jack, after which there is at least one card remaining
in the deck, and the next card in the deck is not a high card,
then the player scores 1 point.
• If a player takes a queen, after which there are at least two cards remaining
in the deck, and neither of the next two cards in the deck is
a high card, then the player scores 2 points.
• If a player takes a king, after which there are at least three cards remaining
in the deck, and none of the next three cards in the deck is
a high card, then the player scores 3 points.
• If a player takes an ace, after which there are at least four cards remaining
in the deck, and none of the next four cards in the deck is a
high card, then the player scores 4 points.
We’re asked to output information each time a player scores, as well as
the total score for each player at the end of the game.
Input
The input consists of 52 lines. Each line contains the type of a card in the
deck. The lines are in the order that cards will be taken from the deck; that
is, the first line is the first card taken from the deck, the second line is the
second card taken, and so on.
Output
Whenever a player scores, output the following line:
Player p scores q point(s).

We’ll be here all year if we go through a 52-card example, so let’s use
a smaller one with just 10 cards. This isn’t a complete test case, so the program
we write won’t work on it, but it’s enough for us to understand the mechanics
of the game and what our solution will have to do. Here’s the test
case:
queen
three
seven
king
nine
jack
eight
king
jack
four
Player A takes the first card, which is a queen. A queen is a high card,
and player A might score 2 points here. First, we confirm that there are
at least two cards remaining in the deck after this queen. Next, we have to
check these next two cards, hoping there is no high card among them. The
next two cards are not high cards—they are a three and a seven—so player A
gets 2 points.
Player B now takes the second card, which is a three. Three isn’t a high
card, so no points for player B.
Player A now takes the seven. No points.
Player B now takes the king, so there’s a chance for 3 points for player B.
There are at least three cards remaining in the deck after this king. We have
to check these next three cards, hoping there is no high card among them.
Sadly, there is a high card, a jack, among those three. No points for player B.
Player A now takes the nine. No points.
Player B now takes the first jack. There is at least one card remaining
in the deck after this jack. We have to check this next card, hoping it isn’t a
high card. Good news: it’s not a high card—it’s an eight—so player B gets 1
point.
There’s only one more point scored, and it’s by player A when they take
the second-last card (the jack) from the deck.
Therefore, this is the output for this test case:
Player A scores 2 point(s).
Player B scores 1 point(s).
Player A scores 1 point(s).
Player A: 3 point(s).
Player B: 1 point(s).
'''
# ======================================================================================================================
# from random import randint
# PlrA = []
# PlrB = []
# PlrAscore = 0
# PlrBscore = 0
# deck = [
#     ['1Two', '1Three', '1Four', '1Five', '1Six', '1Seven', '1Eight', '1Nine', '1Ten', '1Jack', '1Queen', '1King', '1Ace'],
#     ['2Two', '2Three', '2Four', '2Five', '2Six', '2Seven', '2Eight', '2Nine', '2Ten', '2Jack', '2Queen', '2King', '2Ace'],
#     ['3Two', '3Three', '3Four', '3Five', '3Six', '3Seven', '3Eight', '3Nine', '3Ten', '3Jack', '3Queen', '3King', '3Ace'],
#     ['4Two', '4Three', '4Four', '4Five', '4Six', '4Seven', '4Eight', '4Nine', '4Ten', '4Jack', '4Queen', '4King', '4Ace']
#         ]
# highCards = ['1Jack', '1Queen', '1King', '1Ace', '2Jack', '2Queen', '2King', '2Ace', '3Jack', '3Queen', '3King', '3Ace', '4Jack', '4Queen', '4King', '4Ace']
# while deck != []:
#     for _ in range(2):
#         i = randint(0, len(deck)-1)
#         j = randint(0, len(deck[i])-1)
#         PlrA.append(deck[i][j])
#         if deck[i][j] in highCards:
#             PlrAscore += 2
#         deck[i].remove(deck[i][j])
#         if deck[i] == []:
#             deck.remove([])
#     for _ in range(2):
#         i = randint(0, len(deck)-1)
#         j = randint(0, len(deck[i])-1)
#         PlrB.append(deck[i][j])
#         if deck[i][j] in highCards:
#             PlrBscore += 2
#         deck[i].remove(deck[i][j])
#         if deck[i] == []:
#             deck.remove([])
# print('Player A:', PlrA)
# print('Player B:', PlrB)
# print('The deck:', deck)
# print("Player A's score:", PlrAscore)
# print("Player B's score:", PlrBscore)
# ======================================================================================================================
'''Lena has n unopened boxes of action figures. The boxes cannot be opened
(otherwise the action figures lose their value), so the order of action figures
in a box cannot be changed. Further, a box cannot be rotated (otherwise the
action figures will be facing the wrong way).
Each action figure is specified by its height. For example, one of the
boxes might have three action figures, from left to right, of heights 4, 5, and
7.
When I talk about a box of action figures, I’ll always list the heights from
left to right.
Lena wants to organize the boxes, which means to arrange the boxes so
that heights of action figures increase or stay the same from left to right.
Whether she can organize the boxes or not depends on the heights of
action figures in the boxes.
For example, if a first box has action figures of
heights 4, 5, and 7, and a second box has action figures of heights 1 and 2,
then she can organize these boxes by putting the second box first. But if we
keep the first box as is and change the second box to have action figures of
heights 6 and 8, then there’s no way to organize these boxes.
Determine whether it’s possible for Lena to organize the boxes.
Input
The input consists of the following lines:
• A line containing integer n, the number of boxes. n is between 1
and 100.
• n lines, one for each box. Each of these lines begins with integer k,
indicating the number of action figures in this box. k is between 1
and 100. (Since k is at least 1, we don’t have to worry about empty
boxes.) Following k, there are k integers giving the heights of the action
figures from left to right in this box. Each height is an integer
between 1 and 10,000.
There is a space between each pair of integers on the line.
Output
If Lena can organize the boxes, output YES; otherwise, output NO.'''
# ================================================================== functions ==================================================================
# def denis():
#     y = 3 + 2
#     return 2 + 2
#
# print(denis())
# def denis(a, b):
'''
    return sum both of the prameters
    
    :param a: 
    :param b: 
    :return: 
    '''
# TODO: Read input
# TODO: Check whether all boxes are OK
# TODO: Obtain a new list of boxes with only left and right heights
# TODO: Sort boxes
# TODO: Determine whether boxes are organized

#     print(a + b)
#     # return a + b
# denis(input(), input())
# def denis(a, b):
#     print(a - b)
#
# denis(int(input('How many sealed boxes of action figures does Lena has? (1-100)')), int(input()))
# a = [2, 5]
# if a > b:
#     print('Hello')
# else:
#     print('Bye')
# if a[0][0] < a[1][0]:
#     tmp.append(a[0])
# else:
#     pass
# if a[1][0] < a[2][0]:
#     tmp.append(a[1])
# else:
#     pass
# if a[0][0] < a[2][0]:
#     tmp.append(a[0])
#     tmp.append(a[2])
# else:
#     tmp.append(a[2])
#     tmp.append(a[0])
# for l in range(len(a)-1):
#     for i in a:
#         if i[0] < a[l][0]:
#             tmp.append(i)
#
# print(tmp)

# a, b = [1,2,3],[3,2,1]
# print('a>b') if a>b else print('foo')

_sorted = []
b = int(input('Сколько коробок с фигирами в большой коробке?'))
for i in range(b):
    a = input('Какая высота у каждой фигуры?')
    a = a.split()
    a = [int(i) for i in a]
    a = sorted(a)
    _sorted.append(a)
    if _sorted[0] > _sorted[i]:
        _sorted.insert(0, i)
print(_sorted)


# numbers = [1, 2, 3, 4, 5]
# squares = [x**2 for x in numbers]
# print(squares)