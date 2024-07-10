# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel
from .odds_format import OddsFormat
from .cancellation_reason import CancellationReason


class StraightBetV4BetStatus(Enum):
    """An enumeration representing different categories.

    :cvar ACCEPTED: "ACCEPTED"
    :vartype ACCEPTED: str
    :cvar CANCELLED: "CANCELLED"
    :vartype CANCELLED: str
    :cvar LOST: "LOST"
    :vartype LOST: str
    :cvar PENDING_ACCEPTANCE: "PENDING_ACCEPTANCE"
    :vartype PENDING_ACCEPTANCE: str
    :cvar REFUNDED: "REFUNDED"
    :vartype REFUNDED: str
    :cvar PUSHED: "PUSHED"
    :vartype PUSHED: str
    :cvar NOT_ACCEPTED: "NOT_ACCEPTED"
    :vartype NOT_ACCEPTED: str
    :cvar WON: "WON"
    :vartype WON: str
    :cvar HALF_WON_HALF_PUSHED: "HALF_WON_HALF_PUSHED"
    :vartype HALF_WON_HALF_PUSHED: str
    :cvar HALF_LOST_HALF_PUSHED: "HALF_LOST_HALF_PUSHED"
    :vartype HALF_LOST_HALF_PUSHED: str
    """

    ACCEPTED = "ACCEPTED"
    CANCELLED = "CANCELLED"
    LOST = "LOST"
    PENDING_ACCEPTANCE = "PENDING_ACCEPTANCE"
    REFUNDED = "REFUNDED"
    PUSHED = "PUSHED"
    NOT_ACCEPTED = "NOT_ACCEPTED"
    WON = "WON"
    HALF_WON_HALF_PUSHED = "HALF_WON_HALF_PUSHED"
    HALF_LOST_HALF_PUSHED = "HALF_LOST_HALF_PUSHED"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, StraightBetV4BetStatus._member_map_.values())
        )


class StraightBetV4BetType(Enum):
    """An enumeration representing different categories.

    :cvar MONEYLINE: "MONEYLINE"
    :vartype MONEYLINE: str
    :cvar TEAM_TOTAL_POINTS: "TEAM_TOTAL_POINTS"
    :vartype TEAM_TOTAL_POINTS: str
    :cvar SPREAD: "SPREAD"
    :vartype SPREAD: str
    :cvar TOTAL_POINTS: "TOTAL_POINTS"
    :vartype TOTAL_POINTS: str
    :cvar SPECIAL: "SPECIAL"
    :vartype SPECIAL: str
    :cvar PARLAY: "PARLAY"
    :vartype PARLAY: str
    :cvar TEASER: "TEASER"
    :vartype TEASER: str
    :cvar MANUAL: "MANUAL"
    :vartype MANUAL: str
    """

    MONEYLINE = "MONEYLINE"
    TEAM_TOTAL_POINTS = "TEAM_TOTAL_POINTS"
    SPREAD = "SPREAD"
    TOTAL_POINTS = "TOTAL_POINTS"
    SPECIAL = "SPECIAL"
    PARLAY = "PARLAY"
    TEASER = "TEASER"
    MANUAL = "MANUAL"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, StraightBetV4BetType._member_map_.values()))


class StraightBetV4Side(Enum):
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
        return list(map(lambda x: x.value, StraightBetV4Side._member_map_.values()))


