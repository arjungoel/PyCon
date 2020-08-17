AGENDA:- 

- Why logging matters - It allows you to see what application is doing when it's running in production.

- How logging works

# logger class is the main class that you interacts with. When you write a python program you basically takes a logger, we call one of the methods that it have and then we just pass a string
# template and arguments to it. The logger first creates a log record that not only contains the template and the message that you have but also some in context that where is this being
# logged. A handler would take your log record and put it into a stream. The log record is an object. Formatter takes the log records and transforms them into a string.

# Filter allows you to filter the logs on more like fine-tuned characteristics. 


#################################
Loggging Heirarchy:-
#################################

- Whenver you create a logger you can have this function:-
logger = logging.getLogger("parent.child")

that will retrieve a function with the string separated tokens that you pass on it.



- How to use it
- How to configure it

- logging allows multi-threading. It is very flexible as you can categorize your logs.
- It allows us to split the how from the what. It gives us a collaborative approach of what you want to log without having to worrying about how it is going to be logged.


####################
LEVELS:-
####################

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

Every message has a "level". All of these levels are predefined. You can add your levels if you want but in the end they all become numeric levels and they are used for controlling how many
messages really come out. We can turn the logging level down so we can get any more info while debugging and it's always compared with >=.

Logger -> The thing you pass log messages into.
LogRecord -> A container of log information.
Handler -> Something that outputs the logs.
Formatter -> Format a LogRecord for output.

- _checkLevel() function turns Level name into Level number.


# LogRecord has one method: getMessage() which takes the message you got it and spot resolves it with the odds you gave it which is why you always call and pass "message format and list of
# arguments" or "message format and dict of arguments".


:heavy_check_mark:    
-----------------------------------------------------
Always call as:-

log.level(msgformat, param, param, param)
			or:
	log.level(msgformat, {params})
-----------------------------------------------------


::x::       
-----------------------------------------------------

NOT:- 

log.level(msgformat.format(arg, arg))
    log.level(f'{msg}format{...}')
-----------------------------------------------------



