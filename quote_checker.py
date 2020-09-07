#  quote card class - enable you to create multiple quote cards
class QuoteCard:

    def __init__(self, cabinet, trench_road, trench_verge, chamber, pot):
        self.cabinet = cabinet
        self.trench_road = trench_road
        self.trench_verge = trench_verge
        self.chamber = chamber
        self.pot = pot

    def create_quote_card(self):
        quote_card = {'cabinet': self.cabinet, 'trench_road': self.trench_road, 'trench_verge': self.trench_verge,
                      'chamber': self.chamber, 'pot': self.pot}

        return quote_card


# function that captures the users input to gather network component requirements
def collect_details():
    # empty list - each user input will be appended to this list
    network_requirements = []

    cabinet = int(input('Please enter the number of cabinets you require: '))
    network_requirements.append(cabinet)

    trench_road = int(input('How many meters of road cabling do you require: '))
    network_requirements.append(trench_road)

    trench_verge = int(input('How many meter of verge cabling do you require: '))
    network_requirements.append(trench_verge)

    chamber = int(input('Please enter the number of chambers you require: '))
    network_requirements.append(chamber)

    pot = int(input('How many pots do you require: '))

    while True:

        x = input('Are the prices of your pots fixed or relative to your cabling? (f or r): ')

        if x == 'f' or x == 'F':
            network_requirements.append(pot)
            break
        elif x == 'r' or x == 'R':
            # empty list to contain the distances from each pot to cabinet
            pot_dist = 0

            for i in range(pot):
                pot_cab = int(input('How many meters of cabling do you require from the cabinet to your pot'+str(i+1)+': '))
                pot_dist = pot_dist + pot_cab

            network_requirements.append(pot_dist)
            break
        else:
            continue

    return network_requirements


def quote_calc(requirements, quote):
    # network_component list - contains the value of the total components * the price of each component
    n_c = []

    cab_q = requirements[0] * quote['cabinet']
    n_c.append(int(cab_q))

    t_road_q = requirements[1] * quote['trench_road']
    n_c.append(int(t_road_q))

    t_verge_q = requirements[2] * quote['trench_verge']
    n_c.append(int(t_verge_q))

    cham_q = requirements[3] * quote['chamber']
    n_c.append(int(cham_q))

    pot_q = requirements[4] * quote['pot']
    n_c.append(int(pot_q))

    print('Network break down cost - Cabinets: £{}, Trench_road: £{}, Trench_verge: £{}, chambers: £{}, pots: £{}'.format(
        n_c[0],
        n_c[1],
        n_c[2],
        n_c[3],
        n_c[4]))

    return n_c


def quote_sum(quote):
    total = 0

    for i in range(len(quote)):
        total = total + quote[i]

    return total


# MAIN SCRIPT


print('Welcome to your quote program')

print('generating quote card A....')
# create an instance of the quoteCard class - create quote card A
quote_card_A = QuoteCard(1000, 50, 100, 200, 100).create_quote_card()
print(quote_card_A)

print()

print('Please input your network requirements...')
# variable containing the users input for the network requirements
n_r_a = collect_details()

print()

print('generating quote card B...')
# create an instance of the quoteCard class - create quote card B
quote_card_B = QuoteCard(1200, 40, 80, 200, 20).create_quote_card()
print(quote_card_B)

print()

print('Please input your network requirements...')
# variable containing the users input for the network requirements
n_r_b = collect_details()

print()

print('Generating Quote A....')
#  variable containing the output from the quote calculation function - quote a
final_quoteA = quote_calc(n_r_a, quote_card_A)
# total amount variable - storing the total sum for quote A
tA = quote_sum(final_quoteA)
#  print out the total of quote B
print('Total: £' + str(tA))

print()

print('Generating Quote B....')
#  variable containing the output from the quote calculation function - quote b
final_quoteB = quote_calc(n_r_b, quote_card_B)
# total amount variable - storing the total sum for quote B
tB = quote_sum(final_quoteB)
#  print out the total of quote B
print('Total: £' + str(tB))