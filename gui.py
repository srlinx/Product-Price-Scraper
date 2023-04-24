import tkinter as tk
import tkinter.messagebox as messagebox
from scraper import get_lowest_price

def search():
    # Add warning message before scraping
    if not messagebox.askokcancel("Warning", "Web scraping can be illegal in certain circumstances. Do you want to continue?"):
        return
    
    product_name = entry.get()
    websites = [amazon_var.get(), flipkart_var.get(), ebay_var.get()]
    lowest_price = get_lowest_price(product_name, websites)
    result_label.config(text="Lowest Price: ${:.2f}".format(lowest_price))

def create_gui():
    root = tk.Tk()
    root.title("Price Scraper")

    main_frame = tk.Frame(root, padx=10, pady=10)
    main_frame.pack()

    # Product Name Entry
    product_name_frame = tk.Frame(main_frame)
    product_name_frame.pack(fill="x")
    tk.Label(product_name_frame, text="Product Name:").pack(side="left")
    global entry
    entry = tk.Entry(product_name_frame)
    entry.pack(side="right")

    # Website Checkboxes
    website_frame = tk.Frame(main_frame)
    website_frame.pack(fill="x")
    tk.Label(website_frame, text="Websites:").pack(side="left")
    global amazon_var, flipkart_var, ebay_var
    amazon_var = tk.BooleanVar()
    flipkart_var = tk.BooleanVar()
    ebay_var = tk.BooleanVar()
    tk.Checkbutton(website_frame, text="Amazon", variable=amazon_var).pack(side="left")
    tk.Checkbutton(website_frame, text="Flipkart", variable=flipkart_var).pack(side="left")
    tk.Checkbutton(website_frame, text="eBay", variable=ebay_var).pack(side="left")

    # Search Button
    search_button = tk.Button(main_frame, text="Search", command=search)
    search_button.pack()

    # Result Label
    global result_label
    result_label = tk.Label(main_frame, text="")
    result_label.pack()

    root.mainloop()
