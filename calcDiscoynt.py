def calculate_discount(price, discount_percent):
#    This function calculates the final price after applying a discount.
#    If the discount percentage is 20% or more, it applies the discount.
    if discount_percent >= 20:

#Calculate the discount amount
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
#If the discount percentage is less than 20%, it returns the original price
    else:
        return price

# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if discount_percentage >= 20:
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {original_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")