@JsonMap(
    {
        "bet_id": "betId",
        "wager_number": "wagerNumber",
        "placed_at": "placedAt",
        "bet_status": "betStatus",
        "bet_type": "betType",
        "win_loss": "winLoss",
        "odds_format": "oddsFormat",
        "customer_commission": "customerCommission",
        "cancellation_reason": "cancellationReason",
        "update_sequence": "updateSequence",
        "sport_id": "sportId",
        "league_id": "leagueId",
        "event_id": "eventId",
        "team_name": "teamName",
        "period_number": "periodNumber",
        "team1_score": "team1Score",
        "team2_score": "team2Score",
        "ft_team1_score": "ftTeam1Score",
        "ft_team2_score": "ftTeam2Score",
        "p_team1_score": "pTeam1Score",
        "p_team2_score": "pTeam2Score",
        "is_live": "isLive",
        "event_start_time": "eventStartTime",
    }
)
class StraightBetV4(BaseModel):
    """StraightBetV4

    :param bet_id: Bet identification
    :type bet_id: int
    :param wager_number: Wager identification. All bets placed thru the API will have value 1. Website Classic view supports multiple contest(special) bets placement in the same bet slip in that case the bet would have appropriate wager number, as well as all round robin parlay bets.
    :type wager_number: int
    :param placed_at: Date time when the bet was placed.
    :type placed_at: str
    :param bet_status: Bet Status.   ACCEPTED = Bet was accepted. PUSHED = Bet was pushed. CANCELLED = Bet is cancelled as per Pinnacle betting rules.   LOST = The bet is settled as lose.   PENDING_ACCEPTANCE = This status is reserved only for live bets. If a live bet is placed during danger zone or live delay is applied, it will be in PENDING_ACCEPTANCE , otherwise in ACCEPTED status. From this status bet can go to ACCEPTED or NOT_ACCEPTED status.   REFUNDED = When an event is cancelled or when the bet is settled as push, the bet will have REFUNDED status.   NOT_ACCEPTED = Bet was not accepted. Bet can be in this status only if it was previously in PENDING_ACCEPTANCE status.   WON = The bet is settled as won.   HALF_WON_HALF_PUSHED = The bet is settled as half won half pushed. Only for asian handicap bets.   HALF_LOST_HALF_PUSHED =  The bet is settled as half lost half pushed. Only for asian handicap bets.
    :type bet_status: StraightBetV4BetStatus
    :param bet_type: Bet type.
    :type bet_type: StraightBetV4BetType
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
    :param update_sequence: Update Sequence
    :type update_sequence: int
    :param sport_id: sport_id, defaults to None
    :type sport_id: int, optional
    :param league_id: league_id, defaults to None
    :type league_id: int, optional
    :param event_id: event_id, defaults to None
    :type event_id: int, optional
    :param handicap: handicap, defaults to None
    :type handicap: float, optional
    :param price: price, defaults to None
    :type price: float, optional
    :param team_name: team_name, defaults to None
    :type team_name: str, optional
    :param side: Side type., defaults to None
    :type side: StraightBetV4Side, optional
    :param team1: team1, defaults to None
    :type team1: str, optional
    :param team2: team2, defaults to None
    :type team2: str, optional
    :param period_number: period_number, defaults to None
    :type period_number: int, optional
    :param team1_score: Team 1 on the period that the bet was placed on at the moment of placing a bet, only for live bets., defaults to None
    :type team1_score: float, optional
    :param team2_score: Team 2 on the period that the bet was placed on at the moment of placing a bet, only for live bets., defaults to None
    :type team2_score: float, optional
    :param ft_team1_score: Full time team 1 score, only for settled bets., defaults to None
    :type ft_team1_score: float, optional
    :param ft_team2_score: Full time team 2 score, only for settled bets., defaults to None
    :type ft_team2_score: float, optional
    :param p_team1_score: .End of period team 1 score, only for settled bets. If the bet was placed on Game period (periodNumber =0), this will be null . , defaults to None
    :type p_team1_score: float, optional
    :param p_team2_score: End of period team 2 score, only for settled bets. If the bet was placed on Game period (periodNumber =0), this will be null, defaults to None
    :type p_team2_score: float, optional
    :param is_live: Whether the bet is on live event, defaults to None
    :type is_live: bool, optional
    :param event_start_time: Date time when the event starts., defaults to None
    :type event_start_time: str, optional
    """

    def __init__(
        self,
        bet_id: int,
        wager_number: int,
        placed_at: str,
        bet_status: StraightBetV4BetStatus,
        bet_type: StraightBetV4BetType,
        win: float,
        risk: float,
        odds_format: OddsFormat,
        update_sequence: int,
        win_loss: float = None,
        customer_commission: float = None,
        cancellation_reason: CancellationReason = None,
        sport_id: int = None,
        league_id: int = None,
        event_id: int = None,
        handicap: float = None,
        price: float = None,
        team_name: str = None,
        side: StraightBetV4Side = None,
        team1: str = None,
        team2: str = None,
        period_number: int = None,
        team1_score: float = None,
        team2_score: float = None,
        ft_team1_score: float = None,
        ft_team2_score: float = None,
        p_team1_score: float = None,
        p_team2_score: float = None,
        is_live: bool = None,
        event_start_time: str = None,
    ):
        self.bet_id = bet_id
        self.wager_number = wager_number
        self.placed_at = placed_at
        self.bet_status = self._enum_matching(
            bet_status, StraightBetV4BetStatus.list(), "bet_status"
        )
        self.bet_type = self._enum_matching(
            bet_type, StraightBetV4BetType.list(), "bet_type"
        )
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
        if sport_id is not None:
            self.sport_id = sport_id
        if league_id is not None:
            self.league_id = league_id
        if event_id is not None:
            self.event_id = event_id
        if handicap is not None:
            self.handicap = handicap
        if price is not None:
            self.price = price
        if team_name is not None:
            self.team_name = team_name
        if side is not None:
            self.side = self._enum_matching(side, StraightBetV4Side.list(), "side")
        if team1 is not None:
            self.team1 = team1
        if team2 is not None:
            self.team2 = team2
        if period_number is not None:
            self.period_number = period_number
        if team1_score is not None:
            self.team1_score = team1_score
        if team2_score is not None:
            self.team2_score = team2_score
        if ft_team1_score is not None:
            self.ft_team1_score = ft_team1_score
        if ft_team2_score is not None:
            self.ft_team2_score = ft_team2_score
        if p_team1_score is not None:
            self.p_team1_score = p_team1_score
        if p_team2_score is not None:
            self.p_team2_score = p_team2_score
        if is_live is not None:
            self.is_live = is_live
        if event_start_time is not None:
            self.event_start_time = event_start_time
