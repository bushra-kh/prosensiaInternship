import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean(csv_file):
    df = pd.read_csv(csv_file)
    df = df.dropna()
    return df

def plot_line(df, x, y, filename):
    plt.figure()
    plt.plot(df[x], df[y], marker='o')
    plt.title(f"{y} over {x}")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def plot_bar(df, x, y, filename):
    plt.figure()
    plt.bar(df[x], df[y])
    plt.title(f"{y} by {x}")
    plt.xlabel(x)
    plt.ylabel(y)
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def plot_pie(df, labels, values, filename):
    plt.figure()
    plt.pie(df[values], labels=df[labels], autopct='%1.1f%%')
    plt.title(f"{values} distribution")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def plot_heatmap(df, filename):
    plt.figure(figsize=(8,6))
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def summary_report(df, filename):
    with open(filename, "w") as f:
        f.write("Summary Report\n")
        f.write("-----------------\n")
        f.write(str(df.describe()))
        f.write("\n\nColumns:\n")
        f.write(", ".join(df.columns))

def main():
    df = load_and_clean("sales.csv")
    plot_line(df, "Month", "Revenue", "Line_Chart.png")
    plot_bar(df, "Product", "Sales", "Bar_Chart.png")
    plot_pie(df, "Product", "MarketShare", "Pie_Chart.png")
    plot_heatmap(df, "Heatmap.png")
    summary_report(df, "Summary_Report.txt")
    print("✅ All charts and summary report generated.")

if __name__ == "__main__":
    main()