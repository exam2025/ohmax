import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

def main():
    st.title("Iris Flower Classification")
    st.write("This app predicts the species of an iris flower based on its measurements.")

    @st.cache_data
    def load_data():
        iris = datasets.load_iris()
        X = pd.DataFrame(iris.data, columns=iris.feature_names)
        y = iris.target
        return X, y,iris

    X, y,iris = load_data()
    model = KNeighborsClassifier()

    model.fit(X, y)

    sepal_length = st.slider("Sepal Length", float(X['sepal length (cm)'].min()), float(X['sepal length (cm)'].max()))
    sepal_width = st.slider("Sepal Width", float(X['sepal width (cm)'].min()), float(X['sepal width (cm)'].max()))
    petal_length = st.slider("Petal Length", float(X['petal length (cm)'].min()), float(X['petal length (cm)'].max()))
    petal_width = st.slider("Petal Width", float(X['petal width (cm)'].min()), float(X['petal width (cm)'].max()))

    features = [[sepal_length, sepal_width, petal_length, petal_width]]

    prediction = model.predict(features)

    species = iris.target_names[prediction[0]]

    st.write("The predicted species is:", species)

if __name__ == "__main__":
    main()
