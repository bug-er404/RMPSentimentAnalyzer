# RMPSentimentAnalyzer
This application inspects the comments for a given institution or professor and identifies the predominant emotional opinion within the text. It primarily returns the sentiment associated with the comments along with the magnitude of emotion. Based on all the available comments, the application draws an overall sentiment rating.

We initially discussed how significant it is to select good professors for our courses. As college students, we highlighted how RateMyProfessor is a very useful platform to get to know our professors through multiple student reviews and ratings before actually taking them. We were motivated to utilize the available Google APIs and this drew our attention to natural language processing. We wanted to come up with a unique rating system based on the comments. We believe that words generate a more realistic overall rating than an aggregate of whole ratings. This is what inspired us to explore the use of Google Cloud Natural Language API on the comments posted in RateMyProfessor.

How we built it:
For the backend of the application, we used Python along with Google Cloud Natural Language API. For the frontend of the project, we used Java.
