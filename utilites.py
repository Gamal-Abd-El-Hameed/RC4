import wave


def read_sound_file(filename):
    with wave.open(filename, 'rb') as file:
        params = file.getparams()
        sound_data = file.readframes(params.nframes)
    return params, sound_data


def write_sound_file(filename, params, data):
    with wave.open(filename, 'wb') as file:
        file.setparams(params)
        file.writeframes(data)


def swap(x, y):
    x, y = y, x
