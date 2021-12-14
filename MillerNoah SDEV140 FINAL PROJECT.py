#imports tkinter
import tkinter as tk

# Creates first window
window = tk.Tk()
window.title("Restaurant Ordering")
window.resizable(width=False, height=False)

# function to quit application
def delete():
    window.destroy()

# create the window that will display
# the total if the customer wants a meal
# meal will add 2 dollars
def create_window_meal():
    total_window = tk.Toplevel(window)
    global price
    price += 2
    total_label = tk.Label(total_window, text=("Your total is: $"))
    price_label = tk.Label(total_window, text=(float(price)))
    quit_button = tk.Button(total_window, command=delete, text="Quit")

    total_label.grid(row=0, column=0)
    price_label.grid(row=0, column=1)
    quit_button.grid(row=1, column=0, pady=10)

# create the window that will display
# the total if the customer does not want a meal
def create_window_no_meal():
    total_window = tk.Toplevel(window)
    total_label = tk.Label(total_window, text=("Your total is: $"))
    price_label = tk.Label(total_window, text=(float(price)))
    quit_button = tk.Button(total_window, command=delete, text="Quit")

    total_label.grid(row=0, column=0)
    price_label.grid(row=0, column=1)
    quit_button.grid(row=1, column=0, pady=10)

# brings up new window and adds food price to variable
# asks customer if they want a big mac meal
# includes yes button, no button, back button, and quit button
def ask_meal_bigmac():
    meal_window = tk.Toplevel(window)
    big_mac_price = 3.99
    global price
    price = float(big_mac_price)
    def back():
        meal_window.destroy()
    meal_label = tk.Label(meal_window, text=("Would you like to make that a meal for 2 extra dollars?"))
    yes_button = tk.Button(meal_window, text=("Yes"), command=create_window_meal)
    no_button = tk.Button(meal_window, text=("No"), command=create_window_no_meal)
    back_button = tk.Button(meal_window, command=back, text="Back")
    quit_button = tk.Button(meal_window, command=delete, text="Quit")

    meal_label.grid(row=0, pady=5)
    yes_button.grid(row=1, pady=5)
    no_button.grid(row=2, pady=5)
    back_button.grid(row=3, pady=5)
    quit_button.grid(row=4, pady=5)

# brings up new window and adds food price to variable
# asks a customer if they want a 2 cheeseburger meal
# includes yes button, no button, back button, and quit button
def ask_meal_twocheese():
    meal_window = tk.Toplevel(window)
    two_cheese_price = 2.00
    global price
    price = float(two_cheese_price)
    def back():
        meal_window.destroy()
    meal_label = tk.Label(meal_window, text=("Would you like to make that a meal for 2 extra dollars?"))
    yes_button = tk.Button(meal_window, text=("Yes"), command=create_window_meal)
    no_button = tk.Button(meal_window, text=("No"), command=create_window_no_meal)
    back_button = tk.Button(meal_window, command=back, text="Back")
    quit_button = tk.Button(meal_window, command=delete, text="Quit")

    meal_label.grid(row=0, pady=5)
    yes_button.grid(row=1, pady=5)
    no_button.grid(row=2, pady=5)
    back_button.grid(row=3, pady=5)
    quit_button.grid(row=4, pady=5)

# brings up new window and adds food price to variable
# ask a customer if they want a quarter pounder meal
# includes yes button, no button, back button, and quit button

def ask_meal_quarter():
    meal_window = tk.Toplevel(window)
    quarter_pounder_price = 3.79
    global price
    price = float(quarter_pounder_price)
    def back():
        meal_window.destroy()
    meal_label = tk.Label(meal_window, text=("Would you like to make that a meal for 2 extra dollars?"))
    yes_button = tk.Button(meal_window, text=("Yes"), command=create_window_meal)
    no_button = tk.Button(meal_window, text=("No"), command=create_window_no_meal)
    back_button = tk.Button(meal_window, command=back, text="Back")
    quit_button = tk.Button(meal_window, command=delete, text="Quit")

    meal_label.grid(row=0, pady=5)
    yes_button.grid(row=1, pady=5)
    no_button.grid(row=2, pady=5)
    back_button.grid(row=3, pady=5)
    quit_button.grid(row=4, pady=5)

# brings up new window and adds food price to variable
# asks a customer if they want a double quarter pounder meal
# includes yes button, no button, back button, and quit button
def ask_meal_double():
    meal_window = tk.Toplevel(window)
    double_quarter_price = 4.79
    global price
    price = float(double_quarter_price)
    def back():
        meal_window.destroy()
    meal_label = tk.Label(meal_window, text=("Would you like to make that a meal for 2 extra dollars?"))
    yes_button = tk.Button(meal_window, text=("Yes"), command=create_window_meal)
    no_button = tk.Button(meal_window, text=("No"), command=create_window_no_meal)
    back_button = tk.Button(meal_window, command=back, text="Back")
    quit_button = tk.Button(meal_window, command=delete, text="Quit")

    meal_label.grid(row=0, pady=5)
    yes_button.grid(row=1, pady=5)
    no_button.grid(row=2, pady=5)
    back_button.grid(row=3, pady=5)
    quit_button.grid(row=4, pady=5)

# label asking for the customer's order
label = tk.Label(text="Welcome, what would you like to order?")

# button options for food
button = tk.Button(text="Big Mac", command=ask_meal_bigmac)
button_two = tk.Button(text="2 Cheeseburgers", command=ask_meal_twocheese)
button_three = tk.Button(text="Quarter Pounder with Cheese", command=ask_meal_quarter)
button_four = tk.Button(text="Double Quarter Pounder with Cheese", command=ask_meal_double)
button_stop = tk.Button(text="Quit", command=delete)

label.grid(row=0, pady=5)
button.grid(row=1, pady=5)
button_two.grid(row=2, pady=5)
button_three.grid(row=3, pady=5)
button_four.grid(row=4, pady=5)
button_stop.grid(row=5, pady=5)
window.mainloop()
