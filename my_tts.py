import torch
from TTS.api import TTS
import IPython.display as ipd


def en_models():
    # List available 🐸TTS en models
    models = TTS().list_models().list_models()
    for m in models:
        # print(m)
        if m.__contains__('/en/'):
            print(m)

def multi_speaker():
    print('hello TTS ...........')
    # Get device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f'Use device ${device}')

    # Init TTS
    # model = 'tts_models/multilingual/multi-dataset/xtts_v2'
    # model = 'tts_models/multilingual/multi-dataset/xtts_v1.1'

    # model = 'tts_models/en/ljspeech/tacotron2-DDC_ph'
    # model = 'tts_models/en/vctk/vits' # num_speakers=109, speakers={}
    model = 'tts_models/en/vctk/fast_pitch' # num_speakers=108, speakers={}

    tts = TTS(model).to(device)
    if tts.is_multi_speaker:
        print(f'Mutil-speaker model, speakers={tts.speakers}')
    print(f'该 model num_speakers={tts.synthesizer.tts_model.num_speakers}, speakers={tts.synthesizer.tts_speakers}')


    # Run TTS
    # ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
    # Text to speech list of amplitude values as output
    # wav = tts.tts(text="Hello world!", speaker_wav="yue/wav/audio.wav", language="en")
    # Text to speech to a file
    # tts.tts_to_file(text="Hello world!", speaker_wav="yue/wav/audio.wav", language="en", file_path="output.wav")

    # multi speaker model:
    tts.tts_to_file(text="Hello world! I want an apple.", speaker='VCTK_p225', file_path="output/ljspeech7.wav")
    # tts.tts_with_vc_to_file(text="Hello world! I want an apple, no, this is not apple.", speaker='p364', speaker_wav="wav/audio.wav", file_path="output/ljspeech4.wav")


    # tts.tts_to_file(text="Hello world! I want an apple.",  file_path="yue/output/ljspeech.wav")


def en_speaker():
    # Get device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f'Use device ${device}')

    # Init TTS ，
    tts = TTS("tts_models/en/ljspeech/tacotron2-DDC_ph").to(device)

    text = 'we know whenever there is a market concentration, there is really no competition. Right? There is no incentive to improve the quality of your product.'
    # Run TTS
    # tts.tts_to_file(text=text, speaker_wav="wav/easy-man.wav", file_path="output/easyman.wav")

    tts.tts_with_vc_to_file(text=text, speaker_wav="wav/audio.wav", file_path="output/audio2.wav")
    tts.tts_with_vc_to_file(text=text, speaker_wav="wav/easy-man.wav", file_path="output/easyman2.wav")

    # Example voice cloning with YourTTS in English, French and Portuguese
    # tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False).to(device)
    # tts.tts_to_file("This is voice cloning.", speaker_wav="wav/audio.wav", language="en", file_path="output.wav")

    # ipd.Audio(filename="output.wav")



if __name__ == '__main__':
    print('hello speaker ...........')
    multi_speaker()
    # en_models()
    # en_speaker()
