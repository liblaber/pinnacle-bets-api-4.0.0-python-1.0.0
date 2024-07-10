# TeaserBet

**Properties**

| Name                | Type               | Required | Description                                                                                                                                                                                                                                                                                     |
| :------------------ | :----------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bet_id              | int                | ✅       | Bet identification                                                                                                                                                                                                                                                                              |
| wager_number        | int                | ✅       | Wager identification. All bets placed thru the API will have value 1. Website Classic view supports multiple contest(special) bets placement in the same bet slip in that case the bet would have appropriate wager number, as well as all round robin parlay bets.                             |
| placed_at           | str                | ✅       | Date time when the bet was placed.                                                                                                                                                                                                                                                              |
| bet_status          | TeaserBetBetStatus | ✅       | Bet Status. ACCEPTED = Bet was accepted, CANCELLED = Bet is cancelled as per Pinnacle betting rules, LOSE = The bet is settled as lose, REFUNDED = When an event is cancelled or when the bet is settled as push, the bet will have REFUNDED status, WON = The bet is settled as won            |
| bet_type            | str                | ✅       |                                                                                                                                                                                                                                                                                                 |
| win                 | float              | ✅       | Win amount.                                                                                                                                                                                                                                                                                     |
| risk                | float              | ✅       | Risk amount.                                                                                                                                                                                                                                                                                    |
| odds_format         | OddsFormat         | ✅       | Bet odds format. AMERICAN = American odds format, DECIMAL = Decimal (European) odds format, HONGKONG = Hong Kong odds format, INDONESIAN = Indonesian odds format, MALAY = Malaysian odds format                                                                                                |
| update_sequence     | int                | ✅       | Update Sequence                                                                                                                                                                                                                                                                                 |
| teaser_name         | str                | ✅       |                                                                                                                                                                                                                                                                                                 |
| is_same_event_only  | bool               | ✅       |                                                                                                                                                                                                                                                                                                 |
| min_picks           | float              | ✅       |                                                                                                                                                                                                                                                                                                 |
| max_picks           | float              | ✅       |                                                                                                                                                                                                                                                                                                 |
| legs                | List[TeaserLeg]    | ✅       |                                                                                                                                                                                                                                                                                                 |
| unique_request_id   | str                | ❌       | Unique Request Id                                                                                                                                                                                                                                                                               |
| win_loss            | float              | ❌       | Win-Loss for settled bets.                                                                                                                                                                                                                                                                      |
| customer_commission | float              | ❌       | Clientâ€™s commission on the bet.                                                                                                                                                                                                                                                              |
| cancellation_reason | CancellationReason | ❌       | Possible keys \: _ correctTeam1Id _ correctTeam2Id _ correctListedPitcher1 _ correctListedPitcher2 _ correctSpread _ correctTotalPoints _ correctTeam1TotalPoints _ correctTeam2TotalPoints _ correctTeam1Score _ correctTeam2Score _ correctTeam1TennisSetsScore _ correctTeam2TennisSetsScore |
| price               | float              | ❌       | Populated for all teaser bets and will be the original price at the time of the placement.                                                                                                                                                                                                      |
| final_price         | float              | ❌       | Only for settled parlay. Final price may differ in case leg was cancelled or half won.                                                                                                                                                                                                          |
| teaser_id           | float              | ❌       | Reference to the teaser id                                                                                                                                                                                                                                                                      |
| teaser_group_id     | float              | ❌       | Reference to the teaser group id                                                                                                                                                                                                                                                                |

# TeaserBetBetStatus

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
