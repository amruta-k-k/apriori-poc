"""
+Generate random orders with specific product names and quantities.
 
The generated orders will have random quantities of products with the following names:
- Pen
- Pencil
- Scale

The quantity of products per order will be between 1 and 3.
The order id will start from 1 and go up to 11.

The function returns a pandas DataFrame with the following columns:
- item_line_id: integer
- order_id: integer
- item_name: str

"""
import random
import pandas

def generate_random_orders(
    max_order_id: int = 10,
    max_quantity: int = 3
) -> pandas.DataFrame:
    products = {
        1: 'Pen',
        2: 'Pencil',
        3: 'Scale',
        4: 'Book',
        5: 'Eraser',
        6: 'Paper',
        7: 'Stapler',
        8: 'Pencil Sharpener',
        9: 'Notebook',
        10: 'Highlighter',
    }
    data = []
    N = 1
    for i in range(1, max_order_id + 1):
        order_id = i
        quantity = random.randint(1, max_quantity)
        product_ids = list(products.keys())
        random.shuffle(product_ids)
        for j in range(1, quantity + 1):
            row = [
                N,
                order_id,
                products[product_ids[j - 1]]
            ]
            N += 1
            data.append(row)
    df = pandas.DataFrame(data, columns=['item_line_id', 'order_id', 'item_name'])
    return df

CSV_FILE_PATH = 'orders.csv'

MAX_QUANTITY = 10
MAX_ORDER_ID = 100
row = []

if __name__ == '__main__':
    df = generate_random_orders(MAX_ORDER_ID, MAX_QUANTITY)
    df.to_csv(CSV_FILE_PATH, index=False)
