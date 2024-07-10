# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .round_robin_option_with_odds import RoundRobinOptionWithOdds
from .parlay_leg_response import ParlayLegResponse


class PlaceParlayBetResponseStatus(Enum):
    """An enumeration representing different categories.

    :cvar ACCEPTED: "ACCEPTED"
    :vartype ACCEPTED: str
    :cvar PROCESSED_WITH_ERROR: "PROCESSED_WITH_ERROR"
    :vartype PROCESSED_WITH_ERROR: str
    """

    ACCEPTED = "ACCEPTED"
    PROCESSED_WITH_ERROR = "PROCESSED_WITH_ERROR"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, PlaceParlayBetResponseStatus._member_map_.values())
        )


class PlaceParlayBetResponseErrorCode(Enum):
    """An enumeration representing different categories.

    :cvar ABOVE_MAX_BET_AMOUNT: "ABOVE_MAX_BET_AMOUNT"
    :vartype ABOVE_MAX_BET_AMOUNT: str
    :cvar ALL_BETTING_CLOSED: "ALL_BETTING_CLOSED"
    :vartype ALL_BETTING_CLOSED: str
    :cvar BELOW_MIN_BET_AMOUNT: "BELOW_MIN_BET_AMOUNT"
    :vartype BELOW_MIN_BET_AMOUNT: str
    :cvar BLOCKED_BETTING: "BLOCKED_BETTING"
    :vartype BLOCKED_BETTING: str
    :cvar BLOCKED_CLIENT: "BLOCKED_CLIENT"
    :vartype BLOCKED_CLIENT: str
    :cvar INSUFFICIENT_FUNDS: "INSUFFICIENT_FUNDS"
    :vartype INSUFFICIENT_FUNDS: str
    :cvar INVALID_COUNTRY: "INVALID_COUNTRY"
    :vartype INVALID_COUNTRY: str
    :cvar INVALID_LEGS: "INVALID_LEGS"
    :vartype INVALID_LEGS: str
    :cvar INVALID_ODDS_FORMAT: "INVALID_ODDS_FORMAT"
    :vartype INVALID_ODDS_FORMAT: str
    :cvar INVALID_ROUND_ROBIN_OPTIONS: "INVALID_ROUND_ROBIN_OPTIONS"
    :vartype INVALID_ROUND_ROBIN_OPTIONS: str
    :cvar ROUND_ROBIN_DISALLOWED: "ROUND_ROBIN_DISALLOWED"
    :vartype ROUND_ROBIN_DISALLOWED: str
    :cvar TOO_MANY_LEGS: "TOO_MANY_LEGS"
    :vartype TOO_MANY_LEGS: str
    :cvar TOO_FEW_LEGS: "TOO_FEW_LEGS"
    :vartype TOO_FEW_LEGS: str
    :cvar RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED: "RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED"
    :vartype RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED: str
    :cvar RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED: "RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED"
    :vartype RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED: str
    :cvar INVALID_REQUEST: "INVALID_REQUEST"
    :vartype INVALID_REQUEST: str
    :cvar DUPLICATED_REQUEST: "DUPLICATED_REQUEST"
    :vartype DUPLICATED_REQUEST: str
    :cvar SYSTEM_ERROR_3: "SYSTEM_ERROR_3"
    :vartype SYSTEM_ERROR_3: str
    """

    ABOVE_MAX_BET_AMOUNT = "ABOVE_MAX_BET_AMOUNT"
    ALL_BETTING_CLOSED = "ALL_BETTING_CLOSED"
    BELOW_MIN_BET_AMOUNT = "BELOW_MIN_BET_AMOUNT"
    BLOCKED_BETTING = "BLOCKED_BETTING"
    BLOCKED_CLIENT = "BLOCKED_CLIENT"
    INSUFFICIENT_FUNDS = "INSUFFICIENT_FUNDS"
    INVALID_COUNTRY = "INVALID_COUNTRY"
    INVALID_LEGS = "INVALID_LEGS"
    INVALID_ODDS_FORMAT = "INVALID_ODDS_FORMAT"
    INVALID_ROUND_ROBIN_OPTIONS = "INVALID_ROUND_ROBIN_OPTIONS"
    ROUND_ROBIN_DISALLOWED = "ROUND_ROBIN_DISALLOWED"
    TOO_MANY_LEGS = "TOO_MANY_LEGS"
    TOO_FEW_LEGS = "TOO_FEW_LEGS"
    RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED = "RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED"
    RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED = "RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED"
    INVALID_REQUEST = "INVALID_REQUEST"
    DUPLICATED_REQUEST = "DUPLICATED_REQUEST"
    SYSTEM_ERROR_3 = "SYSTEM_ERROR_3"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value, PlaceParlayBetResponseErrorCode._member_map_.values()
            )
        )


