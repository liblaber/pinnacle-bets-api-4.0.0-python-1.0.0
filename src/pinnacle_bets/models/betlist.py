# This file was generated by liblab | https://liblab.com/

from enum import Enum


class Betlist(Enum):
    """An enumeration representing different categories.

    :cvar SETTLED: "SETTLED"
    :vartype SETTLED: str
    :cvar RUNNING: "RUNNING"
    :vartype RUNNING: str
    :cvar ALL: "ALL"
    :vartype ALL: str
    """

    SETTLED = "SETTLED"
    RUNNING = "RUNNING"
    ALL = "ALL"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Betlist._member_map_.values()))