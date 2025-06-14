# Problem 2 - The Number of Rich Customers ( https://leetcode.com/problems/the-number-of-rich-customers/ )
import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    # Filtering amounts greater than 500
    df = store[store['amount'] > 500]
    # Finding number of customers with amounts greater than 500
    rich_count = len(set(df['customer_id']))
    # Return the rich_count dataframe
    return pd.DataFrame([rich_count], columns = ['rich_count'])