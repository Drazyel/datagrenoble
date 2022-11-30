import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import pydeck as pdk
import geopandas as gpd
from geopandas import GeoDataFrame
import pydeck as pdk
import base64





def main():

    pages = {
        'Accueil': Accueil,
        'Contexte':laulau,
        'Dashboard':val,
        'Heatmap': premiere_analyse,
        'Animations': best_corr,
        'les limites' : region_results,
        'Conclusion':conclusion,
        }

    if "page" not in st.session_state:
        st.session_state.update({
        # Default page
        'page': 'Accueil'
        })



    with st.sidebar:
        st.image('logogrenoble.png', width=300)
        page = st.selectbox("Choose a page", tuple(pages.keys()))


    pages[page]()


def Accueil():

    st.write('\n')
    st.write('\n')
    st.write('\n')

    def _max_width_():
        max_width_str = "max-width: 1300px;"
        st.markdown(
            f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str}
        }}
        </style>    
        """,
            unsafe_allow_html=True,
        )

    _max_width_()

           
    with open('p1_accueil.html','r',encoding='UTF-8') as file :
        data = file.read()

    st.markdown(data, unsafe_allow_html=True)

    st.write('\n')
    st.write('\n')
    st.write('\n')

    col1, col2, col3 = st.columns(3)
    with col1:
        st.image('grenoblesat.png', width=800)

    
def laulau():
     #graphs centrés
    config = {'displayModeBar': False}

    with open('laulau.html','r',encoding='UTF-8') as file :
        data = file.read()

    st.markdown(data, unsafe_allow_html=True)


def val():
     #graphs centrés
    config = {'displayModeBar': False}

    with open('val.html','r',encoding='UTF-8') as file :
        data = file.read()
    def _max_width_():
        max_width_str = "max-width: 800px;"
        st.markdown(
            f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str}
        }}
        </style>    
        """,
            unsafe_allow_html=True,
        )

    _max_width_()
    col1, col2, col3 = st.columns(3)
    with col1:
        modes = st.radio(
        "Choix mode de transport 👉",
        key="visibility",
        options=["Velo", "Trotinette","Les deux"],)

    with col2:    
        species_option = st.selectbox('Choisir mode de transport',('taux utilisation','Disponibilite','CA','Km Parcourus'))
        if species_option == 'taux utilisation' and modes == 'Velo':
            st.image('tauxOccup.png', width=950)
        if species_option == 'taux utilisation' and modes =='Trotinette':
            st.image('tauxOccup.png', width=950)
        if species_option == 'taux utilisation' and modes =='Les deux':
            st.image('tauxOccup.png', width=950)
        if species_option == 'Disponibilite' and modes == 'Velo':
            st.image('bike-utilise.jpg', width=950)
        if species_option == 'Disponibilite' and modes =='Trotinette':
            st.image('trot_utilise.jpg', width=950)
        if species_option == 'Disponibilite' and modes =='Les deux':
            st.image('Nb_utilisés_jours.jpg', width=950)
        if species_option == 'CA' and modes == 'Velo':
            st.image('CAbike.png', width=950)
        if species_option == 'CA' and modes =='Trotinette':
            st.image('CAscootter.png', width=950)
        if species_option == 'CA' and modes =='Les deux':
            st.image('Laurence2.jpg', width=950)   
        if species_option == 'Km Parcourus' and modes == 'Velo':
            st.image('bike_km_moy.jpg', width=950)
        if species_option == 'Km Parcourus' and modes =='Trotinette':
            st.image('trot_km_moy.jpg', width=950)
        if species_option == 'Km Parcourus' and modes =='Les deux':
            st.image('kilometres_moyen.jpg', width=950)   
       
    # Show Plots

