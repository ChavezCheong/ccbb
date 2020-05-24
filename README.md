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
1. Need to figure out how to access the microphone on the phone and store the file
2. Run an FFT on the pitch (Use python library)
https://pypi.org/project/crepe/
3. Library of chords (Database)
4. Determine pitch
5. Match pitches to chords (Xuan Min) (Guitar Chord API)
6. UI to display chords
7. Somehow connect backend engine to Kivy frontend
8. Error Handling
9. Logging of Errors





Bibliography:
https://towardsdatascience.com/fast-fourier-transform-937926e591cb
https://www.programmableweb.com/api/guitar-chord-rest-api


