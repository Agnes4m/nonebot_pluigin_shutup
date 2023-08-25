from datetime import datetime, timedelta

from nonebot.adapters import Event
from nonebot.typing import T_State

from .config import config


async def shut_up_permission(event: Event):
    if config.shutup_tome and not event.is_tome():
        return False
    return True


async def shut_up_rule(event: Event, state: T_State):
    seeion_id = event.get_session_id()
    try:
        current_time = state[seeion_id]
    except KeyError:
        return False
    nowtime = datetime.now()
    time_difference = current_time - nowtime
    return time_difference < timedelta(minutes=config.shutup_time)
