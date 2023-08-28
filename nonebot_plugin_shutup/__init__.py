from nonebot.plugin import PluginMetadata

from . import __main__ as __main__  # noqa: E402
from .config import ConfigModel  # noqa: E402

__version__ = "0.0.3"
__plugin_meta__ = PluginMetadata(
    name="雪豹闭嘴",
    description="基于 NoneBot2 的 插件，用于机器人当前会话闭嘴,支持全适配器",
    usage="发送“雪豹闭嘴”",
    type="application",
    homepage="https://github.com/Agnes4m/nonebot_pluigin_shutup",
    config=ConfigModel,
    supported_adapters=None,
    extra={
        "version": __version__,
        "author": ["Agnes4m <Z735803792@163.com>", "student_2333 <lgc2333@126.com>"],
    },
)
