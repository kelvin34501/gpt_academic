from toolbox import CatchException, update_ui
from crazy_functions.crazy_utils import request_gpt_model_in_new_thread_with_ui_alive


@CatchException
def rebuttal文本转换(txt, llm_kwargs, plugin_kwargs, chatbot, history, system_prompt, web_port):
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

    i_say = r"As a computer vision professor and native English speaker, your task is to revise my mixed Chinese-English rebuttal draft. Your goal is to address the reviewers' concerns and persuade them to accept my paper by polishing it into clear, concise, accurate English that follows Nature/CVPR style guidelines while preserving the original meaning of the sentences.  Please ensure that your response is polite and humble throughout. Your revised version should be as concise as possible due to length limitations for the rebuttal. You may incorporate creative phrasing or sentences as needed for clarity or accuracy.  Furthermore, please focus on highlighting the strengths of our work while addressing any weaknesses raised by the reviewers. Please make sure you have a solid understanding of both computer vision concepts and academic writing conventions before starting this task.  Your response should provide detailed revisions with specific explanations for each change made."
    gpt_say = r"Sure, I'm happy to help! Please provide me with the draft."
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
