# This file was generated by liblab | https://liblab.com/

from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class ParlayLegRequestLegBetType(Enum):
    """An enumeration representing different categories.

    :cvar MONEYLINE: "MONEYLINE"
    :vartype MONEYLINE: str
    :cvar SPREAD: "SPREAD"
    :vartype SPREAD: str
    :cvar TOTAL_POINTS: "TOTAL_POINTS"
    :vartype TOTAL_POINTS: str
    """

    MONEYLINE = "MONEYLINE"
    SPREAD = "SPREAD"
    TOTAL_POINTS = "TOTAL_POINTS"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, ParlayLegRequestLegBetType._member_map_.values())
        )


class ParlayLegRequestSide(Enum):
    """An enumeration representing different categories.

    :cvar OVER: "OVER"
    :vartype OVER: str
    :cvar UNDER: "UNDER"
    :vartype UNDER: str
    """

    OVER = "OVER"
    UNDER = "UNDER"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ParlayLegRequestSide._member_map_.values()))


@JsonMap(
    {
        "unique_leg_id": "uniqueLegId",
        "line_id": "lineId",
        "alt_line_id": "altLineId",
        "sport_id": "sportId",
        "event_id": "eventId",
        "period_number": "periodNumber",
        "leg_bet_type": "legBetType",
    }
)
class ParlayLegRequest(BaseModel):
    """ParlayLegRequest

    :param unique_leg_id: Unique id of the leg. It's used to identify and match legs in the response., defaults to None
    :type unique_leg_id: str, optional
    :param line_id: Line identification., defaults to None
    :type line_id: int, optional
    :param alt_line_id: Alternate line identification., defaults to None
    :type alt_line_id: int, optional
    :param sport_id: Sport identification., defaults to None
    :type sport_id: int, optional
    :param event_id: Event identification., defaults to None
    :type event_id: int, optional
    :param period_number: This represents the period of the match. For example, for soccer we have: 0 -  Game, 1 - 1st Half and 2 - 2nd Half, defaults to None
    :type period_number: int, optional
    :param leg_bet_type: Only SPREAD, MONEYLINE and TOTAL_POINTS are supported., defaults to None
    :type leg_bet_type: ParlayLegRequestLegBetType, optional
    :param team: Chosen team type. This is needed only for SPREAD and MONEYLINE bet types., defaults to None
    :type team: str, optional
    :param side: Chosen side type. This is needed only for TOTAL_POINTS bet type., defaults to None
    :type side: ParlayLegRequestSide, optional
    """

    def __init__(
        self,
        unique_leg_id: str = None,
        line_id: int = None,
        alt_line_id: int = None,
        sport_id: int = None,
        event_id: int = None,
        period_number: int = None,
        leg_bet_type: ParlayLegRequestLegBetType = None,
        team: str = None,
        side: ParlayLegRequestSide = None,
    ):
        if unique_leg_id is not None:
            self.unique_leg_id = unique_leg_id
        if line_id is not None:
            self.line_id = line_id
        if alt_line_id is not None:
            self.alt_line_id = alt_line_id
        if sport_id is not None:
            self.sport_id = sport_id
        if event_id is not None:
            self.event_id = event_id
        if period_number is not None:
            self.period_number = period_number
        if leg_bet_type is not None:
            self.leg_bet_type = self._enum_matching(
                leg_bet_type, ParlayLegRequestLegBetType.list(), "leg_bet_type"
            )
        if team is not None:
            self.team = team
        if side is not None:
            self.side = self._enum_matching(side, ParlayLegRequestSide.list(), "side")