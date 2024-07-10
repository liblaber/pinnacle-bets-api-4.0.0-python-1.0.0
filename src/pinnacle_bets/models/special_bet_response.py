# This file was generated by liblab | https://liblab.com/

from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class SpecialBetResponseStatus(Enum):
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
            map(lambda x: x.value, SpecialBetResponseStatus._member_map_.values())
        )


class SpecialBetResponseErrorCode(Enum):
    """An enumeration representing different categories.

    :cvar ALL_BETTING_CLOSED: "ALL_BETTING_CLOSED"
    :vartype ALL_BETTING_CLOSED: str
    :cvar ABOVE_MAX_BET_AMOUNT: "ABOVE_MAX_BET_AMOUNT"
    :vartype ABOVE_MAX_BET_AMOUNT: str
    :cvar BELOW_MIN_BET_AMOUNT: "BELOW_MIN_BET_AMOUNT"
    :vartype BELOW_MIN_BET_AMOUNT: str
    :cvar BLOCKED_BETTING: "BLOCKED_BETTING"
    :vartype BLOCKED_BETTING: str
    :cvar BLOCKED_CLIENT: "BLOCKED_CLIENT"
    :vartype BLOCKED_CLIENT: str
    :cvar CONTEST_NOT_FOUND: "CONTEST_NOT_FOUND"
    :vartype CONTEST_NOT_FOUND: str
    :cvar DUPLICATED_REQUEST: "DUPLICATED_REQUEST"
    :vartype DUPLICATED_REQUEST: str
    :cvar INCOMPLETE_CUSTOMER_BETTING_PROFILE: "INCOMPLETE_CUSTOMER_BETTING_PROFILE"
    :vartype INCOMPLETE_CUSTOMER_BETTING_PROFILE: str
    :cvar INSUFFICIENT_FUNDS: "INSUFFICIENT_FUNDS"
    :vartype INSUFFICIENT_FUNDS: str
    :cvar INVALID_COUNTRY: "INVALID_COUNTRY"
    :vartype INVALID_COUNTRY: str
    :cvar INVALID_REQUEST: "INVALID_REQUEST"
    :vartype INVALID_REQUEST: str
    :cvar LINE_CHANGED: "LINE_CHANGED"
    :vartype LINE_CHANGED: str
    :cvar PAST_CUTOFFTIME: "PAST_CUTOFFTIME"
    :vartype PAST_CUTOFFTIME: str
    :cvar RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED: "RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED"
    :vartype RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED: str
    :cvar RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED: "RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED"
    :vartype RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED: str
    :cvar SYSTEM_ERROR_1: "SYSTEM_ERROR_1"
    :vartype SYSTEM_ERROR_1: str
    :cvar SYSTEM_ERROR_2: "SYSTEM_ERROR_2"
    :vartype SYSTEM_ERROR_2: str
    :cvar UNIQUE_REQUEST_ID_REQUIRED: "UNIQUE_REQUEST_ID_REQUIRED"
    :vartype UNIQUE_REQUEST_ID_REQUIRED: str
    :cvar INVALID_CUSTOMER_PROFILE: "INVALID_CUSTOMER_PROFILE"
    :vartype INVALID_CUSTOMER_PROFILE: str
    :cvar BETTING_SUSPENDED: "BETTING_SUSPENDED"
    :vartype BETTING_SUSPENDED: str
    """

    ALL_BETTING_CLOSED = "ALL_BETTING_CLOSED"
    ABOVE_MAX_BET_AMOUNT = "ABOVE_MAX_BET_AMOUNT"
    BELOW_MIN_BET_AMOUNT = "BELOW_MIN_BET_AMOUNT"
    BLOCKED_BETTING = "BLOCKED_BETTING"
    BLOCKED_CLIENT = "BLOCKED_CLIENT"
    CONTEST_NOT_FOUND = "CONTEST_NOT_FOUND"
    DUPLICATED_REQUEST = "DUPLICATED_REQUEST"
    INCOMPLETE_CUSTOMER_BETTING_PROFILE = "INCOMPLETE_CUSTOMER_BETTING_PROFILE"
    INSUFFICIENT_FUNDS = "INSUFFICIENT_FUNDS"
    INVALID_COUNTRY = "INVALID_COUNTRY"
    INVALID_REQUEST = "INVALID_REQUEST"
    LINE_CHANGED = "LINE_CHANGED"
    PAST_CUTOFFTIME = "PAST_CUTOFFTIME"
    RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED = "RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED"
    RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED = "RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED"
    SYSTEM_ERROR_1 = "SYSTEM_ERROR_1"
    SYSTEM_ERROR_2 = "SYSTEM_ERROR_2"
    UNIQUE_REQUEST_ID_REQUIRED = "UNIQUE_REQUEST_ID_REQUIRED"
    INVALID_CUSTOMER_PROFILE = "INVALID_CUSTOMER_PROFILE"
    BETTING_SUSPENDED = "BETTING_SUSPENDED"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, SpecialBetResponseErrorCode._member_map_.values())
        )


