# SOM
Train SOM on custom images of Bewerage size 110. 
# Self-Organizing Map (SOM) Project

## Project Overview
This project demonstrates the use of **Self-Organizing Maps (SOMs)** for **unsupervised learning**. SOMs are neural networks used to **cluster and visualize high-dimensional data** in a 2D map.

The goal of this project is to:
- Explore **data patterns** without labels.
- Visualize **clusters and relationships** in high-dimensional data.
- Gain a hands-on understanding of **unsupervised learning techniques**.

---
## Data Explanation
The dataset used in this project was prepared as follows:

1. **Collect Data**  
   - Gathered raw data from relevant sources (e.g., experiments, sensors, or any domain-specific dataset).
   - Each data point contains **200 features** (columns).

2. **Convert Data to CSV Format**  
   - Raw data was cleaned and structured into **rows and columns**.
   - Saved as `data.csv` to make it easy to load in Python.
   - Example of CSV structure (first 3 rows):
     ```
     feature1,feature2,...,feature200
     0.12,0.34,...,0.56
     0.78,0.11,...,0.22
     0.45,0.67,...,0.89
     ```

3. **Load Data in Python**  
   - Use `pandas` or `numpy` to read the CSV file:
   ```python
   import pandas as pd

   data = pd.read_csv('data.csv').values  # shape: (110, 200)

## Features
- Train a SOM on your dataset (`shape: 2020 x 200`).
- Generate a **U-Matrix (distance map)** to visualize clusters.
- Map data points to neurons to see how inputs are organized.
- Analyze cluster structures using **hit maps**.

---

## Getting Started

### Prerequisites
- Python 3.8+
- Libraries:
```bash
pip install numpy matplotlib minisom

****Usage****

Import necessary libraries and load your dataset.

Initialize the SOM:

from minisom import MiniSom

som = MiniSom(x=20, y=20, input_len=200, sigma=1.0, learning_rate=0.5)

**Train the SOM:**

som.random_weights_init(data)
som.train_random(data, num_iterations=1000)

**How it Works**

SOM initializes a 2D grid of neurons with random weights.

Each input vector finds its Best Matching Unit (BMU).

BMU and neighbors update their weights to better match the input.

After training, similar inputs cluster together on the map.
