import random
import torch
import os
import gc
from TTS.api import TTS

import gradio as gr


# ----my TTS demo ------------------------------------------------------------
# TTS/server/server.py default model = "tts_models/en/ljspeech/tacotron2-DDC"
# 推荐：tts_models/en/ljspeech/tacotron2-DDC_ph
models = [
            'tts_models/en/vctk/vits',  # Model is multi-speaker
            # 'tts_models/en/vctk/fast_pitch', # Model is multi-speaker # 运行报错；
            'tts_models/en/ek1/tacotron2',
            'tts_models/en/ljspeech/tacotron2-DDC',
            'tts_models/en/ljspeech/tacotron2-DDC_ph',
            'tts_models/en/ljspeech/glow-tts', # num_speakers=0
            'tts_models/en/ljspeech/speedy-speech', # no attribute 'num_speakers'
            'tts_models/en/ljspeech/tacotron2-DCA',
            'tts_models/en/ljspeech/vits', # num_speakers=0
            'tts_models/en/ljspeech/vits--neon', # num_speakers=0
            'tts_models/en/ljspeech/fast_pitch', # no attribute 'num_speakers'
            'tts_models/en/ljspeech/overflow',  # no attribute 'num_speakers'
            'tts_models/en/ljspeech/neural_hmm', # no attribute 'num_speakers'
            'tts_models/en/sam/tacotron-DDC',
            'tts_models/en/blizzard2013/capacitron-t2-c50',
            'tts_models/en/blizzard2013/capacitron-t2-c150_v2',
            'tts_models/en/multi-dataset/tortoise-v2', # no attribute 'num_speakers'
            'tts_models/en/jenny/jenny', # num_speakers=0
          ]


tts :TTS = None

def create_tts_with_model(model):
    global tts
    if tts:
        # 删除旧模型对象 # 释放GPU缓存
        del tts
        gc.collect()
        torch.cuda.empty_cache()

    # Get device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts = TTS(model).to(device)
    print(f'使用 device ${device}')

def on_choose_model(model):
    print(f'选择了model：{model}')
    create_tts_with_model(model)
    global tts
    if tts.is_multi_speaker:
        print(f'{model} is Mutil-speaker model, speaker_count={len(tts.speakers)}')
        return gr.update(choices=tts.speakers, value=tts.speakers[0])
    else:
        return gr.update(choices=[], value=None)

def tts_convert(model, speaker, upload, text):
    print(f'选择模型：{model} 选择speaker：{speaker} 上传录音：{upload} \nTEXT: {text}')
    global tts
    model_name = model.split("/")[-1]
    out_file = f'output/ttsgen-{model_name}-{random.randint(1000, 9999)}.wav'

    if tts.is_multi_speaker:
        if upload:
            # speaker_wav = upload
            tts.tts_with_vc_to_file(text=text, speaker=speaker, speaker_wav=upload, file_path=out_file)
        else:
            # 使用 speaker
            tts.tts_to_file(text=text, speaker=speaker, file_path=out_file)
    else:
        if upload:
            # speaker_wav = upload
            tts.tts_with_vc_to_file(text=text, speaker_wav=upload, file_path=out_file)
        else:
            # 不使用 speaker
            tts.tts_to_file(text=text, file_path=out_file)

    print(f'生成音频：{out_file}')
    return out_file


def fix_speaker_path(selected):
    return f'{os.getcwd()}/../{selected}'

def download_all_models():
    for model in models:
        on_choose_model(model)
        tts_convert(model, f'完成{model}', None, 'please give me an apple.')

with gr.Blocks() as ttsDemo:
    default_model_index = 0
    model = gr.Dropdown(label='Select an english TTS model :', choices=models, value=models[default_model_index])
    # 初始化选项
    create_tts_with_model(models[default_model_index])
    cur_model_speakers = tts.speakers if tts.is_multi_speaker else []

    with gr.Row():
        speaker = gr.Dropdown(label='Select a build-in voice, NOTE: Only 【en/vctk/vits】 support multi-speaker voices.',
                              choices=cur_model_speakers,
                              value=cur_model_speakers[0] if cur_model_speakers else None)
        upload = gr.Audio(label='Upload a voice file(.wav) for cloning:',
                          sources=["upload", "microphone"], # 'upload|microphone',
                          type='filepath',
                          format='wav')

    model.change(fn=on_choose_model, inputs=model, outputs=speaker)

    text = gr.Textbox(label='Input in English to convert :', lines=4)
    with gr.Row():
        submit = gr.Button('Convert').click(
            fn = tts_convert,
            inputs = [model, speaker, upload, text],
            outputs = gr.Audio(label='TTS Result:')
        )
    # gr.Button('update_speaker_dropdown...').click(fn=update_speaker_dropdown)

if __name__ == '__main__':
    ttsDemo.queue()
    ttsDemo.launch(server_name='0.0.0.0', server_port=6006, share=False)












