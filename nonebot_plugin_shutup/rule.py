from datetime import datetime, timedelta

from nonebot.adapters import Event
from nonebot.adapters.onebot.v11.permission import (
    GROUP_ADMIN,
    GROUP_MEMBER,
    GROUP_OWNER,
)
from nonebot.permission import SUPERUSER
from nonebot.rule import to_me
from nonebot.typing import T_State

from .config import config


def shut_up_permission():
    if config.shutup_tome:
        return to_me()
    if config.shutup_permission == 3:
        return SUPERUSER
    if config.shutup_permission == 2:
        return SUPERUSER | GROUP_OWNER
    if config.shutup_permission == 1:
        return SUPERUSER | GROUP_OWNER | GROUP_ADMIN
    if config.shutup_permission == 0:
        return SUPERUSER | GROUP_OWNER | GROUP_ADMIN | GROUP_MEMBER
    return  None

permission = shut_up_permission()

async def shut_up_rule(event: Event, state: T_State):
    seeion_id = event.get_session_id()
    try:
            
        current_time = state[seeion_id]
    except KeyError:
        return False

    nowtime = datetime.now()

    if config.shutup_time <= 0:
        time_difference = timedelta(days=365)
    else:
        time_difference = current_time - nowtime

    return time_difference < timedelta(minutes=config.shutup_time)