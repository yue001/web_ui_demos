### Web UI demo for Coqui TTS

# 环境：
- Python=3.10
- coqui-ai=v0.22.0
- 

# Coqui TTS GitHub：
- https://github.com/coqui-ai/TTS/tree/v0.22.0
# Coqui TTS 官网：
- https://docs.coqui.ai/en/latest/models/tortoise.html

# 示例样本：
when we write off the whole system as inevitably corrupt, and when we sit back and blame the leaders we elect without examining our own role in electing them.

# en models list: // 项目需要只选择纯英语模型
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

# 安装模型过程中，安装的系统软件：
apt-get install ffmeg // 用于上传非 wav 音频时再输入模型前转换为 wav
apt-get install espeak-ng // 忘了哪个模型需要了

# 测试 ljspeech wavs:
> ./tests/data/ljspeech/wavs
- LJ001-00{01~32}.wav
test_speakers = [
    './tests/data/ljspeech/wavs/LJ001-0001.wav',
    './tests/data/ljspeech/wavs/LJ001-0002.wav',
    './tests/data/ljspeech/wavs/LJ001-0031.wav',
    './tests/data/ljspeech/wavs/LJ001-0032.wav'
]