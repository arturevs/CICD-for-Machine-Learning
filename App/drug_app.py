import gradio as gr
import skops.io as sio

pipe = sio.load("./Model/drug_pipeline.skops", trusted=True)


def predict_drug(age, sex, blood_pressure, cholesterol, na_to_k_ratio):
    """Predict drug based on patient features.

    Args:
        age (int): Age of patient
        sex (int): Sex of patient (0 for female, 1 for male)
        blood_pressure (int): Blood pressure level
        cholesterol (int): Cholesterol level
        na_to_k_ratio (float): Ratio of sodium to potassium in blood

    Returns:
        str: Predicted drug label
    """
    features = [age, sex, blood_pressure, cholesterol, na_to_k_ratio]
    predicted_drug = pipe.predict([features])[0]

    label = f"Predicted Drug: {predicted_drug}"
    return label


inputs = [
    gr.Slider(15, 74, step=1, label="Age"),
    gr.Radio(["M", "F"], label="Sex"),
    gr.Radio(["HIGH", "LOW", "NORMAL"], label="Blood Pressure"),
    gr.Radio(["HIGH", "NORMAL"], label="Cholesterol"),
    gr.Slider(6.2, 38.2, step=0.1, label="Na_to_K"),
]
outputs = [gr.Label(num_top_classes=5)]

examples = [
    [30, "M", "HIGH", "NORMAL", 15.4],
    [35, "F", "LOW", "NORMAL", 8],
    [50, "M", "HIGH", "HIGH", 34],
]


title = "Drug Classification"
description = "Enter the details to correctly identify Drug type?"
article = """<center>

[![GitHub Repo stars](https://img.shields.io/github/stars/kingabzpro/CICD-for-Machine-Learning)](https://github.com/kingabzpro/CICD-for-Machine-Learning)[![Follow me on HF](https://huggingface.co/datasets/huggingface/badges/resolve/main/follow-me-on-HF-md.svg)](https://huggingface.co/kingabzpro)

**This app is a part of the Beginner's Guide to CI/CD for Machine Learning.**

**It teaches how to automate training, evaluation, and deployment of models to Hugging Face using GitHub Actions.**

[![DataCamp](https://img.shields.io/badge/Datacamp-05192D?style=for-the-badge&logo=datacamp&logoColor=65FF8F)](https://www.datacamp.com/portfolio/kingabzpro)

</center>"""

gr.Interface(
    fn=predict_drug,
    inputs=inputs,
    outputs=outputs,
    examples=examples,
    title=title,
    description=description,
    article=article,
    theme=gr.themes.Soft(),
).launch()
