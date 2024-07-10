# PlaceBetsService

A list of all methods in the `PlaceBetsService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [bets_straight_v2](#bets_straight_v2) | Place straight bet (SPREAD, MONEYLINE, TOTAL_POINTS, TEAM_TOTAL_POINTS). Please note when the status is PENDING_ACCEPTANCE and if the live delay was applied, the response will not have betId. Client would have to call /bets by uniqueRequestId to check the status if the bet was ACCEPTED. For more details please see [How to place a bet on live events?](https://github.com/pinnacleapi/pinnacleapi-documentation/blob/master/FAQ.md#how-to-place-a-bet-on-live-events) Make sure you handle properly the case of an unexpected error as per [How to handle error on placing a bet?](https://github.com/pinnacleapi/pinnacleapi-documentation/blob/master/FAQ.md#how-to-handle-unexpected-error-on-placing-a-bet) |
| [bets_parlay_v2](#bets_parlay_v2)     | &nbsp;Make sure you handle properly the case of an unexpected error as per [How to handle error on placing a bet?](https://github.com/pinnacleapi/pinnacleapi-documentation/blob/master/FAQ.md#how-to-handle-unexpected-error-on-placing-a-bet)                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [bets_teaser](#bets_teaser)           | &nbsp;Make sure you handle properly the case of an unexpected error as per [How to handle error on placing a bet?](https://github.com/pinnacleapi/pinnacleapi-documentation/blob/master/FAQ.md#how-to-handle-unexpected-error-on-placing-a-bet)                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [bets_special](#bets_special)         | &nbsp;Make sure you handle properly the case of an unexpected error as per [How to handle error on placing a bet?](https://github.com/pinnacleapi/pinnacleapi-documentation/blob/master/FAQ.md#how-to-handle-unexpected-error-on-placing-a-bet)                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## bets_straight_v2

Place straight bet (SPREAD, MONEYLINE, TOTAL_POINTS, TEAM_TOTAL_POINTS). Please note when the status is PENDING_ACCEPTANCE and if the live delay was applied, the response will not have betId. Client would have to call /bets by uniqueRequestId to check the status if the bet was ACCEPTED. For more details please see [How to place a bet on live events?](https://github.com/pinnacleapi/pinnacleapi-documentation/blob/master/FAQ.md#how-to-place-a-bet-on-live-events) Make sure you handle properly the case of an unexpected error as per [How to handle error on placing a bet?](https://github.com/pinnacleapi/pinnacleapi-documentation/blob/master/FAQ.md#how-to-handle-unexpected-error-on-placing-a-bet)

- HTTP Method: `POST`
- Endpoint: `/v4/bets/straight`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [PlaceBetRequest](../models/PlaceBetRequest.md) | ✅       | The request body. |

**Return Type**

`PlaceStraightBetResponse`

**Example Usage Code Snippet**

```python
from pinnacle_bets import PinnacleBets, Environment
from pinnacle_bets.models import PlaceBetRequest

