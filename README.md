# PenguinsClassificationApp


Here is the app link: https://penguins-app-my2.herokuapp.com/

<p align="center">
<img src="https://i.natgeofe.com/k/88de42b8-764c-40d2-89ee-e72d55dc95b8/emperor-penguin-chicks_4x3.jpg" width="700" height="500">
</p>

Steps:
1. Using random forest classifier for classifying Penguin species based on various features like sex, beak length and body mass.
2. Saving a trained model using pickle.
3. Defining the app features in PenguinApp.py using streamlit
4. For running the command in Conda: ``` streamlit run PenguinApp.py  ```
5. Generating a permanent app interface link on Heroku: for that we need Procfile, setup.sh and requirements.txt files
6. Generate requirements file with conda prompt command ``` pipreqs ``` in the project directory.
7. Change app file name in Procfile and setup.sh remains same.


Links:
Project inspired from: https://www.youtube.com/watch?v=JwSS70SZdyM&ab_channel=freeCodeCamp.org
