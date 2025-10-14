def generate_payment_schedule(purchase_price):
    down_payment = 0.10 * purchase_price
    balance = purchase_price - down_payment
    monthly_payment = 0.05 * purchase_price
    annual_interest_rate = 0.12
    monthly_interest_rate = annual_interest_rate / 12

    print("\nTidBit Computer Store Payment Schedule")
    print(f"Purchase Price: ${purchase_price:,.2f}")
    print(f"Down Payment:   ${down_payment:,.2f}")
    print(f"Monthly Payment: ${monthly_payment:,.2f}\n")

    print("Month\tBalance\t\tInterest\tPrincipal\tPayment\t\tRemaining")
    print("----------------------------------------------------------------------")

    month = 1
    while balance > 0:
        interest = balance * monthly_interest_rate
        principal = monthly_payment - interest

        if principal > balance:
            principal = balance
            monthly_payment = interest + principal

        remaining_balance = balance - principal

        print(f"{month}\t${balance:,.2f}\t${interest:,.2f}\t\t${principal:,.2f}\t\t${monthly_payment:,.2f}\t${remaining_balance:,.2f}")

        balance = remaining_balance
        month += 1


def main():
    try:
        purchase_price = float(input("Enter the purchase price: $"))
        if purchase_price <= 0:
            print("Please enter a positive amount.")
            return

        generate_payment_schedule(purchase_price)

    except ValueError:
        print("Invalid input. Please enter a numeric value.")


if __name__ == "__main__":
    main()
