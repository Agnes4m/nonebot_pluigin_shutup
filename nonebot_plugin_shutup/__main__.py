from datetime import datetime

from nonebot import on_endswith, on_message
from nonebot.adapters import Event
from nonebot.matcher import Matcher
from nonebot.params import Endswith, EventPlainText
from nonebot.permission import SUPERUSER
from nonebot.typing import T_State

from .config import config
from .rule import shut_up_permission, shut_up_rule

shut_up = on_endswith(("闭嘴", "shut up"), rule=shut_up_permission, priority=0, block=True)
shut_up_event = on_message(rule=shut_up_rule)
not_shut_up = on_endswith("说话", permission=SUPERUSER, priority=0, block=True)


@shut_up.handle()
async def _(
    event: Event,
    state: T_State,
    matcher: Matcher,
    msg: str = EventPlainText(),
    keyword: str = Endswith(),
):
    if len(config.shutup_name) != 0:
        start = msg.replace(keyword, "")
        if not start.startswith(tuple(config.shutup_name)):
            await matcher.finish()
    seeion_id = event.get_session_id()
    nowtime = datetime.now()
    state[seeion_id] = nowtime

    await matcher.finish(f"呜呜我会闭嘴{config.shutup_time}分钟的")


@shut_up_event.handle()
async def _(matcher: Matcher):
    matcher.stop_propagation()


@not_shut_up.handle()
async def _(
    event: Event,
    state: T_State,
    matcher: Matcher,
    msg: str = EventPlainText(),
    keyword: str = Endswith(),
):
    if len(config.shutup_name) != 0:
        start = msg.replace(keyword, "")
        if not start.startswith(tuple(config.shutup_name)):
            await matcher.finish()
    seeion_id = event.get_session_id()
    state.pop(seeion_id)
