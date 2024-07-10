# ParlayLeg

**Properties**

| Name                | Type                  | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :------------------ | :-------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| sport_id            | int                   | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| leg_bet_type        | ParlayLegLegBetType   | ❌       | Parlay leg type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| leg_bet_status      | ParlayLegLegBetStatus | ❌       | Parlay Leg status. CANCELLED = The leg is canceled- the stake on this leg will be transferred to the next one. In this case the leg will be ignored when calculating the winLoss. LOST = The leg is a loss or a push-lose. When Push-lose happens, the half of the stake on the leg will be pushed to the next leg, and the other half will be a lose. This can happen only when the leg is placed on a quarter points handicap. PUSHED = The leg is a push - the stake on this leg will be transferred to the next one. In this case the leg will be ignored when calculating the winLoss. REFUNDED = The leg is refunded - the stake on this leg will be transferred to the next one. In this case the leg will be ignored when calculating the winLoss. WON = The leg is a won or a push-won. When Push-won happens, the half of the stake on the leg will be pushed to the next leg, and the other half is won. This can happen only when the leg is placed on a quarter points handicap. HALF_WON_HALF_PUSHED = The bet is settled as half won half pushed. Only for asian handicap legs. HALF_LOST_HALF_PUSHED = The bet is settled as half lost half pushed. Only for asian handicap legs. |
| league_id           | int                   | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| event_id            | int                   | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| event_start_time    | str                   | ❌       | Date time when the event starts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| handicap            | float                 | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| price               | float                 | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| team_name           | str                   | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| side                | ParlayLegSide         | ❌       | Side type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| team1               | str                   | ❌       | Wellington Phoenix                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| team2               | str                   | ❌       | Adelaide United                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| period_number       | int                   | ❌       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ft_team1_score      | float                 | ❌       | Full time team 1 score                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ft_team2_score      | float                 | ❌       | Full time team 2 score                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| p_team1_score       | float                 | ❌       | End of period team 1 score. If the bet was placed on Game period (periodNumber =0) , this will be null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| p_team2_score       | float                 | ❌       | End of period team 2 score. If the bet was placed on Game period (periodNumber =0) , this will be null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| cancellation_reason | CancellationReason    | ❌       | Possible keys \: _ correctTeam1Id _ correctTeam2Id _ correctListedPitcher1 _ correctListedPitcher2 _ correctSpread _ correctTotalPoints _ correctTeam1TotalPoints _ correctTeam2TotalPoints _ correctTeam1Score _ correctTeam2Score _ correctTeam1TennisSetsScore _ correctTeam2TennisSetsScore                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

# ParlayLegLegBetType

Parlay leg type.

**Properties**

| Name         | Type | Required | Description    |
| :----------- | :--- | :------- | :------------- |
| MONEYLINE    | str  | ✅       | "MONEYLINE"    |
| SPREAD       | str  | ✅       | "SPREAD"       |
| TOTAL_POINTS | str  | ✅       | "TOTAL_POINTS" |

# ParlayLegLegBetStatus

Parlay Leg status.
CANCELLED = The leg is canceled- the stake on this leg will be transferred to the next one. In this case the leg will be ignored when calculating the winLoss.
LOST = The leg is a loss or a push-lose. When Push-lose happens, the half of the stake on the leg will be pushed to the next leg, and the other half will be a lose. This can happen only when the leg is placed on a quarter points handicap.  
PUSHED = The leg is a push - the stake on this leg will be transferred to the next one. In this case the leg will be ignored when calculating the winLoss.  
REFUNDED = The leg is refunded - the stake on this leg will be transferred to the next one. In this case the leg will be ignored when calculating the winLoss.  
WON = The leg is a won or a push-won. When Push-won happens, the half of the stake on the leg will be pushed to the next leg, and the other half is won. This can happen only when the leg is placed on a quarter points handicap.
HALF_WON_HALF_PUSHED = The bet is settled as half won half pushed. Only for asian handicap legs.
HALF_LOST_HALF_PUSHED = The bet is settled as half lost half pushed. Only for asian handicap legs.

**Properties**

| Name                  | Type | Required | Description             |
| :-------------------- | :--- | :------- | :---------------------- |
| CANCELLED             | str  | ✅       | "CANCELLED"             |
| LOST                  | str  | ✅       | "LOST"                  |
| PUSHED                | str  | ✅       | "PUSHED"                |
| REFUNDED              | str  | ✅       | "REFUNDED"              |
| WON                   | str  | ✅       | "WON"                   |
| ACCEPTED              | str  | ✅       | "ACCEPTED"              |
| HALF_WON_HALF_PUSHED  | str  | ✅       | "HALF_WON_HALF_PUSHED"  |
| HALF_LOST_HALF_PUSHED | str  | ✅       | "HALF_LOST_HALF_PUSHED" |

# ParlayLegSide

Side type.

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| OVER  | str  | ✅       | "OVER"      |
| UNDER | str  | ✅       | "UNDER"     |

<!-- This file was generated by liblab | https://liblab.com/ -->