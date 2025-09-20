### Olympics Medals Prediction

This project uses machine learning to predict the number of Olympic medals a country will win in a given year. By analyzing historical performance data, a linear regression model is built to forecast future medal counts.

-----

### Project Structure

  * `Olympics.ipynb`: A Jupyter Notebook containing all the code for data cleaning, analysis, model training, and evaluation.
  * `teams.csv`: The dataset used for the analysis, containing historical Olympic data for various countries.

-----

### Key Features

  * **Data Preparation**: The project cleans and processes raw Olympic data, handling missing values and selecting key features for the model.
  * **Exploratory Data Analysis (EDA)**: Visualizations are used to identify strong correlations, revealing that the number of athletes and a country's previous medal count are the strongest predictors of future success.
  * **Machine Learning Model**: A **Linear Regression** model from the **scikit-learn** library is trained to predict medal counts.
  * **Model Evaluation**: The model's performance is evaluated using **Mean Absolute Error (MAE)**, providing a clear measure of prediction accuracy. The analysis also includes team-specific error evaluations to highlight the model's strengths and weaknesses.

-----

### Getting Started

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/saksham-v25/Olympics.git
    ```
2.  **Navigate to the project directory**:
    ```bash
    cd Olympics
    ```
3.  **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
4.  **Install the required libraries**:
    ```bash
    pip install pandas scikit-learn seaborn jupyter
    ```
5.  **Run the Jupyter Notebook**:
    ```bash
    jupyter notebook Olympics.ipynb
    ```


