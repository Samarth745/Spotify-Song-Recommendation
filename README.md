# Spotify-Song-Recommendation

<img src="https://storage.googleapis.com/pr-newsroom-wp/1/2018/11/Spotify_Logo_CMYK_Black.png" width="300" height="100"/> <br> 
**Goal** - The goal of the project is to provide song recommendations based on the search from user <br>
**Skills** - Machine Learning, Pandas.
# Model
## Using Search
The input is stored in search and spotipy library is used to find best results regarding this search from spotify web API <br>
The Best result song is then used to retreive other features of the song using spotify API library spotipy <br>
The result is stored in a vector <br>

## Recommendation
Spotify provides features in numeric forms which is already scaled <br>
The data base consists of multiple songs. We create a vector for each song on the deatures provided by spotify <br>
We use machine learning model to select 5 songs suggestions obtained from search. <br>
These 5 songs are shown as recommendation <br>
Further we store the Name, Link and url of the song for further use. 

##Algorithm
The recommendation engine uses the cosine similarity algorithm to find similar songs based on their attributes. The algorithm computes the cosine similarity between two movie vectors and returns a value between 0 and 1, with 1 indicating a perfect match.

## Web Application
Python Library streamlit is used to create a web application which takes input of the user and recommends songs based on search. <br>
The Web application also recieves Album cover and album link for better Interface
