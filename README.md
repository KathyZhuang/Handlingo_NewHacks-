# Handlingo_NewHacks

![image](https://user-images.githubusercontent.com/35270359/117545587-6c5f5480-aff4-11eb-87b3-cbdaa03a6dc7.png)


## Link to Video
https://www.youtube.com/watch?v=rj5UIQ5HRg4&t=162s

## Inspiration
Under the current wave of globalization, people have the incentive to learn new languages for the ease of communication. Thus, bilingual education is greatly emphasized, and many language learning tools are offered in the market. However, people often forget there is a series of well-developed languages -- the sign languages that are crucial to the deaf community.

## What it does
Handlingo is an online platform that allows users to learn and practice different sign languages. Currently, the platform offers the American Sign Language and Italian Sign. Handlingo offers an interactive way of learning. Users can capture your answers with a webcam in real time, to get hands-on practice rather than just memorizing charts. The real time feedback system allows users to learn sign languages in an efficient way. More importantly, it bridges the communication gap that exists when there is a hearing impairment. It is a meaningful digital education tool that brings inclusivity to our community.

## How I built it
The project pipeline has three parts: user interface, backend and evaluation algorithm. The evaluation algorithm utilizes machine learning, specifically the convolution neural network and AlexNet transfer learning. The CNN model written in Pytorch is trained on two different datasets -- the ASL dataset and the Italian Sign Language dataset. It is able to recognize the hand gesture with over 97% of accuracy. The backend is written in Python, while the user interface is built with HTML, CSS and JavaScript.

## Built With
AlexNet, CSS, HTML, JavaScript, Python, Pytorch

## Challenges I ran into
Connecting the frontend, backend and the model within this short amount of time was quite challenging.

## Accomplishments that I'm proud of
We trained two CNN models and were able to reach a relatively high testing accuracy. More importantly, we learnt to collaborate with each other to accomplish the task together.

## What I learned
We learned to develop an interactive frontend, specifically on taking images with webcam and sending them to the backend. We also learned to design a machine learning pipeline starting from data collection, model training to building an interactive webpage.

## What's next for Handlingo
Implementing the English to Italian translation feature Include more sign languages to the database
