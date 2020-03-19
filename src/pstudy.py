import random

class Die:
    def __init__(self, sides):
        self.sides = sides
    
    def roll(self):
        return(random.randint(1, self.sides))

while True:
    # Initialize dice
    dice = []
    n_dice = int(input('How many dice:'))
    total_sides = 0
    for i in range(n_dice):
        dice.append(Die(6))
        total_sides += dice[i].sides
    total_results = [0] * total_sides

    n_rolls = int(input('How many rolls:'))
    if n_rolls == 'quit':
        break
        
    for i in range(n_rolls):
        # Reset sequence and results for each roll
        roll_sequence = ''
        roll_results = [0] * n_dice
        for d in range(n_dice):
            # Roll each die.
            roll_results[d] = dice[d].roll()
            # Capture the sequence of rolls and results for printing.
            if d > 0:
                roll_sequence += '+'
            roll_sequence += str(roll_results[d])
            
        # Capture the total results for the probability.
        # -1 b/c dice are not zero-indexed...
        sum_roll = sum(roll_results)
        total_results[sum_roll - 1] += 1
            
        roll_sequence = roll_sequence + '=' + str(sum_roll)
        #print(roll_sequence)
        
    total_score = sum(total_results)
    for result in range(n_dice - 1, len(total_results)):
        ratio_result = 100 * (total_results[result] / total_score)
        ratio_result_str = "{0:.2f}".format(ratio_result)
        output_line = str(result + 1) + ': ' + str(total_results[result])
        output_line = output_line + ' (' + ratio_result_str + '%)'
        print(output_line)