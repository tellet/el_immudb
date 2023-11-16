# el_immudb

### What kind of data would you store immutable?

1. So, my first thought was about storing logs. A possible use case for that is to track activity in online games, and then analyse it for suspicious flows.
2. The second thing is version control system, immutability helps here to track the changes and to keep existing code safe from unwanted modifications.
3. Then goes financial transactions' case like payments and money transfers, immutable data here can to support better audit.
4. There are other cases of course, like storing personal medical data and blockchain. 

### Create either a manual test flow or an automatic test for your selected use case.

The use case - store event logs.

Logged data: 
* timestamp
* event type (LOG IN|LOG OUT|LIKE|DISLIKE)
* ip address

**Positive flow**\
**Given**: There is an immudb set-up\
**When**: A new event happens in the system\
**Then**: I should understand that event is logged successfully\
&nbsp;&nbsp;&nbsp;&nbsp; **And**: The event should appear in the immudb storage

**Negative flow**\
**Given**: There is an immudb set-up\
**When**: A new event happens in the system\
&nbsp;&nbsp;&nbsp;&nbsp;**And**: immudb token is expired\
**Then**: I should understand that event was not logged\
&nbsp;&nbsp;&nbsp;&nbsp;**And**: The event should not appear in the immudb storage

## Run the tests
### Prerequisites
* Python 3.10
* pip

From [project root](.) run the following commands:
```shell
pip install -r requirements.txt
pytest 
```