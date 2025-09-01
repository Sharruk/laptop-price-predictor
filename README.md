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

⚙️ Installation

Clone the repository and install dependencies:
```bash
git clone https://github.com/Sharruk/laptop-price-predictor.git
cd laptop-price-predictor
pip install -r requirements.txt
```

📊 Usage
1. Run the Jupyter Notebook

For training and testing models:

jupyter notebook notebooks/laptop_price_predictor.ipynb

2. Run the Web App

To launch the Streamlit app:

streamlit run app.py


Then open your browser at http://localhost:8501/.

🧠 Model

Preprocessing: Label encoding, scaling, feature engineering

Algorithms tested: Linear Regression, Ridge, Random Forest, Gradient Boosting

Best performing model saved and used in app.py

📈 Example Prediction

Input: Brand = Dell, RAM = 16GB, CPU = Intel i7, Storage = 512GB SSD

Output: ₹85,000 (approx.)
