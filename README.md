# TechLabs-Project

# Mood Booster
## Which is the problem the solution solves?
During quarantine due to COVID-19 global health crisis, the world realized that not everyone is prepared mentally for a lockdown, this has increased the suicide rate and depression skyrocket, Mood Booster goal its to reduce the lockdown effect on mental health using technology and the current demand for entertainment around the world.

## Solution Pitch
Mood Booster is a Web App desinged to help people stay mentally healthy in quarantine due to COVID-19, but not only in quarantine, also in their normal life style. Mood Booster's purpose is to keep up a positive mindset on the users feeding them with news and articles of their favorite topics and hobbies to show them how beautiful they can make their own life. 

## The solution
Mood Booster will start with a survey to get to know more about the user and take a photo, it will be optional to get access to Facebook for further exploring around the user taste, according to the information collected, Mood Booster will import and classify as good, neutral or bad news/articles. Every morning the web app/app along with a good morning and motivational quote will check the mood of the user, according to the mood of the user that day news, articles and content will be feed via notifications, this will also include recommendations on series, yoga, Sen culture, games, conferences, ted talks, etc. Due to the COVID-19 quarantine initially, Mood Booster won't ask about the mood, it will start with a good morning, motivational quote, and an invitation to do activities according to your tastes.

## Impact on the crisis
Mood Booster will become an entertainment and emotional ally for our users, to the extent that it gets to know their taste and fine-tune the suggestions to be more effective keeping a positive mindset, in the long run, the real purpose it that the users get to see how awesome their life is, create healthy habits, keep their mind busy and be more resilient to events that they can't entirely control.

# Further description	

## Table of contents
* [Survey](#Survey)
* [Facebook Scraping](#Facebook-Scraping)
* [Emotion Detection](#Emotion-Detection)
* [News/articles Classification](#News/articles-Classification)

## Survey
Initially, a survey will be conducted for each user to get to know more about his tastes, and every day a small survey will be conducted along with a good morning message to know how she/he is feeling on that day.

## Facebook Scraping and Data
With the data obtained within the analysis of data from various datasets and data on the person, it can be recommended
news and tastes. First of all, the data obtained from sources like data.gov helped to prove that there was
the need to help people who are suffering from these problems apart from this, as already mentioned the use of 
database we can recommend news to these people and improve their day.

![Image](https://github.com/ladiidie5/TechLabs-Project/blob/master/analysis_data/graphics/news.png)

## Emotion detection
Using [`DeepFace`](https://github.com/serengil/deepface) algorithm the user's face is scanned to detect her/his facial expression.

<p align="center"><img src="https://github.com/ladiidie5/TechLabs-Project/blob/master/Realtime_2%20test.PNG" width="60%" height="60%"></p>

## News Classification
Using [`Natural Language Toolkit`](http://www.nltk.org/), based on the information provided by the initial survey and Facebook scraping (optional), Mood Booster will import news/articles headlines to classify as good, neutral and bad, according to the classification these will be feed to the users during the day.

|                   	Headline                      | Label |
| ---                                                 | ---   | 
| ‘Death Proof’ (2007) is my favourite Quentin T...   |   0   |
| I need help finding the title of a movie.	          |   1   |
| Nutrition and Exercise: Timing is Everything	      |   0   |
| What makes unbalanced Movie bad?	                  |   -1  |
| Could I get your thoughts on "Computational St...   |   0   |
| New on Streaming Official Discussion Megathrea...   |   0   |
| Why superheroes don't die permanently in film?      |   1   |
| Looking for films similar to Bone Tomahawk          |   0   |
| Fifteen years on, how does Star Wars: Revenge ...   |   -1  |
| Anybody else thinks 3:10 Yuma has a very deep ...   |   0   |

Where (-1) stands for bad, (0) for neutrals and (1) stands for good news/articles.

-----------------------------------------------------
