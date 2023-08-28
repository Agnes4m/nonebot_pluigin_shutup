from datetime import datetime, timedelta

from nonebot import get_driver
from nonebot.adapters import Event
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.log import logger
from .config import config


async def shut_up_permission(event: Event):
    if config.shutup_tome:
        return to_me()
    if config.shutup_permission and "超管" in config.shutup_permission:
        if event.get_user_id() in get_driver().config.superusers:
            a = True
        else:
            a = False
    else:
        a = False
    if a:
        logger.info("检测到禁言指令")
    return a


async def shut_up_rule(event: Event, state: T_State):
    seeion_id = event.get_session_id()
    try:
        current_time = state[seeion_id]
    except KeyError:
        return False
    nowtime = datetime.now()
    time_difference = current_time - nowtime
    return time_difference < timedelta(minutes=config.shutup_time)
