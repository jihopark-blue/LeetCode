import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    
    products.fillna(value={'quantity': 0}, inplace=True)
    # products['quantity'] = products['quantity'].fillna(0)

    return products