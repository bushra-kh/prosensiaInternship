import pandas as pd
import matplotlib.pyplot as plt
import logging
import os

logging.basicConfig(filename="log.txt", level=logging.ERROR, format="%(asctime)s %(levelname)s:%(message)s")

class ReportError(Exception):
    pass

def load_data(filename):
    try:
        if filename.endswith('.csv'):
            df = pd.read_csv(filename)
        elif filename.endswith('.xlsx'):
            df = pd.read_excel(filename, engine='openpyxl')
        else:
            raise ReportError("Unsupported file type. Use .csv or .xlsx")
        return df
    except Exception as e:
        logging.error(f"Failed to load data: {e}")
        raise ReportError(f"Error loading file: {e}")

def calculate_stats(df):
    try:
        df['Revenue'] = df['Units Sold'] * df['Unit Price']
        summary = df.groupby('Product')['Revenue'].sum().reset_index()
        total_revenue = summary['Revenue'].sum()
        top_product_row = summary.loc[summary['Revenue'].idxmax()]
        top_product = top_product_row['Product']
        return summary, total_revenue, top_product
    except Exception as e:
        logging.error(f"Failed to calculate stats: {e}")
        raise ReportError(f"Error calculating stats: {e}")

def save_report(summary, total_revenue, top_product, filename="report.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("📊 Sales Summary\n")
            for _, row in summary.iterrows():
                f.write(f"Product: {row['Product']} – Revenue: {int(row['Revenue'])}\n")
            f.write(f"\n🔸 Total Revenue: {int(total_revenue)}\n")
            f.write(f"🔸 Top Product: {top_product}\n")
    except Exception as e:
        logging.error(f"Failed to save report: {e}")
        raise ReportError(f"Error saving report: {e}")

def plot_bar_chart(summary, filename="sales_chart.png"):
    try:
        plt.figure(figsize=(7,4))
        plt.bar(summary['Product'], summary['Revenue'], color='skyblue')
        plt.title("Revenue by Product")
        plt.xlabel("Product")
        plt.ylabel("Revenue")
        plt.tight_layout()
        plt.savefig(filename)
        plt.close()
    except Exception as e:
        logging.error(f"Failed to plot bar chart: {e}")
        raise ReportError(f"Error plotting chart: {e}")

def main():
    try:
        user_file = input("Enter sales data filename (.csv or .xlsx): ").strip()
        if not os.path.exists(user_file):
            raise ReportError("File does not exist.")
        df = load_data(user_file)
        summary, total_revenue, top_product = calculate_stats(df)
        save_report(summary, total_revenue, top_product)
        plot_bar_chart(summary)
        print("Report and chart generated successfully.")
    except ReportError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()