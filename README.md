# Aspect-based Sentiment Analysis for Vietnamese Fashion Comments

This repository contains the implementation of aspect-based sentiment analysis (ABSA) for Vietnamese fashion product comments. The project explores various machine learning and deep learning approaches to aspect-based sentiment analysis, utilizing both traditional machine learning models and advanced neural network models.

## 📄 Documentation

- **Report.pdf**: Comprehensive project report with detailed methodology, results, and conclusions
## 📁 Project Structure

```
.
├── Report.pdf                  # Comprehensive project report
├── crawl_data.py               # Python script for data crawling
├── crawl_data.ipynb            # Jupyter notebook for data crawling with visualizations
├── EDA.ipynb                   # Exploratory Data Analysis notebook
├── machine-learning-absa.ipynb # Traditional ML models implementation
├── multitask-absa-bigru-conv1d.ipynb # Deep learning models implementation
├── phobert-embedding.ipynb     # PhoBERT embedding exploration
├── absa-demo.ipynb             # Interactive demonstration notebook
├── fashion_comment_data.csv    # Raw crawled data
├── dictionary_edit.json        # Dictionary for text processing
├── requirements.txt            # Project dependencies
├── LICENSE                     # MIT License
│
├── dataset/                    # Processed dataset directory
├── embeddings/                 # Pre-trained embeddings
└── trained_models/             # Saved trained models
```

## 🔍 Key Components

### Data Collection
- **crawl_data.py**: Python script for automated data collection from TIKI platform
- **crawl_data.ipynb**: Interactive version with additional visualizations and analysis

### Data Analysis
- **EDA.ipynb**: Exploratory Data Analysis covering:
  - Data distribution analysis
  - Aspect and sentiment class distribution
  - Text normalization and cleaning
  - Data preprocessing for model training

### Model Implementation
- **machine-learning-absa.ipynb**: Traditional machine learning approaches:
  - Random Forest for aspect detection
  - Support Vector Machine (SVM) for sentiment analysis
  - Feature engineering and model evaluation

- **multitask-absa-bigru-conv1d.ipynb**: Deep learning approaches:
  - BiGRU architecture for sequence modeling
  - Conv1D architecture for feature extraction
  - Multitask learning implementation

- **phobert-embedding.ipynb**: PhoBERT embedding exploration:
  - Pre-trained model implementation
  - Embedding visualization
  - Performance comparison

### Demo
- **absa-demo.ipynb**: Interactive demonstration of:
  - Real-time aspect detection
  - Sentiment analysis
  - Model inference pipeline

## 🚀 Getting Started

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/imdhiep/Aspect-based-Sentiment-Analysis-for-Vietnamese-Reviews-about-Fashion-Product-on-E-commerce-Websites.git
    cd Aspect-based-Sentiment-Analysis-for-Vietnamese-Reviews-about-Fashion-Product-on-E-commerce-Websites
    ```

2. **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

Follow these steps to run the complete analysis pipeline:

1. **Data Collection**:
   - Run `crawl_data.py` or `crawl_data.ipynb` to collect Vietnamese fashion product comments
   - The data will be saved in `fashion_comment_data.csv`

2. **Data Analysis and Preparation**:
   - Use `EDA.ipynb` for data exploration and preprocessing
   - This step includes text normalization and cleaning

3. **Model Training**:
   - For traditional ML: Run `machine-learning-absa.ipynb`
   - For deep learning: Run `multitask-absa-bigru-conv1d.ipynb`
   - For embedding exploration: Run `phobert-embedding.ipynb`

4. **Model Testing**:
   - Use `absa-demo.ipynb` for real-time predictions
   - Test with your own Vietnamese text inputs

## 📊 Models

### Machine Learning Models
- **Random Forest**
  - Used for aspect detection
  - Handles non-linear relationships
  - Robust to overfitting

- **Support Vector Machine (SVM)**
  - Used for sentiment analysis
  - Effective for high-dimensional data
  - Good generalization performance

### Deep Learning Models
- **BiGRU (Bidirectional Gated Recurrent Unit)**
  - Captures bidirectional context
  - Effective for sequence modeling
  - Handles variable-length inputs

- **Conv1D (1D Convolutional Neural Network)**
  - Extracts local features
  - Parallel processing capability
  - Efficient for text classification

### Embeddings
- **TF-IDF**
  - Traditional text representation
  - Computationally efficient
  - Good baseline performance

- **PhoBERT**
  - Pre-trained Vietnamese language model
  - Captures semantic relationships
  - State-of-the-art performance

## 📈 Results

### Machine Learning Performance
- Random Forest and SVM provide solid baseline performance
- Good interpretability and training speed
- Suitable for smaller datasets

### Deep Learning Performance
- BiGRU and Conv1D models show superior performance
- Better at capturing context and nuances
- PhoBERT embeddings significantly improve accuracy
- Effective for complex Vietnamese text patterns

## 🖥️ Demo

The `absa-demo.ipynb` notebook provides an interactive interface to:
- Input Vietnamese text
- Detect product aspects
- Analyze sentiment for each aspect
- Visualize results

## ⚙️ Requirements

- Python 3.x
- CUDA-capable GPU (recommended for deep learning models)
- Required libraries (see `requirements.txt`):
  - Data processing: pandas, numpy
  - Deep learning: torch, tensorflow
  - NLP: transformers, pyvi
  - ML: scikit-learn
  - Visualization: matplotlib
  - Web scraping: selenium, undetected-chromedriver

## 📝 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

```
