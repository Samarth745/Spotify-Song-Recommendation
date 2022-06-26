import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np
    
st.title('Spotify Song recommendation')
    
    
    
Track_name = st.text_input('Enter name of track')
Artist_name=st.text_input('Enter name of artist')
    
    
client_credentials_manager = SpotifyClientCredentials(client_id='f76ee452a0464e9198b742acce8b3ff6', client_secret='6c27e0026ad0424393f1e96ee7a05851')
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    
def get_track(x,y):
    input_song = sp.search('track:%s artists:%s'%(x,y),limit=1)['tracks']['items'][0]['name']
    input_song_id = sp.search('track:%s artists:%s'%(x,y),limit=1)['tracks']['items'][0]['id']
    input_song_features = sp.audio_features(input_song_id)
    input_song_df = pd.DataFrame(input_song_features)
    print(input_song)
    return(input_song_df,input_song)
    
def get_index(df,input_song_df):   
    new_data = df.iloc[:,:11]   
    new_result = input_song_df.iloc[:,:11]

    new_data['Vector']=new_data.apply(lambda x:tuple(x),axis=1)
    new_result['Vector']=new_result.apply(lambda x:tuple(x),axis=1)

    b = new_result['Vector'][0]

    b = np.array(b)
    new_data['distance']=new_data['Vector'].apply(lambda x:np.linalg.norm(x-b))

    index = new_data.sort_values('distance').head().index
    return(index)
    
    
if st.button('Recommend'):
    input_song_df,inputsong = get_track(Track_name,Artist_name)
    st.markdown("On the basis of your favourite track %s suggestions are"%inputsong)
    df=pd.read_csv(r'C:\Users\Samarth\Desktop\Music_data.csv')
    index = get_index(df,input_song_df)
    
    
    
        
    A=[]
    for j in index:
        name_of_song = df.iloc[j,-3]
        id_of_song = df.iloc[j,-10]
        url_of_song = 'http://open.spotify.com/track/%s'%id_of_song
        result = sp.search(name_of_song)  
        image = result['tracks']['items'][0]['album']['images'][0]['url']
        A.append((name_of_song,url_of_song,image))
    A=pd.DataFrame(A)
    A.rename(columns={0:'Track name', 1:'Link',2:'Image'},inplace=True)
    
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
            st.image(A.loc[0][2],width=200)
            st.markdown(A.loc[0][0])
            link = A.loc[0][1]
            st.write(link,unsafe_allow_html=True)
    with col2:
            st.image(A.loc[1][2],width=200)
            st.markdown(A.loc[1][0])
            link = A.loc[1][1]
            st.write(link,unsafe_allow_html=True)
    with col3:
            st.image(A.loc[2][2],width=200)
            st.markdown(A.loc[2][0])
            link = A.loc[2][1]
            st.write(link,unsafe_allow_html=True)
    with col4:
            st.image(A.loc[3][2],width=200)
            st.markdown(A.loc[3][0])
            link = A.loc[3][1]
            st.write(link,unsafe_allow_html=True)
    with col5:
            st.image(A.loc[4][2],width=200)
            st.markdown(A.loc[4][0])
            link = A.loc[4][1]
            st.write(link,unsafe_allow_html=True)
    


#st.image('https://i.scdn.co/image/ab67616d0000b2733f5d63f12fa8e44a86936e07', width=200)