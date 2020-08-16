"""
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:

Logger logger = new Logger();

// logging string &quot;foo&quot; at timestamp 1
logger.shouldPrintMessage(1, &quot;foo&quot;); returns true; 

// logging string &quot;bar&quot; at timestamp 2
logger.shouldPrintMessage(2,&quot;bar&quot;); returns true;

// logging string &quot;foo&quot; at timestamp 3
logger.shouldPrintMessage(3,&quot;foo&quot;); returns false;

// logging string &quot;bar&quot; at timestamp 8
logger.shouldPrintMessage(8,&quot;bar&quot;); returns false;

// logging string &quot;foo&quot; at timestamp 10
logger.shouldPrintMessage(10,&quot;foo&quot;); returns false;

// logging string &quot;foo&quot; at timestamp 11
logger.shouldPrintMessage(11,&quot;foo&quot;); returns true;

"""
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        


# param_1 = obj.shouldPrintMessage(timestamp,message)
        pass


if __name__ == '__main__':
    assert Solution().__init__(0) == 0

