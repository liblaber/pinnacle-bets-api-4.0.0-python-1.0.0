# This file was generated by liblab | https://liblab.com/

from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class TeaserBetLegBetType(Enum):
    """An enumeration representing different categories.

    :cvar SPREAD: "SPREAD"
    :vartype SPREAD: str
    :cvar TOTAL_POINTS: "TOTAL_POINTS"
    :vartype TOTAL_POINTS: str
    """

    SPREAD = "SPREAD"
    TOTAL_POINTS = "TOTAL_POINTS"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, TeaserBetLegBetType._member_map_.values()))


class TeaserBetLegSide(Enum):
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
        return list(map(lambda x: x.value, TeaserBetLegSide._member_map_.values()))


@JsonMap(
    {
        "leg_id": "legId",
        "bet_type": "betType",
        "line_id": "lineId",
        "event_id": "eventId",
    }
)
class TeaserBetLeg(BaseModel):
    """TeaserBetLeg

    :param leg_id: Client generated GUID for uniquely identifying the leg., defaults to None
    :type leg_id: str, optional
    :param bet_type: Leg bet type can be SPREAD or TOTAL_POINTS , defaults to None
    :type bet_type: TeaserBetLegBetType, optional
    :param line_id: Unique identifier., defaults to None
    :type line_id: int, optional
    :param event_id: Unique identifier., defaults to None
    :type event_id: int, optional
    :param team: Team being bet on for a spread line., defaults to None
    :type team: str, optional
    :param side: Chosen side type. This is needed only for TOTAL_POINTS bet type., defaults to None
    :type side: TeaserBetLegSide, optional
    """

    def __init__(
        self,
        leg_id: str = None,
        bet_type: TeaserBetLegBetType = None,
        line_id: int = None,
        event_id: int = None,
        team: str = None,
        side: TeaserBetLegSide = None,
    ):
        if leg_id is not None:
            self.leg_id = leg_id
        if bet_type is not None:
            self.bet_type = self._enum_matching(
                bet_type, TeaserBetLegBetType.list(), "bet_type"
            )
        if line_id is not None:
            self.line_id = line_id
        if event_id is not None:
            self.event_id = event_id
        if team is not None:
            self.team = team
        if side is not None:
            self.side = self._enum_matching(side, TeaserBetLegSide.list(), "side")
