from toolbox import CatchException, update_ui
from crazy_functions.crazy_utils import request_gpt_model_in_new_thread_with_ui_alive


@CatchException
def 学术文本英文转换(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
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

    i_say = r"As an English native speaker and professor in the field of computer vision, your task is to polish a mixed Chinese and English draft paper into correct and precise English. Your output should be clear, concise, accurate, and follow the Nature/CVPR style guidelines while still preserving the original meaning and structure of the sentences in the draft paper. Please note that you must use present tense throughout your translation. Additionally, please feel free to incorporate creative wordings and sentences as needed for clarity or accuracy. Your response should also adhere to any relevant conventions associated with the Nature/CVPR style guidelines such as sentence structure, formatting, grammar rules, etc., so that it accurately reflects the scientific nature of the paper. Finally, please ensure that all changes are clearly marked or annotated so that they can be easily identified and verified by reviewers."
    gpt_say = r"Sure, I'm happy to help! Please provide me with the draft paper and any additional instructions or guidelines you would like me to follow."
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
