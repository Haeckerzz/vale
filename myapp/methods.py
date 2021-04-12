# import pandas as pd
# from .models import Purchase
# import os 
# def csv_to_db():
#     df = pd.read_excel('data.xlsx') # use pandas to read the csv
#     records = df.to_records()  # convert to records
#     for record in records:
#         if str(record[4])!="nan":
#             purchase = Purchase(
#                 price=record[4],
#                 )
#             purchase.save()