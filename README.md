💻 Laptop Price Predictor

A machine learning project to predict laptop prices based on specifications such as brand, RAM, storage, CPU, GPU, operating system, and more.

# 💻 **Laptop Price Predictor**

A machine learning project that predicts laptop prices based on their specifications using various regression models and an interactive Streamlit web app.

---

## 🚀 Features
- Predict laptop prices instantly with a trained ML model.  
- Interactive **Streamlit web app** for real-time predictions.  
- Preprocessed dataset with feature engineering.  
- Multiple ML algorithms compared (**Linear Regression, Random Forest, XGBoost**).  
- Best model saved and deployed in the app.  

---

## 📁 Project Structure


📂 Project Structure
```bash
laptop-price-predictor/
│── data/
│   └── laptop.csv              # Dataset used for training
│── notebooks/
│   └── laptop_price_predictor.ipynb   # Jupyter notebook with experiments
│── app.py                      # Streamlit web app for predictions
│── check_delete_it_later.py    # Helper / test script
│── requirements.txt            # Dependencies
│── README.md                   # Project documentation
│── LICENSE                     # License file
│── .gitignore                  # Ignored files
```


## ⚡ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Sharruk/sentiment-analysis.git
   cd sentiment-analysis


2. Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
pip install -r requirements.txt
```
3. Run the Streamlit app:
```bash
streamlit run app.py
```

## 📊 Model Performance  

We trained and evaluated multiple machine learning models on the **Laptop Specifications Dataset (`laptop.csv`)**.  

| Model              | MAE (↓)   | RMSE (↓)  | R² (↑)  |  
|--------------------|-----------|-----------|---------|  
| Linear Regression  | 13,714.50 | 19,844.93 | 0.73 |  
| Random Forest      | 12,107.70 | 19,222.48 | 0.74 |  
| XGBoost            | 11,990.39 | 19,521.70 | 0.74 |  

✅ **Best Model: RandomForest**  
## 📊 Model Performance  

```python
{'MAE': 12107.700871106854, 'RMSE': 19222.476313127947, 'R2': 0.7437349716327546}
```
Input: Brand = Dell, RAM = 16GB, CPU = Intel i7, Storage = 512GB SSD

Output: ₹85,000 (approx.)



