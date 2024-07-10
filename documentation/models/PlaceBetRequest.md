# PlaceBetRequest

Request to place a bet.

**Properties**

| Name               | Type                        | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :----------------- | :-------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| odds_format        | OddsFormat                  | ❌       | Bet odds format. AMERICAN = American odds format, DECIMAL = Decimal (European) odds format, HONGKONG = Hong Kong odds format, INDONESIAN = Indonesian odds format, MALAY = Malaysian odds format                                                                                                                                                                                                                                              |
| unique_request_id  | str                         | ❌       | This is a Unique ID for PlaceBet requests. This is to support idempotent requests.                                                                                                                                                                                                                                                                                                                                                            |
| accept_better_line | bool                        | ❌       | Whether or not to accept a bet when there is a line change in favor of the client.                                                                                                                                                                                                                                                                                                                                                            |
| stake              | float                       | ❌       | amount in clientâ€™s currency.                                                                                                                                                                                                                                                                                                                                                                                                               |
| win_risk_stake     | PlaceBetRequestWinRiskStake | ❌       | Whether the stake amount is risk or win amount.                                                                                                                                                                                                                                                                                                                                                                                               |
| line_id            | int                         | ❌       | Line identification.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| alt_line_id        | int                         | ❌       | Alternate line identification.                                                                                                                                                                                                                                                                                                                                                                                                                |
| fill_type          | FillType                    | ❌       | NORMAL - bet will be placed on specified stake. FILLANDKILL - If the stake is over the max limit, bet will be placed on max limit, otherwise it will be placed on specified stake. FILLMAXLIMIT - bet will be places on max limit, stake amount will be ignored. Please note that maximum limits can change at any moment, which may result in risking more than anticipated. This option is replacement of isMaxStakeBet from v1/bets/place' |
| sport_id           | int                         | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| event_id           | int                         | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| period_number      | int                         | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| bet_type           | PlaceBetRequestBetType      | ❌       | Bet type.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| team               | Team                        | ❌       | Team type.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| side               | PlaceBetRequestSide         | ❌       | Side type.                                                                                                                                                                                                                                                                                                                                                                                                                                    |

# PlaceBetRequestWinRiskStake

Whether the stake amount is risk or win amount.

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| WIN  | str  | ✅       | "WIN"       |
| RISK | str  | ✅       | "RISK"      |

# FillType

NORMAL - bet will be placed on specified stake.  
FILLANDKILL - If the stake is over the max limit, bet will be placed on max limit, otherwise it will be placed on specified stake.  
FILLMAXLIMIT - bet will be places on max limit, stake amount will be ignored. Please note that maximum limits can change at any moment, which may result in risking more than anticipated. This option is replacement of isMaxStakeBet from v1/bets/place'

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| NORMAL       | str  | ✅       | "NORMAL"       |
| FILLANDKILL  | str  | ✅       | "FILLANDKILL"  |
| FILLMAXLIMIT | str  | ✅       | "FILLMAXLIMIT" |

# PlaceBetRequestBetType

Bet type.

**Properties**

| Name              | Type | Required | Description         |
| :---------------- | :--- | :------- | :------------------ |
| MONEYLINE         | str  | ✅       | "MONEYLINE"         |
| TEAM_TOTAL_POINTS | str  | ✅       | "TEAM_TOTAL_POINTS" |
| SPREAD            | str  | ✅       | "SPREAD"            |
| TOTAL_POINTS      | str  | ✅       | "TOTAL_POINTS"      |

# Team

Team type.

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| TEAM1 | str  | ✅       | "TEAM1"     |
| TEAM2 | str  | ✅       | "TEAM2"     |
| DRAW  | str  | ✅       | "DRAW"      |

# PlaceBetRequestSide

Side type.

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| OVER  | str  | ✅       | "OVER"      |
| UNDER | str  | ✅       | "UNDER"     |

<!-- This file was generated by liblab | https://liblab.com/ -->
