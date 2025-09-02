💻 Laptop Price Predictor

A machine learning project to predict laptop prices based on specifications such as brand, RAM, storage, CPU, GPU, operating system, and more.

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

🧠 Model

Preprocessing: Label encoding, scaling, feature engineering

Algorithms tested: Linear Regression, Ridge, Random Forest, Gradient Boosting

Best performing model saved and used in app.py

📈 Example Prediction

Input: Brand = Dell, RAM = 16GB, CPU = Intel i7, Storage = 512GB SSD

Output: ₹85,000 (approx.)

