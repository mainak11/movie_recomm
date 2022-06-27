# movie_recommendation-system


## Goal: Goal of this project is to recommend top 5 movies based on users movie search. They can search any movie and get top 5 similar kind of movie.
### •	I take a data set of approximate 16500 movies where 3 different languages are taken. 8000 Hindi,4500 Bengali and 4000 English movies are taken.
### •	Then I preprocess all the three datasets and fill and drop the null values and cancel all the noises for further procedure. 
### •	in this project the main problem is to calculate the difference between the movies. So we create vectors of the given movies and calculate the distance/similarity using cosine similarity.
### •	For this calculation first we create a table of ‘Tags’ where all the features of the movies are available like movie genre, actors, directors, producers, description etc. then we create vectors and calculate the cosine similarity between the movies using nltk and scikit-learn libraries. 
### •	we create a list of top 5 similar movies based on the users search and give an output of 5 movie names. And in this recommendation system we can select the language of the movie.
