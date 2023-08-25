from typing import List

from nonebot import get_driver
from pydantic import BaseModel


class ConfigModel(BaseModel):
    shutup_tome: bool = True
    shutup_name: List[str] = []
    shutup_time: int = 10
    shutup_permission: List[str] = ["超管"]


config: ConfigModel = ConfigModel.parse_obj(get_driver().config.dict())
