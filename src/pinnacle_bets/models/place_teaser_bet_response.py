# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .place_teaser_bet_leg_response import PlaceTeaserBetLegResponse


class PlaceTeaserBetResponseErrorCode(Enum):
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
    :cvar DOUBLE_HIT: "DOUBLE_HIT"
    :vartype DOUBLE_HIT: str
    :cvar DUPLICATE_CLIENT_REFERENCE_ID: "DUPLICATE_CLIENT_REFERENCE_ID"
    :vartype DUPLICATE_CLIENT_REFERENCE_ID: str
    :cvar INCOMPLETE_CUSTOMER_BETTING_PROFILE: "INCOMPLETE_CUSTOMER_BETTING_PROFILE"
    :vartype INCOMPLETE_CUSTOMER_BETTING_PROFILE: str
    :cvar INSUFFICIENT_FUNDS: "INSUFFICIENT_FUNDS"
    :vartype INSUFFICIENT_FUNDS: str
    :cvar INVALID_COUNTRY: "INVALID_COUNTRY"
    :vartype INVALID_COUNTRY: str
    :cvar INVALID_CUSTOMER_PROFILE: "INVALID_CUSTOMER_PROFILE"
    :vartype INVALID_CUSTOMER_PROFILE: str
    :cvar INVALID_LEGS: "INVALID_LEGS"
    :vartype INVALID_LEGS: str
    :cvar INVALID_REQUEST: "INVALID_REQUEST"
    :vartype INVALID_REQUEST: str
    :cvar ODDS_FORMAT_MISMATCH: "ODDS_FORMAT_MISMATCH"
    :vartype ODDS_FORMAT_MISMATCH: str
    :cvar TEASER_DOES_NOT_EXIST: "TEASER_DOES_NOT_EXIST"
    :vartype TEASER_DOES_NOT_EXIST: str
    :cvar SAME_EVENT_ONLY_REQUIRED: "SAME_EVENT_ONLY_REQUIRED"
    :vartype SAME_EVENT_ONLY_REQUIRED: str
    :cvar SYSTEM_ERROR_1: "SYSTEM_ERROR_1"
    :vartype SYSTEM_ERROR_1: str
    :cvar SYSTEM_ERROR_2: "SYSTEM_ERROR_2"
    :vartype SYSTEM_ERROR_2: str
    :cvar SYSTEM_ERROR_3: "SYSTEM_ERROR_3"
    :vartype SYSTEM_ERROR_3: str
    :cvar TOO_FEW_LEGS: "TOO_FEW_LEGS"
    :vartype TOO_FEW_LEGS: str
    :cvar TOO_MANY_LEGS: "TOO_MANY_LEGS"
    :vartype TOO_MANY_LEGS: str
    :cvar DUPLICATED_REQUEST: "DUPLICATED_REQUEST"
    :vartype DUPLICATED_REQUEST: str
    :cvar RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED: "RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED"
    :vartype RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED: str
    :cvar RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED: "RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED"
    :vartype RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED: str
    """

    ABOVE_MAX_BET_AMOUNT = "ABOVE_MAX_BET_AMOUNT"
    ALL_BETTING_CLOSED = "ALL_BETTING_CLOSED"
    BELOW_MIN_BET_AMOUNT = "BELOW_MIN_BET_AMOUNT"
    BLOCKED_BETTING = "BLOCKED_BETTING"
    BLOCKED_CLIENT = "BLOCKED_CLIENT"
    DOUBLE_HIT = "DOUBLE_HIT"
    DUPLICATE_CLIENT_REFERENCE_ID = "DUPLICATE_CLIENT_REFERENCE_ID"
    INCOMPLETE_CUSTOMER_BETTING_PROFILE = "INCOMPLETE_CUSTOMER_BETTING_PROFILE"
    INSUFFICIENT_FUNDS = "INSUFFICIENT_FUNDS"
    INVALID_COUNTRY = "INVALID_COUNTRY"
    INVALID_CUSTOMER_PROFILE = "INVALID_CUSTOMER_PROFILE"
    INVALID_LEGS = "INVALID_LEGS"
    INVALID_REQUEST = "INVALID_REQUEST"
    ODDS_FORMAT_MISMATCH = "ODDS_FORMAT_MISMATCH"
    TEASER_DOES_NOT_EXIST = "TEASER_DOES_NOT_EXIST"
    SAME_EVENT_ONLY_REQUIRED = "SAME_EVENT_ONLY_REQUIRED"
    SYSTEM_ERROR_1 = "SYSTEM_ERROR_1"
    SYSTEM_ERROR_2 = "SYSTEM_ERROR_2"
    SYSTEM_ERROR_3 = "SYSTEM_ERROR_3"
    TOO_FEW_LEGS = "TOO_FEW_LEGS"
    TOO_MANY_LEGS = "TOO_MANY_LEGS"
    DUPLICATED_REQUEST = "DUPLICATED_REQUEST"
    RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED = "RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED"
    RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED = "RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value, PlaceTeaserBetResponseErrorCode._member_map_.values()
            )
        )


@JsonMap(
    {
        "error_code": "errorCode",
        "bet_id": "betId",
        "unique_request_id": "uniqueRequestId",
        "invalid_legs": "invalidLegs",
        "valid_legs": "validLegs",
    }
)
class PlaceTeaserBetResponse(BaseModel):
    """PlaceTeaserBetResponse

    :param status: Status of the request., defaults to None
    :type status: str, optional
    :param error_code: When Status is PROCESSED_WITH_ERROR, provides a code indicating the specific problem. ABOVE_MAX_BET_AMOUNT = Bet is above the maximum allowed,   ALL_BETTING_CLOSED = The wagering is disabled in the system (not related to a customer),   BELOW_MIN_BET_AMOUNT = Bet is below the minimum allowed,   BLOCKED_BETTING = Betting is suspended for the client,   BLOCKED_CLIENT = Customer is inactive in the system,   DOUBLE_HIT = The website submitted the same bet more than once,   DUPLICATE_CLIENT_REFERENCE_ID = The teaser unique id and/or one of the leg unique id are the same,   INCOMPLETE_CUSTOMER_BETTING_PROFILE = The customer does not exist,   INSUFFICIENT_FUNDS = The risk amount is above the customerâ€™s available balance,   INVALID_COUNTRY = Current location is proscribed,   INVALID_CUSTOMER_PROFILE = Either the customer does not exist OR the customer business rules are not verified,   INVALID_LEGS = One or more legs are not verified,   INVALID_REQUEST = Teaser request is not valid,   ODDS_FORMAT_MISMATCH = Agent customerâ€™s odds format differs from wager request odds format, TEASER_DOES_NOT_EXIST = Teaser does not exist in the system,   SAME_EVENT_ONLY_REQUIRED = Legs required to be for the same game only. Specified in the Teaser Specifications,   SYSTEM_ERROR_1 = System error,   SYSTEM_ERROR_2 = System error,   SYSTEM_ERROR_3 = System error,   TOO_FEW_LEGS = Legs count is below Min Picks specified in the Teaser Specifications,   TOO_MANY_LEGS = Legs count is above Max Picks specified in the Teaser Specifications, DUPLICATED_REQUEST = Request with the same uniqueRequestId was already processed. Please set the new value if you still want the request to be processed,   RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED = Client has reached his total loss limit,   RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED = Client has reached his total risk limit , defaults to None
    :type error_code: PlaceTeaserBetResponseErrorCode, optional
    :param bet_id: Id of a newly created bet., defaults to None
    :type bet_id: int, optional
    :param unique_request_id: Unique identifier provided in the request., defaults to None
    :type unique_request_id: str, optional
    :param price: Price for the bet., defaults to None
    :type price: float, optional
    :param risk: Amount wagered., defaults to None
    :type risk: float, optional
    :param win: Potential winnings., defaults to None
    :type win: float, optional
    :param invalid_legs: A collection of invalid legs, if any., defaults to None
    :type invalid_legs: List[PlaceTeaserBetLegResponse], optional
    :param valid_legs: A collection of valid legs, if any., defaults to None
    :type valid_legs: List[PlaceTeaserBetLegResponse], optional
    """

    def __init__(
        self,
        status: str = None,
        error_code: PlaceTeaserBetResponseErrorCode = None,
        bet_id: int = None,
        unique_request_id: str = None,
        price: float = None,
        risk: float = None,
        win: float = None,
        invalid_legs: List[PlaceTeaserBetLegResponse] = None,
        valid_legs: List[PlaceTeaserBetLegResponse] = None,
    ):
        if status is not None:
            self.status = status
        if error_code is not None:
            self.error_code = self._enum_matching(
                error_code, PlaceTeaserBetResponseErrorCode.list(), "error_code"
            )
        if bet_id is not None:
            self.bet_id = bet_id
        if unique_request_id is not None:
            self.unique_request_id = unique_request_id
        if price is not None:
            self.price = price
        if risk is not None:
            self.risk = risk
        if win is not None:
            self.win = win
        if invalid_legs is not None:
            self.invalid_legs = self._define_list(
                invalid_legs, PlaceTeaserBetLegResponse
            )
        if valid_legs is not None:
            self.valid_legs = self._define_list(valid_legs, PlaceTeaserBetLegResponse)
