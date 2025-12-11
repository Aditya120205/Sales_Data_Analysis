# 📊 Sales Data Analysis Dashboard

An interactive **Sales Analysis Dashboard** built using **Streamlit**, **Pandas**, and **Plotly**.  
This dashboard allows users to explore sales performance, revenue trends, product performance, and regional comparisons using multiple visualizations.

---

## 🚀 Features

### ✅ **Data Cleaning & Feature Engineering**
- Standardizes column names  
- Converts date column into datetime  
- Calculates:
  - **Total Cost**
  - **Profit**
  - **Revenue**
  - **Month** (for trend analysis)

---

## 📌 **Dashboard Includes 8 Visualizations**

### **1. Monthly Sales & Profit Trend (Line Chart)**
Shows monthly performance using Sales Amount and Profit.

### **2. Revenue by Product Category (Bar Plot)**  
Visual comparison of total revenue for each category.

### **3. Region-wise Revenue Share (Pie Chart)**  
Displays how revenue is distributed across different regions.

### **4. Top 5 Products by Revenue (Bar Plot)**  
Identifies your highest-earning products.

### **5. Correlation Heatmap**  
Shows statistical relationships between numeric metrics like Sales, Profit, Price, etc.

### **6. Revenue Distribution (Histogram)**  
Visualizes the spread of revenue across transactions.

### **7. Units Sold vs Revenue (Scatter Plot)**  
Understands how quantity sold impacts revenue.

### **8. Daily Revenue Trend (Line Chart)**  
Breakdown of revenue on a day-by-day basis.

---

## 🎛️ **Filters**

Use the sidebar to filter data by:

- **Region**
- **Product Category**

All charts update dynamically based on selected filters.

---

## 📂 Project Structure

Sales_Data_Analysis/
│── main.py

│── sales_data.csv

│── requirements.txt (optional)

│── README.md


---

## 🛠️ How to Run the Dashboard

### 1. Install required libraries
```bash
pip install streamlit pandas plotly

2. Place your sales_data.csv

Keep it in the same folder as main.py.

3. Run the Streamlit app
streamlit run main.py


## 🧮 Columns Required in `sales_data.csv`

Your dataset must include the following columns:

| Column Name       | Description                |
|-------------------|----------------------------|
| Sale_Date         | Date of sale               |
| Region            | Region name                |
| Product_Category  | Product category           |
| Product_ID        | Product identifier         |
| Quantity_Sold     | Units sold                 |
| Unit_Cost         | Cost per unit              |
| Unit_Price        | Selling price per unit     |
| Sales_Amount      | Total sale value           |

---

## 📸 Screenshot (Optional)

_Add a screenshot of your dashboard here if you want._

---

## 🤝 Contributing

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you would like to improve.

---

## 📝 License

This project is for learning and personal use.  
Feel free to modify and build on top of it.


