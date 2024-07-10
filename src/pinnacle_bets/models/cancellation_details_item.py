# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class CancellationDetailsItem(BaseModel):
    """CancellationDetailsItem

    :param key: key, defaults to None
    :type key: str, optional
    :param value: value, defaults to None
    :type value: str, optional
    """

    def __init__(self, key: str = None, value: str = None):
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
