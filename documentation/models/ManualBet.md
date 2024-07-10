# ManualBet

**Properties**

| Name             | Type               | Required | Description                                                                                                                                                                                                                                                                          |
| :--------------- | :----------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bet_id           | int                | ✅       | Bet identification                                                                                                                                                                                                                                                                   |
| wager_number     | int                | ✅       | Wager identification. All bets placed thru the API will have value 1. Website Classic view supports multiple contest(special) bets placement in the same bet slip in that case the bet would have appropriate wager number, as well as all round robin parlay bets.                  |
| placed_at        | str                | ✅       | Date time when the bet was placed.                                                                                                                                                                                                                                                   |
| bet_status       | ManualBetBetStatus | ✅       | Bet Status. ACCEPTED = Bet was accepted, CANCELLED = Bet is cancelled as per Pinnacle betting rules, LOSE = The bet is settled as lose, REFUNDED = When an event is cancelled or when the bet is settled as push, the bet will have REFUNDED status, WON = The bet is settled as won |
| bet_type         | str                | ✅       |                                                                                                                                                                                                                                                                                      |
| win              | float              | ✅       | Win amount.                                                                                                                                                                                                                                                                          |
| risk             | float              | ✅       | Risk amount.                                                                                                                                                                                                                                                                         |
| update_sequence  | int                | ✅       | Update Sequence                                                                                                                                                                                                                                                                      |
| description      | str                | ✅       | Manual bet description.                                                                                                                                                                                                                                                              |
| win_loss         | float              | ❌       | Win-Loss for settled bets.                                                                                                                                                                                                                                                           |
| reference_bet_id | int                | ❌       | Referenced original bet id.                                                                                                                                                                                                                                                          |

# ManualBetBetStatus

Bet Status.

ACCEPTED = Bet was accepted,  
CANCELLED = Bet is cancelled as per Pinnacle betting rules,  
LOSE = The bet is settled as lose,  
REFUNDED = When an event is cancelled or when the bet is settled as push, the bet will have REFUNDED status,  
WON = The bet is settled as won

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| ACCEPTED  | str  | ✅       | "ACCEPTED"  |
| CANCELLED | str  | ✅       | "CANCELLED" |
| LOSE      | str  | ✅       | "LOSE"      |
| REFUNDED  | str  | ✅       | "REFUNDED"  |
| WON       | str  | ✅       | "WON"       |

<!-- This file was generated by liblab | https://liblab.com/ -->
