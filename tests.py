import data
import analysis


def run_tests():
    data.expenses.clear()
    data.monthly_budget = 0

    assert analysis.calculate_total() == 0
    assert analysis.count_expenses() == 0
    assert analysis.calculate_average() == 0

    data.expenses.extend([
        {
            "item": "Food",
            "amount": 100.0,
            "category": "food",
            "date": "01-09-2026",
            "payment": "UPI"
        },
        {
            "item": "Travel",
            "amount": 200.0,
            "category": "travel",
            "date": "02-09-2026",
            "payment": "cash"
        }
    ])

    assert analysis.calculate_total() == 300.0
    assert analysis.count_expenses() == 2
    assert analysis.calculate_average() == 150.0

    data.monthly_budget = 500.0
    assert data.monthly_budget - analysis.calculate_total() == 200.0

    print("All validation tests passed.")


if __name__ == "__main__":
    run_tests()