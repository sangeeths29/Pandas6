# Problem 1 - Delete Duplicate Emails ( https://leetcode.com/problems/delete-duplicate-emails/)
import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort by id
    person.sort_values(['id'], inplace = True)
    # Drop duplicate emails
    person.drop_duplicates(['email'], inplace = True)