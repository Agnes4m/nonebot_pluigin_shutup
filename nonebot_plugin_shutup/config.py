from typing import List

from nonebot import get_driver
from pydantic import BaseModel


class ConfigModel(BaseModel):
    shutup_tome: bool = True
    shutup_name: List[str] = []
    shutup_time: int = 10
    shutup_permission: int = 0
    """
    - 0: 全体
    - 1: 群管理员+
    - 2: 群主+
    - 3: 超级管理员
    """


config: ConfigModel = ConfigModel.parse_obj(get_driver().config)
