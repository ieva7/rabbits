import pandas as pd
import streamlit as st

if __name__ == "__main__":

    rabbits = pd.read_csv("./data/rabbits.csv")

    print(rabbits.shape)