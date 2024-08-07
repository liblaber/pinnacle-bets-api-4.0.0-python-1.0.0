# This file was generated by liblab | https://liblab.com/

from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .cancellation_details_item import CancellationDetailsItem


@JsonMap({})
class CancellationReason(BaseModel):
    """Possible keys \:
    * correctTeam1Id
    * correctTeam2Id
    * correctListedPitcher1
    * correctListedPitcher2
    * correctSpread
    * correctTotalPoints
    * correctTeam1TotalPoints
    * correctTeam2TotalPoints
    * correctTeam1Score
    * correctTeam2Score
    * correctTeam1TennisSetsScore
    * correctTeam2TennisSetsScore


    :param code: code
    :type code: str
    :param details: details, defaults to None
    :type details: List[CancellationDetailsItem], optional
    """

    def __init__(self, code: str, details: List[CancellationDetailsItem] = None):
        self.code = code
        if details is not None:
            self.details = self._define_list(details, CancellationDetailsItem)
