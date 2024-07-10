# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel
from .odds_format import OddsFormat
from .cancellation_reason import CancellationReason


class SpecialBetBetStatus(Enum):
    """An enumeration representing different categories.

    :cvar ACCEPTED: "ACCEPTED"
    :vartype ACCEPTED: str
    :cvar CANCELLED: "CANCELLED"
    :vartype CANCELLED: str
    :cvar LOSE: "LOSE"
    :vartype LOSE: str
    :cvar REFUNDED: "REFUNDED"
    :vartype REFUNDED: str
    :cvar WON: "WON"
    :vartype WON: str
    """

    ACCEPTED = "ACCEPTED"
    CANCELLED = "CANCELLED"
    LOSE = "LOSE"
    REFUNDED = "REFUNDED"
    WON = "WON"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, SpecialBetBetStatus._member_map_.values()))


@JsonMap(
    {
        "bet_id": "betId",
        "unique_request_id": "uniqueRequestId",
        "wager_number": "wagerNumber",
        "placed_at": "placedAt",
        "bet_status": "betStatus",
        "bet_type": "betType",
        "win_loss": "winLoss",
        "odds_format": "oddsFormat",
        "customer_commission": "customerCommission",
        "cancellation_reason": "cancellationReason",
        "update_sequence": "updateSequence",
        "special_id": "specialId",
        "special_name": "specialName",
        "contestant_id": "contestantId",
        "contestant_name": "contestantName",
        "sport_id": "sportId",
        "league_id": "leagueId",
        "event_id": "eventId",
        "period_number": "periodNumber",
        "event_start_time": "eventStartTime",
    }
)
class SpecialBet(BaseModel):
    """SpecialBet

    :param bet_id: Bet identification
    :type bet_id: int
    :param unique_request_id: Unique Request Id, defaults to None
    :type unique_request_id: str, optional
    :param wager_number: Wager identification. All bets placed thru the API will have value 1. Website Classic view supports multiple contest(special) bets placement in the same bet slip in that case the bet would have appropriate wager number, as well as all round robin parlay bets.
    :type wager_number: int
    :param placed_at: Date time when the bet was placed.
    :type placed_at: str
    :param bet_status: Bet Status.  ACCEPTED = Bet was accepted,  CANCELLED = Bet is cancelled as per Pinnacle betting rules,  LOSE = The bet is settled as lose, REFUNDED = When an event is cancelled or when the bet is settled as push, the bet will have REFUNDED status,  WON = The bet is settled as won  PUSHED = The bet is settled as a push.
    :type bet_status: SpecialBetBetStatus
    :param bet_type: bet_type
    :type bet_type: str
    :param win: Win amount.
    :type win: float
    :param risk: Risk amount.
    :type risk: float
    :param win_loss: Win-Loss for settled bets., defaults to None
    :type win_loss: float, optional
    :param odds_format: Bet odds format.   AMERICAN = American odds format,   DECIMAL = Decimal (European) odds format,   HONGKONG = Hong Kong odds format,   INDONESIAN = Indonesian odds format,   MALAY = Malaysian odds format
    :type odds_format: OddsFormat
    :param customer_commission: Clientâ€™s commission on the bet., defaults to None
    :type customer_commission: float, optional
    :param cancellation_reason: Possible keys \:   * correctTeam1Id * correctTeam2Id * correctListedPitcher1 * correctListedPitcher2 * correctSpread * correctTotalPoints * correctTeam1TotalPoints * correctTeam2TotalPoints * correctTeam1Score * correctTeam2Score * correctTeam1TennisSetsScore * correctTeam2TennisSetsScore , defaults to None
    :type cancellation_reason: CancellationReason, optional
    :param update_sequence: Update Sequence. It gets updated when the bet status change.
    :type update_sequence: int
    :param special_id: special_id
    :type special_id: int
    :param special_name: special_name
    :type special_name: str
    :param contestant_id: contestant_id
    :type contestant_id: int
    :param contestant_name: contestant_name
    :type contestant_name: str
    :param price: price
    :type price: float
    :param handicap: handicap, defaults to None
    :type handicap: float, optional
    :param units: units, defaults to None
    :type units: str, optional
    :param sport_id: sport_id
    :type sport_id: int
    :param league_id: league_id
    :type league_id: int
    :param event_id: Populated if bet was placed on a special linked to the event., defaults to None
    :type event_id: int, optional
    :param period_number: Populated if bet was placed on a special linked to the event., defaults to None
    :type period_number: int, optional
    :param team1: Populated if bet was placed on a special linked to the event., defaults to None
    :type team1: str, optional
    :param team2: Populated if bet was placed on a special linked to the event., defaults to None
    :type team2: str, optional
    :param event_start_time: Date time when the event starts, defaults to None
    :type event_start_time: str, optional
    """

    def __init__(
        self,
        bet_id: int,
        wager_number: int,
        placed_at: str,
        bet_status: SpecialBetBetStatus,
        bet_type: str,
        win: float,
        risk: float,
        odds_format: OddsFormat,
        update_sequence: int,
        special_id: int,
        special_name: str,
        contestant_id: int,
        contestant_name: str,
        price: float,
        sport_id: int,
        league_id: int,
        unique_request_id: str = None,
        win_loss: float = None,
        customer_commission: float = None,
        cancellation_reason: CancellationReason = None,
        handicap: float = None,
        units: str = None,
        event_id: int = None,
        period_number: int = None,
        team1: str = None,
        team2: str = None,
        event_start_time: str = None,
    ):
        self.bet_id = bet_id
        if unique_request_id is not None:
            self.unique_request_id = unique_request_id
        self.wager_number = wager_number
        self.placed_at = placed_at
        self.bet_status = self._enum_matching(
            bet_status, SpecialBetBetStatus.list(), "bet_status"
        )
        self.bet_type = bet_type
        self.win = win
        self.risk = risk
        if win_loss is not None:
            self.win_loss = win_loss
        self.odds_format = self._enum_matching(
            odds_format, OddsFormat.list(), "odds_format"
        )
        if customer_commission is not None:
            self.customer_commission = customer_commission
        if cancellation_reason is not None:
            self.cancellation_reason = self._define_object(
                cancellation_reason, CancellationReason
            )
        self.update_sequence = update_sequence
        self.special_id = special_id
        self.special_name = special_name
        self.contestant_id = contestant_id
        self.contestant_name = contestant_name
        self.price = price
        if handicap is not None:
            self.handicap = handicap
        if units is not None:
            self.units = units
        self.sport_id = sport_id
        self.league_id = league_id
        if event_id is not None:
            self.event_id = event_id
        if period_number is not None:
            self.period_number = period_number
        if team1 is not None:
            self.team1 = team1
        if team2 is not None:
            self.team2 = team2
        if event_start_time is not None:
            self.event_start_time = event_start_time