@JsonMap(
    {
        "error_code": "errorCode",
        "bet_id": "betId",
        "unique_request_id": "uniqueRequestId",
        "round_robin_option_with_odds": "roundRobinOptionWithOdds",
        "max_risk_stake": "maxRiskStake",
        "min_risk_stake": "minRiskStake",
        "valid_legs": "validLegs",
        "invalid_legs": "invalidLegs",
    }
)
class PlaceParlayBetResponse(BaseModel):
    """PlaceParlayBetResponse

    :param status: Status of the response., defaults to None
    :type status: PlaceParlayBetResponseStatus, optional
    :param error_code: When Status is PROCESSED_WITH_ERROR, provides a code indicating the specific problem. ABOVE_MAX_BET_AMOUNT = Stake is above allowed maximum amount,   ALL_BETTING_CLOSED = Betting is not allowed at this moment,   BELOW_MIN_BET_AMOUNT = Stake is below allowed minimum amount,   BLOCKED_BETTING = Betting is suspended for the client,    BLOCKED_CLIENT = Client is no longer active,   INSUFFICIENT_FUNDS = Bet is submitted by a client with insufficient funds,   INVALID_COUNTRY = Client country is not allowed for betting,   INVALID_LEGS = One or more legs are invalid,   INVALID_ODDS_FORMAT = If a bet was submitted with the odds format that is not allowed for the client,   INVALID_ROUND_ROBIN_OPTIONS = Round robin options are invalid (i.e. does not match with number of legs),   ROUND_ROBIN_DISALLOWED = Round robin is disallowed for one of the leagues,   TOO_MANY_LEGS = Maximum of 10 legs can be specified,   TOO_FEW_LEGS = At least 2 legs are required for Parlay,   RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED = Client has reached his total loss limit,   RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED = Client has reached his total risk limit,   INVALID_REQUEST = Request has invalid parameters,   DUPLICATED_REQUEST = Request with the same uniqueRequestId was already processed. Please set the new value if you still want the request to be processed,   SYSTEM_ERROR_3 = Unexpected error  , defaults to None
    :type error_code: PlaceParlayBetResponseErrorCode, optional
    :param bet_id: Id of a newly created bet., defaults to None
    :type bet_id: int, optional
    :param unique_request_id: Unique identifier provided in the request., defaults to None
    :type unique_request_id: str, optional
    :param round_robin_option_with_odds: Provides array with all acceptable Round Robin options with parlay odds for that option., defaults to None
    :type round_robin_option_with_odds: List[RoundRobinOptionWithOdds], optional
    :param max_risk_stake: Maximum stake amount, defaults to None
    :type max_risk_stake: float, optional
    :param min_risk_stake: Minimum stake amount, defaults to None
    :type min_risk_stake: float, optional
    :param valid_legs: Collection of valid legs (format described below). Can be empty if no valid legs found., defaults to None
    :type valid_legs: List[ParlayLegResponse], optional
    :param invalid_legs: The collection of legs that resulted in error (format described below). Can be empty if no invalid legs found., defaults to None
    :type invalid_legs: List[ParlayLegResponse], optional
    """

    def __init__(
        self,
        status: PlaceParlayBetResponseStatus = None,
        error_code: PlaceParlayBetResponseErrorCode = None,
        bet_id: int = None,
        unique_request_id: str = None,
        round_robin_option_with_odds: List[RoundRobinOptionWithOdds] = None,
        max_risk_stake: float = None,
        min_risk_stake: float = None,
        valid_legs: List[ParlayLegResponse] = None,
        invalid_legs: List[ParlayLegResponse] = None,
    ):
        if status is not None:
            self.status = self._enum_matching(
                status, PlaceParlayBetResponseStatus.list(), "status"
            )
        if error_code is not None:
            self.error_code = self._enum_matching(
                error_code, PlaceParlayBetResponseErrorCode.list(), "error_code"
            )
        if bet_id is not None:
            self.bet_id = bet_id
        if unique_request_id is not None:
            self.unique_request_id = unique_request_id
        if round_robin_option_with_odds is not None:
            self.round_robin_option_with_odds = self._define_list(
                round_robin_option_with_odds, RoundRobinOptionWithOdds
            )
        if max_risk_stake is not None:
            self.max_risk_stake = max_risk_stake
        if min_risk_stake is not None:
            self.min_risk_stake = min_risk_stake
        if valid_legs is not None:
            self.valid_legs = self._define_list(valid_legs, ParlayLegResponse)
        if invalid_legs is not None:
            self.invalid_legs = self._define_list(invalid_legs, ParlayLegResponse)