import numpy as np
import matplotlib.pyplot as plt

categories = np.array([], dtype=str)
amounts = np.array([], dtype=float)

while True:

    print("\n" + "=" * 40)
    print("       SMART EXPENSE ANALYZER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total and Average")
    print("4. Category-wise Report")
    print("5. Highest and Lowest Expense")
    print("6. Show Expense Charts")
    print("7. Exit")
    print("=" * 40)

    choice = input("Enter your choice (1-7): ")

    # 1. Add Expense
    if choice == "1":

        category = input("Enter category: ").strip().title()

        try:
            amount = float(input("Enter amount (Rs.): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if not category:
            print("Category cannot be empty!")
            continue

        if amount <= 0:
            print("Amount must be greater than zero!")
            continue

        categories = np.append(categories, category)
        amounts = np.append(amounts, amount)

        print("Expense added successfully!")

    # 2. View All Expenses
    elif choice == "2":

        if len(amounts) == 0:
            print("No expenses recorded yet.")

        else:
            print("\n------ ALL EXPENSES ------")

            for i in range(len(amounts)):
                print(i + 1, categories[i], "Rs.", amounts[i])

    # 3. Total and Average
    elif choice == "3":

        if len(amounts) == 0:
            print("No data available.")

        else:
            print("\n------ SUMMARY ------")
            print("Total Expense:", np.sum(amounts))
            print("Average Expense:", round(np.mean(amounts), 2))
            print("Number of Expenses:", len(amounts))

    # 4. Category-wise Report
    elif choice == "4":

        if len(amounts) == 0:
            print("No data available.")

        else:
            print("\n------ CATEGORY REPORT ------")

            unique_categories = np.unique(categories)

            for cat in unique_categories:
                total = np.sum(amounts[categories == cat])
                print(cat, ":", total, "Rs.")

    # 5. Highest and Lowest Expense
    elif choice == "5":

        if len(amounts) == 0:
            print("No data available.")

        else:
            high = np.argmax(amounts)
            low = np.argmin(amounts)

            print("\nHighest Expense:")
            print(categories[high], amounts[high], "Rs.")

            print("\nLowest Expense:")
            print(categories[low], amounts[low], "Rs.")

    # 6. Show Expense Charts
    elif choice == "6":

        if len(amounts) == 0:
            print("Add expenses first to view charts.")

        else:
            unique_categories = np.unique(categories)

            totals = np.array([
                np.sum(amounts[categories == cat])
                for cat in unique_categories
            ])

            # Bar Chart
            plt.figure(figsize=(8, 5))
            plt.bar(unique_categories, totals)
            plt.title("Category-wise Expenses")
            plt.xlabel("Categories")
            plt.ylabel("Amount (Rs.)")
            plt.tight_layout()
            plt.show()

            # Pie Chart
            plt.figure(figsize=(7, 7))
            plt.pie(
                totals,
                labels=unique_categories,
                autopct="%1.1f%%"
            )
            plt.title("Expense Distribution")
            plt.tight_layout()
            plt.show()

    # 7. Exit
    elif choice == "7":

        print("Thank you for using Smart Expense Analyzer!")
        print("Program closed.")
        break

    else:
        print("Invalid choice! Please enter between 1 and 7.")
