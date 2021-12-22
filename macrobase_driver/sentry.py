from typing import Type

__skip_exceptions = set()


def skip_exception(*exceptions: Type[Exception]):
    for exc in exceptions:
        __skip_exceptions.add(exc)


def _exception_is_skipped(e: Exception) -> bool:
    for exc in __skip_exceptions:
        if isinstance(e, exc):
            return True

    return False


def sentry_before_send(event, hint):
    exc_info = hint.get('exc_info')
    log_record = hint.get('log_record')
    err = None

    if exc_info and isinstance(exc_info[0], Exception):
        err = exc_info[0]

    if err is None and getattr(log_record, 'exc_info') and isinstance(log_record.exc_info[0], Exception):
        err = log_record.exc_info[0]

    if not err or _exception_is_skipped(err):
        return None

    return event
