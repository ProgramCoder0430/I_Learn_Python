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

'''Does each box, on its own, have the action figures going from shortest to
tallest? Good question, and not one we know how to answer in just a line
or two of code. Let’s rely on a new function, all_boxes_ok, to tell us. If that
function returns False, then at least one box has its heights messed up, so
we won’t be able to organize the boxes. In that case, we should output NO. If
all_boxes_ok returns True, then we should carry out our remaining tasks to
determine whether the boxes can be organized'''
# =============================================================================================================================================
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

# bigBox = []
# boxes = int(input('Сколько коробок с фигурами в большой коробке?'))
# for i in range(boxes):
#     figures = input('Какая высота у каждой фигуры?')
#     figures = figures.split()
#     figures = [int(i) for i in figures]
#     bigBox.append(figures)
# print(bigBox)
# for boxes in bigBox:
#     for i in range(len(boxes)-1):
#         if boxes[i] == boxes[i+1]:
#             print('No')
#         elif boxes[i] < boxes[i+1]:
#             pass
#         else:
#             print('No')
# for i in range(len(bigBox)-1):
#     if bigBox[i][-1] > bigBox[i+1][0]:
#         print('No')

# def read_boxes(n):
#     '''n is the number of boxes to read.
#     Read the boxes from the input and return them as a list of boxes;
#     each boxes is the list of action figure height.'''
#     boxes = []
#     for i in range(n):  # Change the n number
#         box = input("What's the height of each figure? (Divide with space)").split()
#         box.pop(0)
#     for i in range(len(box)):
#         box[i] = int(box[i])
#         boxes.append(box)
#     return boxes
#
#
# def box_ok(box):
#     '''
#     'box' is the list of action figure height in a given box.
#     Return True if the height in box are in non-decricen order,
#     False otherwise.
#     '''
#     for i in range(len(box) - 1):
#         if box[i] < box[i + 1]:
#             return True
#         else:
#             return False
#
#
# def all_boxes_OK(boxes):
#     '''
#     'boxes' is a list of boxes, each box is the action figure's height.
#     Return True if each box in boxes has its action figures in non-decricen order height.
#     False otherwise.
#     '''
#     for box in boxes:
#         if not box_ok(box):
#             return False
#         else:
#             return True
#
#
# def boxes_endpoints(boxes):
#     '''
#     'boxes' is a list of boxes each box is a list of figure's height.
#     Return a list where each value is a list of two values:
#     The height of the leftmost and the rightmost action figure in a box.
#     '''
#     endpoints = []
#     for box in boxes:
#         endpoints.append([box[0], box[-1]])
#     return endpoints
#
#
# def all_endpoint_ok(endpoints):
#     '''
#     'endpoints' is a list where each list is a value of two values,
#      the height is the leftmost and rightmost action figures in a box.
#      Requires: 'endpoints' is sorted by action figure height.
#      Return 'True' if the 'endpoints' came from boxes that can be put in order.
#      False otherwise.
#     '''
#     maximum = endpoints[0][1]
#     for i in range(1, len(endpoints)):
#         if endpoints[i][0] < maximum:
#             return False
#         else:
#             return True
#
#
# # endpoints.sort()
#
# # ---Main Program---
# n = int(input('What is the box count?'))
# boxes = read_boxes(n)
# # Checks whether all boxes are OK
# if not all_boxes_OK(boxes):
#     print('No')
# else:
#     '''Obtain all lists of boxes with only left and right height.'''
#     endpoints = boxes_endpoints(boxes)
#
#     # Sort boxes
#     endpoints.sort()
#
#     # Determine whether the boxes oraganizible or not
#     if all_boxes_OK(endpoints):
#         print("Yes")
#     else:
#         print('No')

# ------------------  R E A D I N G A N D W R I T I N G F I L E S  ----------------------
'''
Bessie the cow is writing an essay. Each word in the essay contains only lowercase
or uppercase characters. Her teacher has specified the maximum
number of characters, not counting spaces, that can occur per line. To satisfy
this requirement, Bessie writes down the words of the essay using the
following rules:
• If the next word fits on the current line, add it to the current line.
Include a space between each pair of words on the line.
• Otherwise, put this word on a new line; this line becomes
Input
Read input from the file named word.in.
The input consists of two lines.
• The first line contains two integers separated by a space. The first
integer is n, the number of words in the essay; it’s between 1 and
100. The second integer is k, the maximum number of characters
(not counting spaces) that can occur per line; it’s between 1 and 80.
• The second line contains n words, with a space between each pair of
words. Each word has at most k characters.
Output
Write output to the file named word.out.
Output the properly formatted essay.
'''
