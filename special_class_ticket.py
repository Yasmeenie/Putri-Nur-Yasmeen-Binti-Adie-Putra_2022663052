import tkinter as tk
import mysql.connector

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="special_class_ticket"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()


# Function to handle the calculation and database saving
def collect_data():
    user_name = user_name_entry.get()
    user_phone_number = int(user_phone_number_entry.get())
    user_address = user_address_entry.get()
    user_age = user_age_label.get()
    special_class_type = class_type_var.get()
    ticket = int(ticket_package_entry.get())
    
    #  the price below is to defined the value from your selections
    prices = {
    "Special Class A": 200,
    "Special Class M": 150,
    "Special Class C": 100,
}

    # Calculate the total price.
    total_price = prices[special_class_type] * int(ticket_package_entry.get())
    
    # To insert your Data to your database.
    sql = "INSERT INTO order_ticket (User_Name, User_Phone_Number, User_Address, User_Age, Special_Class_Type, Ticket, Total_Price) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (user_name, user_phone_number, user_address, user_age, special_class_type, ticket, total_price)
    mycursor.execute(sql, val)
    mydb.commit()

    
    # To print back the output.
    output_label.config(text=f"Congratulation! Now You Can Join: {special_class_type}, Ticket: {ticket}, Total Price: RM{total_price}", bg="light blue", font=("Rockwell Condensed",10, "bold"))


# Main Window
root = tk.Tk()
root.title("Purchase Special Class Ticket")
root.geometry('500x700')
root.configure(bg="light blue")

# Page Title
label = tk.Label(root, text="HELLO ^-^ COME JOIN US",bg="light blue", font=("Showcard Gothic",15, "bold",))
label.pack(ipadx=10, ipady=10)


# Prices List by using textbox
prices_text = tk.Text(root, bd=3, height=10, width=45)
prices_text.pack(pady=5) 


# The defined list by using pricebox
prices_text.insert(tk.END, "Special Class and Prices:\n\n")
prices_text.insert(tk.END, "Special Class A: Art Class \nPrice: RM200\n\n")
prices_text.insert(tk.END, "Special Class M: Music Class \nPrice: RM150\n\n")
prices_text.insert(tk.END, "Special Class C: Chess Class \nPrice: RM100\n\n")
prices_text.configure(state='disabled')


# Create name entry
user_name_label = tk.Label(root, text="Name:",bg="light blue", font=("Rockwell Condensed",13, "bold"))
user_name_entry = tk.Entry(root, bd=3)
user_name_label.pack(pady=5)
user_name_entry.pack(pady=5)

# Create phone entry
user_phone_number_label = tk.Label(root, text="Phone Number:", bg="light blue", font=("Rockwell Condensed",13, "bold"))
user_phone_number_entry = tk.Entry(root, bd=3)
user_phone_number_label.pack(pady=5)
user_phone_number_entry.pack(pady=5)

# Create address entry
user_address_label = tk.Label(root, text="Address:",bg="light blue", font=("Rockwell Condensed",13, "bold"))
user_address_entry = tk.Entry(root, bd=3)
user_address_label.pack(pady=5)
user_address_entry.pack(pady=5)

# Create age entry
user_age_label = tk.StringVar(root)
user_age_label.set("Choose Your Age")  # Default value before your selection
trip_dropdown = tk.OptionMenu(root, user_age_label, "7-20 age", "21-40 age", "41-60 age")
trip_dropdown.pack(pady=5)

# Special Class Type Dropdown
class_type_var = tk.StringVar(root)
class_type_var.set("Choose Your Class")  # Default value before your selection
trip_dropdown = tk.OptionMenu(root, class_type_var, "Special Class A", "Special Class M", "Special Class C")
trip_dropdown.pack(pady=5)


# Packs Entry
ticket_package_label = tk.Label(root, text="How many ticket do you need:", bg="light blue", font=("Rockwell Condensed",13, "bold"))
ticket_package_label.pack()
ticket_package_entry = tk.Entry(root)
ticket_package_entry.pack()

# Save Button
save_button = tk.Button(root, text="Calculate Total", bg="light blue", font=("Rockwell Condensed",13, "bold"), command=collect_data)
save_button.pack(pady=5)

# Output Label & result
label = tk.Label(root, text="Ticket Price:", bg="light blue", font=("Rockwell Condensed",13, "bold"))
label.pack(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.pack()


root.mainloop()













