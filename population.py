def main():
    print("Population Growth Predictor")

    try:
        initial_population = int(input("Enter the initial number of organisms: "))
        growth_rate = float(input("Enter the growth rate (e.g., 2 for doubling): "))
        hours_per_growth = float(input("Enter the number of hours to achieve this rate: "))
        total_hours = float(input("Enter the total number of hours for growth: "))

        if initial_population <= 0 or growth_rate <= 0 or hours_per_growth <= 0 or total_hours < 0:
            print("Please enter positive values for all inputs.")
            return

        # calculate growth rate interval
        growth_cycles = int(total_hours // hours_per_growth)

        population = initial_population
        for _ in range(growth_cycles):
            population *= growth_rate

        print(f"\nPredicted population after {total_hours} hours: {int(population)} organisms")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
