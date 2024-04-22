import tkinter as tk
from tkinter import messagebox, scrolledtext
from functools import partial
import yfinance as yf
import matplotlib.pyplot as plt
from pandas import DataFrame

def get_stock_data(ticker, start_date, end_date):
    # Fetching historical stock data from Yahoo Finance
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    return data

def analyze_stock(ticker, start_date, end_date):
    data = get_stock_data(ticker, start_date, end_date)
    
    if data.empty:
        messagebox.showerror("Error", f"No data found for {ticker}")
        return None
    
    # Perform analysis on historical data...
    # For demonstration purposes, let's visualize the closing prices
    plt.plot(data.index, data['Close'])
    plt.title(f"Historical Closing Prices for {ticker}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    
    return data

def on_analyze_button_click(ticker_entry, start_date_entry, end_date_entry):
    ticker = ticker_entry.get()
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    
    data = analyze_stock(ticker, start_date, end_date)
    if data is not None:
        display_data_window(data)

def display_data_window(data):
    # Create a new window to display textual data
    data_window = tk.Toplevel()
    data_window.title("Stock Data")
    
    # Create a scrolled text area to display the data
    text_area = scrolledtext.ScrolledText(data_window, wrap=tk.WORD, width=50, height=20)
    text_area.insert(tk.END, data.to_string())
    text_area.pack()
    
    # Show the new window
    plt.show()

def main():
    # Create the main window
    window = tk.Tk()
    window.title("Stock Analysis")
    
    # Create and place widgets
    label_ticker = tk.Label(window, text="Enter the ticker symbol of the stock:")
    label_ticker.pack()
    ticker_entry = tk.Entry(window)
    ticker_entry.pack()
    
    label_start_date = tk.Label(window, text="Enter the start date (YYYY-MM-DD):")
    label_start_date.pack()
    start_date_entry = tk.Entry(window)
    start_date_entry.pack()

    label_end_date = tk.Label(window, text="Enter the end date (YYYY-MM-DD):")
    label_end_date.pack()
    end_date_entry = tk.Entry(window)
    end_date_entry.pack()
    
    analyze_button = tk.Button(window, text="Analyze", command=partial(on_analyze_button_click, ticker_entry, start_date_entry, end_date_entry))
    analyze_button.pack()
    
    # Run the main event loop
    window.mainloop()

if __name__ == "__main__":
    main()
