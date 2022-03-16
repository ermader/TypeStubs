"""
This type stub file was generated by pyright.
"""

import logging
import timeit

TIME_LEVEL: int = ...
DEFAULT_FORMATS: dict[str, str] = ...

class LevelFormatter(logging.Formatter):
    """Log formatter with level-specific formatting.

    Formatter class which optionally takes a dict of logging levels to
    format strings, allowing to customise the log records appearance for
    specific levels.


    Attributes:
            fmt: A dictionary mapping logging levels to format strings.
                    The ``*`` key identifies the default format string.
            datefmt: As per py:class:`logging.Formatter`
            style: As per py:class:`logging.Formatter`

    >>> import sys
    >>> handler = logging.StreamHandler(sys.stdout)
    >>> formatter = LevelFormatter(
    ...     fmt={
    ...         '*':     '[%(levelname)s] %(message)s',
    ...         'DEBUG': '%(name)s [%(levelname)s] %(message)s',
    ...         'INFO':  '%(message)s',
    ...     })
    >>> handler.setFormatter(formatter)
    >>> log = logging.getLogger('test')
    >>> log.setLevel(logging.DEBUG)
    >>> log.addHandler(handler)
    >>> log.debug('this uses a custom format string')
    test [DEBUG] this uses a custom format string
    >>> log.info('this also uses a custom format string')
    this also uses a custom format string
    >>> log.warning("this one uses the default format string")
    [WARNING] this one uses the default format string
    """

    def __init__(self, fmt=..., datefmt=..., style=...) -> None: ...
    def format(self, record): ...

def configLogger(**kwargs):  # -> None:
    """A more sophisticated logging system configuation manager.

    This is more or less the same as :py:func:`logging.basicConfig`,
    with some additional options and defaults.

    The default behaviour is to create a ``StreamHandler`` which writes to
    sys.stderr, set a formatter using the ``DEFAULT_FORMATS`` strings, and add
    the handler to the top-level library logger ("fontTools").

    A number of optional keyword arguments may be specified, which can alter
    the default behaviour.

    Args:

            logger: Specifies the logger name or a Logger instance to be
                    configured. (Defaults to "fontTools" logger). Unlike ``basicConfig``,
                    this function can be called multiple times to reconfigure a logger.
                    If the logger or any of its children already exists before the call is
                    made, they will be reset before the new configuration is applied.
            filename: Specifies that a ``FileHandler`` be created, using the
                    specified filename, rather than a ``StreamHandler``.
            filemode: Specifies the mode to open the file, if filename is
                    specified. (If filemode is unspecified, it defaults to ``a``).
            format: Use the specified format string for the handler. This
                    argument also accepts a dictionary of format strings keyed by
                    level name, to allow customising the records appearance for
                    specific levels. The special ``'*'`` key is for 'any other' level.
            datefmt: Use the specified date/time format.
            level: Set the logger level to the specified level.
            stream: Use the specified stream to initialize the StreamHandler. Note
                    that this argument is incompatible with ``filename`` - if both
                    are present, ``stream`` is ignored.
            handlers: If specified, this should be an iterable of already created
                    handlers, which will be added to the logger. Any handler in the
                    list which does not have a formatter assigned will be assigned the
                    formatter created in this function.
            filters: If specified, this should be an iterable of already created
                    filters. If the ``handlers`` do not already have filters assigned,
                    these filters will be added to them.
            propagate: All loggers have a ``propagate`` attribute which determines
                    whether to continue searching for handlers up the logging hierarchy.
                    If not provided, the "propagate" attribute will be set to ``False``.
    """
    ...

