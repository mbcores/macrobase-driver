from asyncio import AbstractEventLoop, get_event_loop
from typing import ClassVar

from macrobase_driver.context import Context
from macrobase_driver.config import DriverConfig


class MacrobaseDriver(object):

    def __init__(self, name: str = None, *args, **kwargs):
        self.name = name
        self.config = DriverConfig
        self.context = Context()

    @property
    def loop(self) -> AbstractEventLoop:
        return get_event_loop()

    def update_config(self, config_obj: ClassVar[DriverConfig]):
        pass

    def run(self, *args, **kwargs):
        pass
