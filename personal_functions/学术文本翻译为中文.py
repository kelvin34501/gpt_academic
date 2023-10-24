from toolbox import CatchException, update_ui
from crazy_functions.crazy_utils import request_gpt_model_in_new_thread_with_ui_alive


@CatchException
def 学术文本翻译为中文(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
    """
    txt             输入栏用户输入的文本，例如需要翻译的一段话，再例如一个包含了待处理文件的路径
    llm_kwargs      gpt模型参数, 如温度和top_p等, 一般原样传递下去就行
    plugin_kwargs   插件模型的参数, 如温度和top_p等, 一般原样传递下去就行
    chatbot         聊天显示框的句柄，用于显示给用户
    history         聊天历史，前情提要
    system_prompt   给gpt的静默提醒
    web_port        当前软件运行的端口号
    """
    from pprint import pformat

    chatbot.clear()
    history = []  # reset history
    yield from update_ui(chatbot=chatbot, history=history)  # 刷新界面

    i_say = r"作为一名精通汉语和英语的人工智能领域教授，你的任务是将一段CVPR论文准确翻译为中文。请注意保持原句意思不变，同时符合中文的语法规则和习惯。在翻译的过程中，请不要使用如同：“我们”等主语形式，你可以更改句子为被动语态或者使用“本项目”作为主语。对于计算机视觉专业术语，请确保翻译准确无误。如果没有相应的中文翻译，请直接使用原始英文名称。 在翻译过程中，您可以自由添加新的句子来总结论文内容并增强翻译结果的丰富性。请注意，LaTeX标记的公式、符号、引用格式请不要更改，尤其不要删除latex引用中的如下划线`_`, 星号`*`等字符。保证Latex标记部分必须与原始输入完全相同。请输出清晰、明确、无歧义的最终版本。"
    gpt_say = r"好的，我很乐意帮忙！请提供给我原始的英文论文和任何额外的指导方针。"
    chatbot.append((i_say, gpt_say))
    history.append(i_say)
    history.append(gpt_say)
    yield from update_ui(chatbot=chatbot, history=history)  # 刷新界面

    gpt_response = yield from request_gpt_model_in_new_thread_with_ui_alive(
        inputs=txt,
        inputs_show_user=txt,
        llm_kwargs=llm_kwargs,
        chatbot=chatbot,
        history=history,
        sys_prompt="",  # 无需静默提示
    )
    chatbot[-1] = (txt, gpt_response)
    history.append(txt)
    history.append(gpt_response)
    yield from update_ui(chatbot=chatbot, history=history)  # 刷新界面
