# Options glossary (Nifty, educational)

- **Call (CE):** right to buy at the strike price. Profits if the index rises above the strike.
- **Put (PE):** right to sell at the strike price. Profits if the index falls below the strike.
- **Premium:** price of the option. Buyers pay it; sellers receive it.
- **Lot size:** the number of units in one contract. Check the current NSE value, since it changes.
- **Expiry:** the date the contract ends. Nifty weekly options expire on a set weekday (check NSE rules).
- **Intrinsic value:** how far in-the-money the option is right now.
- **Implied volatility (IV):** the market's estimate of how much the index may move. Used in `probability.py`.
- **Iron condor:** sell an OTM put and an OTM call, and buy cheaper, further-OTM puts and calls as protection. Limited profit (the credit), limited loss (the spread width minus the credit). Profits if the index stays in the middle range.
- **Straddle / strangle:** buy or sell a call and a put together, at the same strike (straddle) or different strikes (strangle). Bets on a big move or on no big move.
- **Stop loss:** a preset level where you exit to cap the loss.
- **Position sizing:** how many lots you trade, based on how much of your capital you can afford to lose on that trade.

## Reminders
- Option sellers can lose much more than the premium received unless the position is hedged. Iron condors have defined loss only when the protective legs are actually held.
- Margin requirements change; check your broker's margin calculator before any trade.
- Same-day settlement and brokerage/charges reduce profit. Include them in your calculations.