@JsonMap(
    {
        "error_code": "errorCode",
        "bet_id": "betId",
        "unique_request_id": "uniqueRequestId",
        "better_line_was_accepted": "betterLineWasAccepted",
    }
)
class SpecialBetResponse(BaseModel):
    """SpecialBetResponse

    :param status: Status of the request., defaults to None
    :type status: SpecialBetResponseStatus, optional
    :param error_code: When Status is PROCESSED_WITH_ERROR, provides a code indicating the specific problem. ALL_BETTING_CLOSED = Betting is not allowed at this moment. This may happen during system maintenance.    ABOVE_MAX_BET_AMOUNT = Stake is above allowed maximum amount,    BELOW_MIN_BET_AMOUNT = Stake is below allowed minimum amount,    BLOCKED_BETTING = Betting is suspended for the client,    BLOCKED_CLIENT = Client is no longer active,    CONTEST_NOT_FOUND = Incorrect contest id provided or contest is no longer available,    DUPLICATED_REQUEST = UniqueRequestId must be unique for each bet,    INCOMPLETE_CUSTOMER_BETTING_PROFILE = Customer profile could not be loaded,     INSUFFICIENT_FUNDS = Bet is submitted by a client with insufficient funds,    INVALID_COUNTRY = Client country is not allowed for betting,    INVALID_REQUEST = Special bet request is not valid,    LINE_CHANGED = Bet is submitted on a line that has changed,    PAST_CUTOFFTIME = Bet is submitted on a game after the betting cutoff time,    RESPONSIBLE_BETTING_LOSS_LIMIT_EXCEEDED = Self-imposed loss limit exceeded,    RESPONSIBLE_BETTING_RISK_LIMIT_EXCEEDED = Self-imposed risk limit exceeded,   SYSTEM_ERROR_1 = Unexpected error,    SYSTEM_ERROR_2 = Unexpected error,    UNIQUE_REQUEST_ID_REQUIRED = UniqueRequestId is missing,    INVALID_CUSTOMER_PROFILE = System configuration issue,  BETTING_SUSPENDED - Due to anomalous market circumstances bets are not currently being accepted on this line. Try again with next LineId. , defaults to None
    :type error_code: SpecialBetResponseErrorCode, optional
    :param bet_id: Bet identifier. Populated in case of accepted bet., defaults to None
    :type bet_id: int, optional
    :param unique_request_id: Unique identifier provided in the request., defaults to None
    :type unique_request_id: str, optional
    :param win: Win amount. Populated in case of accepted bet., defaults to None
    :type win: float, optional
    :param risk: Risk amount.  Populated in case of accepted bet., defaults to None
    :type risk: float, optional
    :param price: Bet price. Populated in case of accepted bet., defaults to None
    :type price: float, optional
    :param better_line_was_accepted: Whether or not the bet was accepted on the line that changed in favour of client. This can be true only if acceptBetterLine in the Place Bet request is set to TRUE., defaults to None
    :type better_line_was_accepted: bool, optional
    """

    def __init__(
        self,
        status: SpecialBetResponseStatus = None,
        error_code: SpecialBetResponseErrorCode = None,
        bet_id: int = None,
        unique_request_id: str = None,
        win: float = None,
        risk: float = None,
        price: float = None,
        better_line_was_accepted: bool = None,
    ):
        if status is not None:
            self.status = self._enum_matching(
                status, SpecialBetResponseStatus.list(), "status"
            )
        if error_code is not None:
            self.error_code = self._enum_matching(
                error_code, SpecialBetResponseErrorCode.list(), "error_code"
            )
        if bet_id is not None:
            self.bet_id = bet_id
        if unique_request_id is not None:
            self.unique_request_id = unique_request_id
        if win is not None:
            self.win = win
        if risk is not None:
            self.risk = risk
        if price is not None:
            self.price = price
        if better_line_was_accepted is not None:
            self.better_line_was_accepted = better_line_was_accepted
