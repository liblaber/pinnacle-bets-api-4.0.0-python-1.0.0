# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .odds_format import OddsFormat
from .cancellation_reason import CancellationReason
from .parlay_leg import ParlayLeg


class ParlayBetBetStatus(Enum):
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
    :cvar NOT_ACCEPTED: "NOT_ACCEPTED"
    :vartype NOT_ACCEPTED: str
    :cvar WON: "WON"
    :vartype WON: str
    :cvar PARTIAL_WON: "PARTIAL_WON"
    :vartype PARTIAL_WON: str
    :cvar PARTIAL_LOST: "PARTIAL_LOST"
    :vartype PARTIAL_LOST: str
    """

    ACCEPTED = "ACCEPTED"
    CANCELLED = "CANCELLED"
    LOST = "LOST"
    PENDING_ACCEPTANCE = "PENDING_ACCEPTANCE"
    REFUNDED = "REFUNDED"
    NOT_ACCEPTED = "NOT_ACCEPTED"
    WON = "WON"
    PARTIAL_WON = "PARTIAL_WON"
    PARTIAL_LOST = "PARTIAL_LOST"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ParlayBetBetStatus._member_map_.values()))


@JsonMap(
    {
        "bet_id": "betId",
        "unique_request_id": "uniqueRequestId",
        "wager_number": "wagerNumber",
        "bet_status": "betStatus",
        "bet_type": "betType",
        "win_loss": "winLoss",
        "odds_format": "oddsFormat",
        "customer_commission": "customerCommission",
        "cancellation_reason": "cancellationReason",
        "update_sequence": "updateSequence",
        "final_price": "finalPrice",
    }
)
class ParlayBet(BaseModel):
    """ParlayBet

    :param bet_id: Bet identification
    :type bet_id: int
    :param unique_request_id: Unique Request Id, defaults to None
    :type unique_request_id: str, optional
    :param wager_number: Wager identification. All bets placed thru the API will have value 1. Website Classic view supports multiple contest(special) bets placement in the same bet slip in that case the bet would have appropriate wager number, as well as all round robin parlay bets.
    :type wager_number: int
    :param bet_status: Bet Status.  ACCEPTED = Bet was accepted.   CANCELLED = Bet is cancelled as per Pinnacle betting rules.   LOST = The bet is settled as lose.   PENDING_ACCEPTANCE = This status is reserved only for live bets. If a live bet is placed during danger zone or live delay is applied, it will be in PENDING_ACCEPTANCE , otherwise in ACCEPTED status. From this status bet can go to ACCEPTED or REJECTED status.   REFUNDED = When an event is cancelled or when the bet is settled as push, the bet will have REFUNDED status.   NOT_ACCEPTED = Bet was not accepted. Bet can be in this status only if it was previously in PENDING_ACCEPTANCE status.   WON = The bet is settled as won.   PARTIAL_WON  - If gross payout is greater than the  stake. Only for parlays with the asian handicap legs.   PARTIAL_LOST  - If gross payout is less or equal to the stake. Only for parlays with the asian handicap legs.
    :type bet_status: ParlayBetBetStatus
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
    :param update_sequence: Update Sequence
    :type update_sequence: int
    :param legs: legs
    :type legs: List[ParlayLeg]
    :param price: price, defaults to None
    :type price: float, optional
    :param final_price: Only for settled parlay. Final price may differ in case leg was cancelled or half won, defaults to None
    :type final_price: float, optional
    """

    def __init__(
        self,
        bet_id: int,
        wager_number: int,
        bet_status: ParlayBetBetStatus,
        bet_type: str,
        win: float,
        risk: float,
        odds_format: OddsFormat,
        update_sequence: int,
        legs: List[ParlayLeg],
        unique_request_id: str = None,
        win_loss: float = None,
        customer_commission: float = None,
        cancellation_reason: CancellationReason = None,
        price: float = None,
        final_price: float = None,
    ):
        self.bet_id = bet_id
        if unique_request_id is not None:
            self.unique_request_id = unique_request_id
        self.wager_number = wager_number
        self.bet_status = self._enum_matching(
            bet_status, ParlayBetBetStatus.list(), "bet_status"
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
        self.legs = self._define_list(legs, ParlayLeg)
        if price is not None:
            self.price = price
        if final_price is not None:
            self.final_price = final_price
