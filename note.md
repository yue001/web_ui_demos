

### 安装模型过程中，安装的系统软件：
apt-get install ffmeg // 用于上传非 wav 音频时再输入模型前转换为 wav
apt-get install espeak-ng // 忘了哪个模型需要了

### 测试 ljspeech wavs:
> ./tests/data/ljspeech/wavs
```angular2html
- LJ001-00{01~32}.wav
test_speakers = [
    './tests/data/ljspeech/wavs/LJ001-0001.wav',
    './tests/data/ljspeech/wavs/LJ001-0002.wav',
    './tests/data/ljspeech/wavs/LJ001-0031.wav',
    './tests/data/ljspeech/wavs/LJ001-0032.wav'
]
```