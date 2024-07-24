# Pneumonia Detection

Welcome to the Pneumonia Detection project! This streamlit application is designed for pneumonia detection using X-ray images. Here's a quick overview of the key files:

## Project Overview

- **Objective:** Detect pneumonia in X-ray images and classify them into three categories: Normal, Virus, Bacterial Pneumonia.

- **Files:**
  - `Data_ingest.py`: Python script for data ingestion.
  - `Data_process.py`: Python script for data processing.
  - `Prediction.py`: Python script for making predictions.
  - `app.py`: Main Streamlit application file.
  - `pipeline.py`: Python script for the data processing pipeline.
  - `requirements.txt`: List of project dependencies.
  - `images/`: Folder containing X-ray images.
  - `static/`: Folder for static assets in the Streamlit app.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/vijaytakbhate2002/pneumonia-detection.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

4. Upload X-ray images to get predictions for Normal, Virus, and Bacterial Pneumonia.

## Contributing

We welcome contributions! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
