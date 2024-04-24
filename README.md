### Web UI demo for Coqui TTS

### 环境：
- Python=3.10
- coqui-ai=v0.22.0
- gradio=4.25.0

### Coqui TTS GitHub：
- https://github.com/coqui-ai/TTS/tree/v0.22.0
### Coqui TTS 官网：
- https://docs.coqui.ai/en/latest/models/tortoise.html

### en models list: // 项目需要只选择纯英语模型
```angular2html
'tts_models/en/vctk/vits',  # Model is multi-speaker 
# 'tts_models/en/vctk/fast_pitch', 
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
```

