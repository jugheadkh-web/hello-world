def generate_salary_schedule(starting_salary, percentage_increase, number_of_years):
    print("Year\tSalary")
    print("---------------------")
    current_salary = starting_salary

    for year in range(1, number_of_years + 1):
        print(f"{year}\t${current_salary:,.2f}")
        current_salary += current_salary * (percentage_increase / 100)


def main():
    try:
        starting_salary = float(input("Enter the starting salary: "))
        percentage_increase = float(input("Enter the percentage increase per year: "))
        number_of_years = int(input("Enter the number of years in the schedule: "))

        print("\nSalary Schedule:")
        generate_salary_schedule(starting_salary, percentage_increase, number_of_years)

    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