sdk = PinnacleBets(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

request_body = PlaceBetRequest(
    odds_format="AMERICAN",
    unique_request_id="d5cc50e4-284d-4d50-8d49-429bdc4f2a48",
    accept_better_line=True,
    stake=10.5,
    win_risk_stake="WIN",
    line_id=420921914,
    alt_line_id=8,
    fill_type="NORMAL",
    sport_id=29,
    event_id=757504261,
    period_number=2,
    bet_type="MONEYLINE",
    team="TEAM1",
    side="OVER"
)

result = sdk.place_bets.bets_straight_v2(request_body=request_body)

print(result)
```

## bets_parlay_v2

&nbsp;Make sure you handle properly the case of an unexpected error as per [How to handle error on placing a bet?](https://github.com/pinnacleapi/pinnacleapi-documentation/blob/master/FAQ.md#how-to-handle-unexpected-error-on-placing-a-bet)

- HTTP Method: `POST`
- Endpoint: `/v4/bets/parlay`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [PlaceParlayBetRequest](../models/PlaceParlayBetRequest.md) | ✅       | The request body. |

**Return Type**

`PlaceParlayBetResponse`

**Example Usage Code Snippet**

```python
from pinnacle_bets import PinnacleBets, Environment
from pinnacle_bets.models import PlaceParlayBetRequest

sdk = PinnacleBets(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

request_body = PlaceParlayBetRequest(
    unique_request_id="a9eb2eb1-13a5-4600-9f1b-4859379cdec4",
    accept_better_line=True,
    risk_amount=10.5,
    odds_format="AMERICAN",
    legs=[
        {
            "unique_leg_id": "CFAD8ACF-E410-437C-8F0F-33611F565981",
            "line_id": 419715968,
            "alt_line_id": 8,
            "sport_id": 29,
            "event_id": 758023991,
            "period_number": 2,
            "leg_bet_type": "MONEYLINE",
            "team": "TEAM1",
            "side": "OVER"
        }
    ],
    round_robin_options=[
        "Parlay"
    ]
)

result = sdk.place_bets.bets_parlay_v2(request_body=request_body)

print(result)
```

## bets_teaser

&nbsp;Make sure you handle properly the case of an unexpected error as per [How to handle error on placing a bet?](https://github.com/pinnacleapi/pinnacleapi-documentation/blob/master/FAQ.md#how-to-handle-unexpected-error-on-placing-a-bet)

- HTTP Method: `POST`
- Endpoint: `/v4/bets/teaser`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [PlaceTeaserBetRequest](../models/PlaceTeaserBetRequest.md) | ✅       | The request body. |

**Return Type**

`PlaceTeaserBetResponse`

**Example Usage Code Snippet**

```python
from pinnacle_bets import PinnacleBets, Environment
from pinnacle_bets.models import PlaceTeaserBetRequest

sdk = PinnacleBets(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

request_body = PlaceTeaserBetRequest(
    unique_request_id="10924e23-a2fe-4317-bffd-80504675f554",
    teaser_id=1,
    odds_format="AMERICAN",
    win_risk_stake="winRiskStake",
    stake=2.37,
    legs=[
        {
            "leg_id": "10924E23-A2FE-4317-BFFD-80504675F554",
            "bet_type": "SPREAD",
            "line_id": 8,
            "event_id": 1,
            "team": "team",
            "side": "OVER"
        }
    ]
)

result = sdk.place_bets.bets_teaser(request_body=request_body)

print(result)
```

## bets_special

&nbsp;Make sure you handle properly the case of an unexpected error as per [How to handle error on placing a bet?](https://github.com/pinnacleapi/pinnacleapi-documentation/blob/master/FAQ.md#how-to-handle-unexpected-error-on-placing-a-bet)

- HTTP Method: `POST`
- Endpoint: `/v4/bets/special`

**Parameters**

| Name         | Type                                                                              | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [MultiBetRequestSpecialBetRequest](../models/MultiBetRequestSpecialBetRequest.md) | ✅       | The request body. |

**Return Type**

`MultiBetResponseSpecialBetResponse`

**Example Usage Code Snippet**

```python
from pinnacle_bets import PinnacleBets, Environment
from pinnacle_bets.models import MultiBetRequestSpecialBetRequest

sdk = PinnacleBets(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value
)

request_body = MultiBetRequestSpecialBetRequest(
    bets=[
        {
            "unique_request_id": "10924e23-a2fe-4317-bffd-80504675f554",
            "accept_better_line": True,
            "odds_format": "AMERICAN",
            "stake": 10.5,
            "win_risk_stake": "WIN",
            "line_id": 51024304,
            "special_id": 726394409,
            "contestant_id": 726394411
        }
    ]
)

result = sdk.place_bets.bets_special(request_body=request_body)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
