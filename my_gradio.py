import random
import time
import os

import gradio as gr
import numpy as np



# -----------------------------------------------------------------------------
def greet(arg):
    return f'hello {arg}'

ui = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(lines=3, placeholder='input your name...', label='Name'),
    outputs='text')

# -------多组件----------------------------------------------------------------------
def greet2(name, male, age):
    # num = 'boy' if male else 'girl'
    say = f'hello, {name}, what a beautiful {"boy" if male else "girl"}'
    return say, age

demo2 = gr.Interface(
    fn=greet2,
    inputs=['text', 'checkbox', gr.Slider(18,30)],
    outputs=['text', 'number']
)

# ----使用 state 组件 存储会话状态 -------------------------------------------------------------------------
def chat(message, history):
    history = history or []
    message = message.lower()
    if message.startswith('how many'):
        response = str(random.randint(1,10))
    elif message.startswith('how'):
        response = random.choice(['Greet', 'Good', 'Okay', 'Bad'])
    elif message.startswith('where'):
        response = random.choice(['Beijing', 'New York', 'London'])
    else:
        response = "I don't know"
    history.append((message,response))
    return history, history
# 新建对话框
chatbot = gr.Chatbot()
demo3 = gr.Interface(
    fn=chat,
    inputs=['text', 'state'], # 添加 state 组件
    outputs=[chatbot, 'state'], # 输出更新的 state
    allow_flagging='never' # 设置不要保存按钮
)

# -----使用 Blocks 定制组件 --------------------------------------------------------------------
with gr.Blocks() as demo4:
    name = gr.Textbox(label='Name:')
    echo = gr.Textbox(label="ECHO:")
    button = gr.Button('GO')
    button.click(fn=greet, inputs=name, outputs=echo)

# ----使用生产器，实现连续多次输出，示例每隔一秒返回自动生成的图片----------------------------------------------------------------
def fake_diffusion(stemps):
    for _ in range(stemps):
        time.sleep(1)
        image = np.random.randint(255, size=(300,600,3))
        yield image

demo5 = gr.Interface(
    fn=fake_diffusion,
    inputs=gr.Slider(1, 10, value=3, step=1),
    outputs='image'
)


if __name__ == '__main__':
    print(f'当前命令路径：{os.getcwd()}')
    print(f'当前运行文件路径：{os.path.realpath(__file__)}')
    demo = demo5
    # 如函数执行时间过长，或流量过大，使用 queue 排队，该方法使用 websockets，防止 网络超时；
    demo.queue()
    app, local_url, share_url = demo.launch(server_name='0.0.0.0', server_port=6006, share=False)
    print(f'app is {app} \n local_url = {local_url} \n share_url = {share_url}')

