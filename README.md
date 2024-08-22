# Music Recommendation System

This project implements a music recommendation system using Streamlit, leveraging a Spotify dataset to suggest similar songs based on user input. The system calculates song similarities using cosine similarity and provides recommendations in real-time.

![Music Recommendation System](Image.png)

## Project Overview

The recommendation system uses the Spotify dataset to build a user-item matrix and compute item similarities. Users can select a song from the provided list, and the system will recommend similar songs based on the selected song's popularity and attributes.

## Files

- `Spotify-2000.csv`: The dataset used for the recommendation system.
- `app.py`: The main Streamlit application file that implements the recommendation system.
- `Music_Recommendation_System.ipynb`: A Jupyter notebook version of the same recommendation system code.

## Requirements

To run this project, you need to have the following Python libraries installed:

- `streamlit`
- `pandas`
- `numpy`
- `scikit-learn`
- `scipy`

You can install the required libraries using pip:

## Overview

This project involves creating a music recommendation system using a Spotify dataset. The system utilizes a collaborative filtering approach to recommend songs based on their similarity. The key steps are data loading and preprocessing, matrix construction, similarity calculation, and recommendation retrieval.

## How It Works

### 1. Data Loading and Preprocessing

- **Dataset:** The dataset is loaded from `Spotify-2000.csv`.
- **Cleaning:** Duplicate entries and missing values are removed to ensure data quality.
- **Encoding:** Categorical variables (Artist and Title) are encoded into numerical features for processing.

### 2. Matrix Construction

- **User-Item Matrix:** A matrix is constructed using the `Artist` and `Title` columns, with `Popularity` as the value.
- **Sparse Matrix:** This matrix is converted into a sparse matrix format to improve computational efficiency.

### 3. Similarity Calculation

- **Cosine Similarity:** Item-item similarity is computed using cosine similarity.
- **Similarity Matrix:** A similarity matrix is generated to facilitate song recommendations.

### 4. Recommendation Function

- **Retrieval:** Given a song title, the system retrieves and sorts similar songs based on the similarity matrix.
- **Display:** The top recommendations are shown in the Streamlit app.

```bash
pip install streamlit pandas numpy scikit-learn scipy