class Timer:
    """Keeps track of overall time and split/lap times.

    >>> import time
    >>> timer = Timer()
    >>> time.sleep(0.01)
    >>> print("First lap:", timer.split())
    First lap: ...
    >>> time.sleep(0.02)
    >>> print("Second lap:", timer.split())
    Second lap: ...
    >>> print("Overall time:", timer.time())
    Overall time: ...

    Can be used as a context manager inside with-statements.

    >>> with Timer() as t:
    ...     time.sleep(0.01)
    >>> print("%0.3f seconds" % t.elapsed)
    0... seconds

    If initialised with a logger, it can log the elapsed time automatically
    upon exiting the with-statement.

    >>> import logging
    >>> log = logging.getLogger("my-fancy-timer-logger")
    >>> configLogger(logger=log, level="DEBUG", format="%(message)s", stream=sys.stdout)
    >>> with Timer(log, 'do something'):
    ...     time.sleep(0.01)
    Took ... to do something

    The same Timer instance, holding a reference to a logger, can be reused
    in multiple with-statements, optionally with different messages or levels.

    >>> timer = Timer(log)
    >>> with timer():
    ...     time.sleep(0.01)
    elapsed time: ...s
    >>> with timer('redo it', level=logging.INFO):
    ...     time.sleep(0.02)
    Took ... to redo it

    It can also be used as a function decorator to log the time elapsed to run
    the decorated function.

    >>> @timer()
    ... def test1():
    ...    time.sleep(0.01)
    >>> @timer('run test 2', level=logging.INFO)
    ... def test2():
    ...    time.sleep(0.02)
    >>> test1()
    Took ... to run 'test1'
    >>> test2()
    Took ... to run test 2
    """

    _time = timeit.default_timer
    default_msg = ...
    default_format = ...
    def __init__(self, logger=..., msg=..., level=..., start=...) -> None: ...
    def reset(self, start=...):  # -> None:
        """Reset timer to 'start_time' or the current time."""
        ...
    def time(self):  # -> float:
        """Return the overall time (in seconds) since the timer started."""
        ...
    def split(self):  # -> float:
        """Split and return the lap time (in seconds) in between splits."""
        ...
    def formatTime(self, msg, time):  # -> str:
        """Format 'time' value in 'msg' and return formatted string.
        If 'msg' contains a '%(time)' format string, try to use that.
        Otherwise, use the predefined 'default_format'.
        If 'msg' is empty or None, fall back to 'default_msg'.
        """
        ...
    def __enter__(self):  # -> Self@Timer:
        """Start a new lap"""
        ...
    def __exit__(self, exc_type, exc_value, traceback):  # -> None:
        """End the current lap. If timer has a logger, log the time elapsed,
        using the format string in self.msg (or the default one).
        """
        ...
    def __call__(
        self, func_or_msg=..., **kwargs
    ):  # -> ((*args: Unknown, **kwds: Unknown) -> Unknown) | Self@Timer:
        """If the first argument is a function, return a decorator which runs
        the wrapped function inside Timer's context manager.
        Otherwise, treat the first argument as a 'msg' string and return an updated
        Timer instance, referencing the same logger.
        A 'level' keyword can also be passed to override self.level.
        """
        ...
    def __float__(self): ...
    def __int__(self) -> int: ...
    def __str__(self) -> str: ...

class ChannelsFilter(logging.Filter):
    """Provides a hierarchical filter for log entries based on channel names.

    Filters out records emitted from a list of enabled channel names,
    including their children. It works the same as the ``logging.Filter``
    class, but allows the user to specify multiple channel names.

    >>> import sys
    >>> handler = logging.StreamHandler(sys.stdout)
    >>> handler.setFormatter(logging.Formatter("%(message)s"))
    >>> filter = ChannelsFilter("A.B", "C.D")
    >>> handler.addFilter(filter)
    >>> root = logging.getLogger()
    >>> root.addHandler(handler)
    >>> root.setLevel(level=logging.DEBUG)
    >>> logging.getLogger('A.B').debug('this record passes through')
    this record passes through
    >>> logging.getLogger('A.B.C').debug('records from children also pass')
    records from children also pass
    >>> logging.getLogger('C.D').debug('this one as well')
    this one as well
    >>> logging.getLogger('A.B.').debug('also this one')
    also this one
    >>> logging.getLogger('A.F').debug('but this one does not!')
    >>> logging.getLogger('C.DE').debug('neither this one!')
    """

    def __init__(self, *names) -> None: ...
    def filter(self, record): ...

class CapturingLogHandler(logging.Handler):
    def __init__(self, logger, level) -> None: ...
    def __enter__(self): ...
    def __exit__(self, type, value, traceback): ...
    def emit(self, record): ...
    def assertRegex(self, regexp, msg=...): ...

class LogMixin:
    """Mixin class that adds logging functionality to another class.

    You can define a new class that subclasses from ``LogMixin`` as well as
    other base classes through multiple inheritance.
    All instances of that class will have a ``log`` property that returns
    a ``logging.Logger`` named after their respective ``<module>.<class>``.

    For example:

    >>> class BaseClass(object):
    ...     pass
    >>> class MyClass(LogMixin, BaseClass):
    ...     pass
    >>> a = MyClass()
    >>> isinstance(a.log, logging.Logger)
    True
    >>> print(a.log.name)
    fontTools.misc.loggingTools.MyClass
    >>> class AnotherClass(MyClass):
    ...     pass
    >>> b = AnotherClass()
    >>> isinstance(b.log, logging.Logger)
    True
    >>> print(b.log.name)
    fontTools.misc.loggingTools.AnotherClass
    """

    @property
    def log(self) -> logging.Logger: ...

def deprecateArgument(name: str, msg: str, category: Warning = ...) -> None:
    """Raise a warning about deprecated function argument 'name'."""
    ...

def deprecateFunction(
    msg: str, category: Warning = ...
):  # -> (func: Unknown) -> ((*args: Unknown, **kwargs: Unknown) -> Unknown):
    """Decorator to raise a warning when a deprecated function is called."""
    ...

if __name__ == "__main__": ...
