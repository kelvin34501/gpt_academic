from toolbox import HotReload

PREFIX = "自定义-"

def get_personal_functions():
    from personal_functions.学术文本翻译为中文 import 学术文本翻译为中文
    from personal_functions.学术文本英文转换 import 学术文本英文转换

    function_plugins = {
        PREFIX + "学术文本翻译为中文": {
            "Group": "学术",
            "Color": "stop",
            "AsButton": True,
            "Info": "自定义：学术文本翻译为中文",
            "Function": HotReload(学术文本翻译为中文)
        },
        PREFIX + "学术文本英文转换": {
            "Group": "学术",
            "Color": "stop",
            "AsButton": True,
            "Info": "自定义：学术文本英文转换",
            "Function": HotReload(学术文本英文转换)
        }
    }

    """
    设置默认值:
    - 默认 Group = 对话
    - 默认 AsButton = True
    - 默认 AdvancedArgs = False
    - 默认 Color = secondary
    """
    for name, function_meta in function_plugins.items():
        if "Group" not in function_meta:
            function_plugins[name]["Group"] = '对话'
        if "AsButton" not in function_meta:
            function_plugins[name]["AsButton"] = True
        if "AdvancedArgs" not in function_meta:
            function_plugins[name]["AdvancedArgs"] = False
        if "Color" not in function_meta:
            function_plugins[name]["Color"] = 'secondary'

    return function_plugins