def premiere_analyse():



    def _max_width_():
        max_width_str = "max-width: 800px;"
        st.markdown(
            f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str}
        }}
        </style>    
        """,
            unsafe_allow_html=True,
        )

    _max_width_()

    col1, col2, col3 = st.columns(3)
    with col2:
        st.image('logos.jpg', width=200)
    
    
    #texte explicatif en html    
    with open('p2_première analyse.html','r',encoding='UTF-8') as file :
        data = file.read()

    st.markdown(data, unsafe_allow_html=True)
    
            
    st.write('\n')
    st.write('\n')
    st.write('\n')

    df = pd.read_csv(r"http://91.166.31.159:62020/share/JHM-695W9u_AziSi/filter.csv")

    px.set_mapbox_access_token("pk.eyJ1IjoiZHJhenllbCIsImEiOiJjbGFzZGF4bGIxbTk0M3Budm5iOHJmNGR3In0.ZJdWPpessKf7-0JyHouAhg")

    df = pd.DataFrame(df,
       columns=['lat', 'lon'])

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=45.155723,
            longitude=5.716685,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
               'Scatterplotlayer',
               data=df,
               get_position='[lon, lat]',
               radius=100,
               elevation_scale=25,
               elevation_range=[0, 1000],
               pickable=True,
               extruded=True,
            ),
            pdk.Layer(
                'HeatmapLayer',
                data=df,
                get_position='[lon, lat]',
                get_color='[180, 0, 200, 140]',
                get_radius=250,
            ),
        ],
    ))







def best_corr():

    #graphs centrés
    config = {'displayModeBar': False}


    #utilisation de la largeur de la page
    def _max_width_():
        max_width_str = "max-width: 800px;"
        st.markdown(
            f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str}
        }}
        </style>    
        """,
            unsafe_allow_html=True,
        )

    _max_width_()



    link = 'http://91.166.31.159:62020/share/JHM-695W9u_AziSi/filter.csv'
    df1 = pd.read_csv(link)
    


    #commentaire graph 1 et accueil page
    with open('p3_diff_corr.html','r',encoding='UTF-8') as file :
        data3 = file.read()

    st.markdown(data3, unsafe_allow_html=True)


    def animate_map(time_col):
        fig = px.scatter_mapbox(df1,
              lat="lat" ,
              lon="lon",
              hover_name="bike_id",
              color="vehicle_type_id",
              animation_frame=time_col,
              mapbox_style='open-street-map',
              category_orders={
              time_col:list(np.sort(df1["last-reported_d"].unique()))
              },                  
              zoom=10)
        fig.show();
    animate_map(time_col='time')

    #commentaire graph
    



def region_results():

     #graphs centrés
    config = {'displayModeBar': False}

    with open('val.html','r',encoding='UTF-8') as file :
        data = file.read()
    def _max_width_():
        max_width_str = "max-width: 800px;"
        st.markdown(
            f"""
        <style>
        .reportview-container .main .block-container{{
            {max_width_str}
        }}
        </style>    
        """,
            unsafe_allow_html=True,
        )

    _max_width_()
    col1, col2, col3 = st.columns(3)
    with col1:
        modes = st.radio(
        "Choix mode de transport 👉",
        key="visibility",
        options=["Velo", "Trotinette","Les deux"],)

    with col2:    
        species_option = st.selectbox('Etat de la flotte',('Non Fonctionnel','Batterie Vide','Carte des pannes','babouche'))
        if species_option == 'Non Fonctionnel' and modes == 'Velo':
            st.image('bike-casse.jpg', width=1000)
        if species_option == 'Non Fonctionnel' and modes == 'Trotinette':
            st.image('trot_casse.jpg', width=1000)
        if species_option == 'Non Fonctionnel' and modes == 'Les deux':
            st.image('non_fonctinnel_val2.jpg', width=1000)   
        if species_option == 'Batterie Vide' and modes == 'Les deux':
            st.image('nb_vehicules_batteries_vides.jpg', width=1000)
        if species_option == 'Batterie Vide' and modes == 'Velo':
            st.image('bike_batterie_vide.jpg', width=1000)
        if species_option == 'Batterie Vide' and modes == 'Trotinette':
            st.image('trot_ batterie_vide.jpg', width=1000)
        if species_option == 'Carte des pannes' and modes == 'Velo':
            st.image('bike_map.jpg', width=1000)
        if species_option == 'Carte des pannes' and modes == 'Trotinette':
            st.image('trot_map.jpg', width=1000)
        if species_option == 'Carte des pannes' and modes == 'Les deux':
            st.image('val1.jpg', width=1000)        

        






def conclusion():
     #graphs centrés
    config = {'displayModeBar': False}

    with open('conclu.html','r',encoding='UTF-8') as file :
        data = file.read()

    st.markdown(data, unsafe_allow_html=True)

    st.image('babouche.jpg', width=800)
    st.image('unicorn.gif', width= 500)
    st.write("Christopher Dubois [linkedin](https://www.google.fr)") 
    st.write("Elisa Cid [linkedin](https://www.google.fr)")
    st.write("Laurence Léon[linkedin](https://www.google.fr)")
    st.write("Valérie Nevo [linkedin](https://www.google.fr)")


if __name__ == "__main__":
    main()    