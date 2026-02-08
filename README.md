# Student Performance Prediction System

## Overview
This project is a comprehensive Machine Learning application designed to predict student performance based on various demographic and socioeconomic factors. By analyzing data such as gender, race/ethnicity, parental level of education, lunch type, and test preparation courses, the system provides insights into likely exam outcomes.

The application features a user-friendly web interface built with **Flask**, allowing users to input data and receive instant predictions. The core machine learning pipeline is built using **Scikit-Learn**, **Pandas**, and **Numpy**, ensuring robust data processing and accurate model performance.

## Features
-   **Data Ingestion & Transformation**: Automated pipelines for handling data loading and preprocessing (handling missing values, encoding categorical variables, scaling).
-   **Machine Learning Model**: Utilizes ensemble methods (like Random Forest, Gradient Boosting, etc.) to achieve high prediction accuracy.
-   **Web Interface**: A clean, responsive HTML/CSS frontend served by Flask for easy user interaction.
-   **Modular Codebase**: Organized into clear components (Data Ingestion, Transformation, Model Training) for maintainability and scalability.

## Tech Stack
-   **Frontend**: HTML, CSS
-   **Backend**: Python, Flask
-   **Machine Learning**: Scikit-Learn, Pandas, Numpy, CatBoost, XGBoost
-   **Deployment**: Ready for deployment on cloud platforms (AWS, Azure, Render, etc.)

## Installation

### Prerequisites
-   Python 3.8+
-   Pip

### Steps to Run Locally

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/DEEPAK-317/Student-Performance-Prediction-System.git
    cd Student-Performance-Prediction-System
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment**
    -   **Windows**:
        ```bash
        .\venv\Scripts\activate
        ```
    -   **macOS/Linux**:
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Application**
    ```bash
    python app.py
    ```

6.  **Access the App**
    Open your browser and navigate to `http://127.0.0.1:5000/`.

## Usage
1.  Go to the home page.
2.  Click on "Predict your data" or navigable links to the prediction form.
3.  Fill in the student details (Gender, Ethnicity, etc.).
4.  Submit the form to see the predicted math score.

## Project Structure
```
├── artifacts/          # Stores generated models and preprocessors
├── notebook/           # Jupyter notebooks for EDA and model experimentation
├── src/                # Source code for the ML pipeline
│   ├── components/     # Data ingestion, transformation, and model training modules
│   ├── pipeline/       # Prediction and training pipelines
│   ├── utils.py        # Utility functions
│   ├── logger.py       # Logging configuration
│   └── exception.py    # Custom exception handling
├── templates/          # HTML templates for the web app
├── app.py              # Main Flask application entry point
├── requirements.txt    # Project dependencies
├── setup.py            # Package setup script
└── README.md           # Project documentation
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.