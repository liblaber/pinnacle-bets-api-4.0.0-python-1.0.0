# PlaceTeaserBetRequest

**Properties**

| Name              | Type               | Required | Description                                                                                                                                                                                      |
| :---------------- | :----------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| unique_request_id | str                | ❌       | Client generated GUID for uniquely identifying the bet.                                                                                                                                          |
| teaser_id         | int                | ❌       | Unique identifier. Teaser details can be retrieved from a call to Get Teaser Groups endpoint.                                                                                                    |
| odds_format       | OddsFormat         | ❌       | Bet odds format. AMERICAN = American odds format, DECIMAL = Decimal (European) odds format, HONGKONG = Hong Kong odds format, INDONESIAN = Indonesian odds format, MALAY = Malaysian odds format |
| win_risk_stake    | str                | ❌       | Whether the stake amount is risk or win amount.                                                                                                                                                  |
| stake             | float              | ❌       | amount in clientâ€™s currency.                                                                                                                                                                  |
| legs              | List[TeaserBetLeg] | ❌       | Collection of legs.                                                                                                                                                                              |

<!-- This file was generated by liblab | https://liblab.com/ -->