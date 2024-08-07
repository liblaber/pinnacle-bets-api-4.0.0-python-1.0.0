# This file was generated by liblab | https://liblab.com/

from pinnacle_bets import PinnacleBets, Environment
from pinnacle_bets.models import Betlist, SortDir

sdk = PinnacleBets(
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    base_url=Environment.DEFAULT.value,
)
bet_statuses = ["WON"]
betids = [9]
unique_request_ids = ["uniqueRequestIds"]
bet_type = ["SPREAD"]

result = sdk.get_bets.bets_get_bets_by_type_v4(
    betlist="SETTLED",
    bet_statuses=bet_statuses,
    from_date="fromDate",
    to_date="toDate",
    sort_dir="ASC",
    page_size=1000,
    from_record=9,
    betids=betids,
    unique_request_ids=unique_request_ids,
    bet_type=bet_type,
)

print(result)
