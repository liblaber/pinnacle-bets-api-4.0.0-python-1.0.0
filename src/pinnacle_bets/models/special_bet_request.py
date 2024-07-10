# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel
from .odds_format import OddsFormat


class SpecialBetRequestWinRiskStake(Enum):
    """An enumeration representing different categories.

    :cvar WIN: "WIN"
    :vartype WIN: str
    :cvar RISK: "RISK"
    :vartype RISK: str
    """

    WIN = "WIN"
    RISK = "RISK"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, SpecialBetRequestWinRiskStake._member_map_.values())
        )


@JsonMap(
    {
        "unique_request_id": "uniqueRequestId",
        "accept_better_line": "acceptBetterLine",
        "odds_format": "oddsFormat",
        "win_risk_stake": "winRiskStake",
        "line_id": "lineId",
        "special_id": "specialId",
        "contestant_id": "contestantId",
    }
)
class SpecialBetRequest(BaseModel):
    """SpecialBetRequest

    :param unique_request_id: This unique id of the place bet requests. This is to support idempotent requests., defaults to None
    :type unique_request_id: str, optional
    :param accept_better_line: Whether or not to accept a bet when there is a line change in favor of the client., defaults to None
    :type accept_better_line: bool, optional
    :param odds_format: Bet odds format.   AMERICAN = American odds format,   DECIMAL = Decimal (European) odds format,   HONGKONG = Hong Kong odds format,   INDONESIAN = Indonesian odds format,   MALAY = Malaysian odds format  , defaults to None
    :type odds_format: OddsFormat, optional
    :param stake: amount in clientâ€™s currency., defaults to None
    :type stake: float, optional
    :param win_risk_stake: Whether the stake amount is risk or win amount., defaults to None
    :type win_risk_stake: SpecialBetRequestWinRiskStake, optional
    :param line_id: Line identification., defaults to None
    :type line_id: int, optional
    :param special_id: Special identification., defaults to None
    :type special_id: int, optional
    :param contestant_id: Contestant identification., defaults to None
    :type contestant_id: int, optional
    """

    def __init__(
        self,
        unique_request_id: str = None,
        accept_better_line: bool = None,
        odds_format: OddsFormat = None,
        stake: float = None,
        win_risk_stake: SpecialBetRequestWinRiskStake = None,
        line_id: int = None,
        special_id: int = None,
        contestant_id: int = None,
    ):
        if unique_request_id is not None:
            self.unique_request_id = unique_request_id
        if accept_better_line is not None:
            self.accept_better_line = accept_better_line
        if odds_format is not None:
            self.odds_format = self._enum_matching(
                odds_format, OddsFormat.list(), "odds_format"
            )
        if stake is not None:
            self.stake = stake
        if win_risk_stake is not None:
            self.win_risk_stake = self._enum_matching(
                win_risk_stake, SpecialBetRequestWinRiskStake.list(), "win_risk_stake"
            )
        if line_id is not None:
            self.line_id = line_id
        if special_id is not None:
            self.special_id = special_id
        if contestant_id is not None:
            self.contestant_id = contestant_id