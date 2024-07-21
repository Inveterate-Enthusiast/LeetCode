# Table: FriendRequest
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | sender_id      | int     |
# | send_to_id     | int     |
# | request_date   | date    |
# +----------------+---------+
# This table may contain duplicates (In other words, there is no primary key for this table in SQL).
# This table contains the ID of the user who sent the request, the ID of the user who received the request,
# and the date of the request.
#
# Table: RequestAccepted
#
# +----------------+---------+
# | Column Name    | Type    |
# +----------------+---------+
# | requester_id   | int     |
# | accepter_id    | int     |
# | accept_date    | date    |
# +----------------+---------+
# This table may contain duplicates (In other words, there is no primary key for this table in SQL).
# This table contains the ID of the user who sent the request, the ID of the user who received the request,
# and the date when the request was accepted.

# Find the overall acceptance rate of requests, which is the number of acceptance divided
# by the number of requests. Return the answer rounded to 2 decimals places.
#
# Note that:
#
# The accepted requests are not necessarily from the table friend_request.
# In this case, Count the total accepted requests (no matter whether they are in the original requests),
# and divide it by the number of requests to get the acceptance rate.
# It is possible that a sender sends multiple requests to the same receiver,
# and a request could be accepted more than once. In this case, the ‘duplicated’ requests or acceptances are only counted once.
# If there are no requests at all, you should return 0.00 as the accept_rate.

import pandas as pd
from datetime import datetime

def acceptance_rate(friend_request: pd.DataFrame, request_accepted: pd.DataFrame) -> pd.DataFrame:
    friend_request.drop_duplicates(subset=["sender_id", "send_to_id"], inplace=True)
    request_accepted.drop_duplicates(subset=["requester_id", "accepter_id"], inplace=True)
    try:
        ans = (request_accepted.shape[0] / friend_request.shape[0])
    except ZeroDivisionError:
        ans = 0
    return pd.DataFrame({"accept_rate": [round(ans, 2)]})

FriendRequest = pd.DataFrame({
    "sender_id": [1, 1, 1, 2, 3],
    "send_to_id": [2, 3, 4, 3, 4],
    "request_date": [datetime(2016, 6, 1), datetime(2016, 6, 1),
                     datetime(2016, 6, 1), datetime(2016, 6, 2),
                     datetime(2016, 6, 9)]
})

RequestAccepted = pd.DataFrame({
    "requester_id": [1, 1, 2, 3, 3],
    "accepter_id": [2, 3, 3, 4, 4],
    "accept_date": [datetime(2016, 6, 3), datetime(2016, 6, 8),
                     datetime(2016, 6, 8), datetime(2016, 6, 9),
                     datetime(2016, 6, 10)]
})

print(acceptance_rate(FriendRequest, RequestAccepted))


