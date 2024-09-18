import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import io
import base64

df = None

def load_csv(file):
    global df
    df = pd.read_csv(file)
    return df.columns.to_list()

def scatterplot(x_col, y_col):
    global df
    plt.figure(figsize=(10, 6))
    plt.scatter(x=df[x_col], y=df[y_col])
    plt.title(f"{x_col} vs. {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    return plot_url

def barplot(x_col, y_col):
    global df
    plt.figure(figsize=(10, 6))
    df.groupby(x_col)[y_col].mean().plot(kind='bar')
    plt.title(f"{x_col} vs. Mean {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(f"Mean {y_col}")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    return plot_url
