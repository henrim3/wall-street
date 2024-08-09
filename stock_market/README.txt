I was having a problem with the player classes, right now I kept the player.py file and deleted
the player directory which fixed it for now. I think this counteracts the restructuring done? 
Will fix it tomorrow.

ALSO... allocating to buyout fund only subtracted an amount from capital and wasn't added anywhere....
each player now has a buyout_fund that just keeps track of total amount allocated

Total value of portfolio is now displayed, summation of stock share values, capital and buyout fund

Buying, Selling stocks, or Allocating to buyout fund will now give (up to ...) in input line, with ... being max 
amount of stocks or money to allocate