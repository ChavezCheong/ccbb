Which Platform:
1. Mobile (Kivy)
2. Desktop (Kivy)
3. Web (Django)
4. Game (PyGame, Unity [C++])
5. Data Science (Kaggle, Jupyter)
6. Machine Learning (Tensorflow)
7. Music Pitch Detector (Desktop Microphone)

App Idea:
(Mobile)
Hum a pitch and the app will recommend chords for you to play. Shows images of chords for different instruments. Accuracy to specific chords (not just major chords)

Components:
1. Need to figure out how to access the microphone on the phone and store the file (Used sounddevice)
1b. How to access different audio sources for the user to manage (customize)
2. Run an FFT on the pitch (Use python library)
https://pypi.org/project/crepe/
3. Library of chords (Database)
4. Determine pitch
5. Match pitches to chords (Xuan Min) (Guitar Chord API) (PyChord)
6. UI to display chords
7. Somehow connect backend engine to Kivy frontend
8. Error Handling
9. Logging of Errors

Tracking for Each Component:
1. Recording of Audio (detect audio and record for 3 seconds)

sounddevice (https://python-sounddevice.readthedocs.io/en/0.3.15/api/index.html)



2. Detecting Pitch

If machine learning libraries take .wav files as input, we need an efficient way of converting numpy arrays into wav
Possible solution is soundfile (https://stackoverflow.com/questions/47485692/writing-a-wav-file-using-sounddevice-and-numpy-in-python3)

https://www.kaggle.com/asparago/simple-pitch-detector

XM:
(https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.wavfile.write.html)

If FFT can be performed immediately on this numpy array, let it be. We need to convert the sine and cosine functions into frequencies for detection.

Do we want to 



Bibliography:
https://towardsdatascience.com/fast-fourier-transform-937926e591cb
https://www.programmableweb.com/api/guitar-chord-rest-api


