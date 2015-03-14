import dicesimulator

starting_balance = 0.00010000
max_balance = starting_balance
balance = starting_balance
bet_amount = 0.00000100

# max target = 64225
less_then_target = 230

round_id = 0
while (balance - bet_amount > 0):
    round_id += 1

    # roll the dice
    dice = dicesimulator.roll()

    # substract bet amount
    balance -= bet_amount

    # receive payout
    balance += dicesimulator.payout(bet_amount, less_then_target, dice)

    # keep track of max balance
    if balance > max_balance:
        max_balance = balance

    # profit/loss made
    profit = dicesimulator.profit(bet_amount, less_then_target, dice)

    print "round={round} dice={dice:<5} bet={bet:.8f} profit={profit:+.8f} chance={win:.3f}% payout=x{payout:.5f} balance={balance:.8f}".format(
    round=round_id,
    dice=dice,
    target=less_then_target,
    profit=profit,
    bet=bet_amount,
    balance=balance,
    win=dicesimulator.probability(less_then_target),
    payout=dicesimulator.payout_multiplier(less_then_target)
    )


print "starting_balance={starting_balance:.8f} max_balance={max_balance:.8f}".format(starting_balance=starting_balance, max_balance=max_balance)