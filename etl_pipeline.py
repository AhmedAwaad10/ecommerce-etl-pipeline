import pandas as pd
import pyodbc
# customer dataset
def clean_customers() :
    cust_file=pd.read_csv(r'C:\Users\Home Lab\Desktop\archive\olist_customers_dataset.csv')
    cust_file['customer_id']= cust_file['customer_id'].str.strip()
    cust_file['customer_unique_id']= cust_file['customer_unique_id'].str.strip()
    cust_file['customer_zip_code_prefix']= cust_file['customer_zip_code_prefix'].astype(str).str.strip()
    cust_file['customer_city']= cust_file['customer_city'].str.strip()
    cust_file['customer_state']= cust_file['customer_state'].str.strip()
    return cust_file

# orders item dataset
def clean_order_item ():
    order_file=pd.read_csv(r'C:\Users\Home Lab\Desktop\archive\olist_order_items_dataset.csv')
    order_file['order_id']=order_file['order_id'].str.strip()
    order_file['product_id']=order_file['product_id'].str.strip()
    order_file['seller_id']=order_file['seller_id'].str.strip()
    order_file['shipping_limit_date']=pd.to_datetime(order_file['shipping_limit_date']) 
    order_file['price']=order_file['price'].astype(float)
    order_file['freight_value']=order_file['freight_value'].astype(float)
    return order_file

# order payment
def clean_order_payment():
    payment_file=pd.read_csv(r'C:\Users\Home Lab\Desktop\archive\olist_order_payments_dataset.csv')
    payment_file['order_id']=payment_file['order_id'].str.strip()
    payment_file['payment_type']=payment_file['payment_type'].str.strip()
    return payment_file

# orders dataset
def clean_order_dataset():
    orders_dataset=pd.read_csv(r'C:\Users\Home Lab\Desktop\archive\olist_orders_dataset.csv')
    date_cols = [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]

    for col in date_cols:
        orders_dataset[col] = pd.to_datetime(orders_dataset[col])
    return orders_dataset

# category dataset
def clean_category():
    cate_file=pd.read_csv(r'C:\Users\Home Lab\Desktop\archive\product_category_name_translation.csv')
    cate_file['product_category_name']=cate_file['product_category_name'].astype(str).str.strip()
    cate_file['product_category_name_english']= cate_file['product_category_name_english'].astype(str).str.strip()    
    return cate_file

# geoloc dataset
def clean_geoloc():
    geoloc_file=pd.read_csv(r'C:\Users\Home Lab\Desktop\archive\olist_geolocation_dataset.csv')
    geoloc_file['geolocation_city']=geoloc_file['geolocation_city'].astype(str).str.strip()
    geoloc_file['geolocation_state']=geoloc_file['geolocation_state'].astype(str).str.strip()
    return geoloc_file

# product dataset
def clean_product_dataset():
    product_file=pd.read_csv(r'C:\Users\Home Lab\Desktop\archive\olist_products_dataset.csv')
    product_file['product_id']=product_file['product_id'].str.strip()
    product_file['product_category_name']=product_file['product_category_name'].fillna('unknown').astype(str).str.strip()
    product_file['product_name_lenght']=product_file['product_name_lenght'].fillna(0)
    product_file['product_description_lenght']=product_file['product_description_lenght'].fillna(0)
    product_file['product_photos_qty']=product_file['product_photos_qty'].fillna(0)
    product_file['product_weight_g']=product_file['product_weight_g'].fillna(0)
    product_file['product_length_cm']=product_file['product_length_cm'].fillna(0)
    product_file['product_height_cm']=product_file['product_height_cm'].fillna(0)
    product_file['product_width_cm']=product_file['product_width_cm'].fillna(0)
    return product_file

# reviews dataset
def clean_reviews():
    reviews_file=pd.read_csv(r'C:\Users\Home Lab\Desktop\archive\olist_order_reviews_dataset.csv')
    reviews_file['review_id']=reviews_file['review_id'].str.strip()
    reviews_file['order_id']=reviews_file['order_id'].astype(str).str.strip()
    reviews_file['review_comment_title']=reviews_file['review_comment_title'].fillna('unknown').astype(str).str.strip()
    reviews_file['review_comment_message']=reviews_file['review_comment_message'].fillna('unknown').astype(str).str.strip()
    reviews_file['review_creation_date']=pd.to_datetime(reviews_file['review_creation_date'])
    reviews_file['review_answer_timestamp']=pd.to_datetime(reviews_file['review_answer_timestamp'])
    return reviews_file

# sellers dataset
def clean_sellers_dataset():
    sellers_file=pd.read_csv(r'C:\Users\Home Lab\Desktop\archive\olist_sellers_dataset.csv')
    sellers_file['seller_id'] = sellers_file['seller_id'].str.strip()
    sellers_file['seller_city']=sellers_file['seller_city'].str.strip()
    sellers_file['seller_state']=sellers_file['seller_state'].str.strip()
    return sellers_file

def run_etl_pipline():
    print(" Starting ETL Pipeline execution...\n")
    cust_file = clean_customers()
    print("1/9 Customers dataset processed successfully.")
    order_file= clean_order_item()
    print("2/9 order_item dataset processed successfully.")
    payment_file=clean_order_payment()
    print("3/9 order_payment dataset processed successfully.")
    orders_dataset= clean_order_dataset()
    print("4/9 order_dataset dataset processed successfully.")
    cate_file=clean_category()
    print("5/9 clean_category dataset processed successfully.")
    geoloc_file=clean_geoloc()
    print("6/9 clean_geoloc dataset processed successfully.")
    product_file=clean_product_dataset()
    print("7/9 clean_product_dataset dataset processed successfully.")
    reviews_file=clean_reviews()
    print("8/9 clean_reviews dataset processed successfully.")
    sellers_file=clean_sellers_dataset()
    print("9/9 clean_sellers dataset processed successfully.")
if __name__ == "__main__":
    run_etl_pipline()    
    
# --- دالة الـ Load باستخدام pyodbc ---
def load_to_sql(data_frames):
    print("Connecting to SQL Server via pyodbc")
    
    server_name = 'localhost\SQLEXPRESS'  
    db_name = 'Ecommerce'
    
    # connection string
    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server_name};DATABASE={db_name};Trusted_Connection=yes;"
    
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.fast_executemany = True  # لتسريع عملية الإدخال جداً
        print("Connected to Database successfully!\n")
        
        # 1. Customers
        print("Uploading [Customers]...")
        cursor.executemany(
            "INSERT INTO Customers (customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state) VALUES (?, ?, ?, ?, ?)",
            data_frames['customers'].values.tolist()
        )
        conn.commit()
        print("[Customers] loaded!")

        # 2. Category Translation
        print(" Uploading [Category_Translation]...")
        cursor.executemany(
            "INSERT INTO Category_Translation (product_category_name, product_category_name_english) VALUES (?, ?)",
            data_frames['category'].values.tolist()
        )
        conn.commit()
        print("[Category_Translation] loaded!")

        # 3. Products
        print("Uploading [Products]...")
        cursor.executemany(
            "INSERT INTO Products (product_id, product_category_name, product_name_lenght, product_description_lenght, product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            data_frames['products'].values.tolist()
        )
        conn.commit()
        print("[Products] loaded!")

        # 4. Sellers
        print(" Uploading [Sellers]...")
        cursor.executemany(
            "INSERT INTO Sellers (seller_id, seller_zip_code_prefix, seller_city, seller_state) VALUES (?, ?, ?, ?)",
            data_frames['sellers'].values.tolist()
        )
        conn.commit()
        print("[Sellers] loaded!")

        # 5. Geolocation
        print("Uploading [Geolocation]...")
        cursor.executemany(
            "INSERT INTO Geolocation (geolocation_zip_code_prefix, geolocation_lat, geolocation_lng, geolocation_city, geolocation_state) VALUES (?, ?, ?, ?, ?)",
            data_frames['geoloc'].values.tolist()
        )
        conn.commit()
        print(" [Geolocation] loaded!")

        # 6. Orders
        print(" Uploading [Orders]...")
        cursor.executemany(
            "INSERT INTO Orders (order_id, customer_id, order_status, order_purchase_timestamp, order_approved_at, order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            data_frames['orders'].values.tolist()
        )
        conn.commit()
        print("[Orders] loaded!")

        # 7. Order Items
        print(" Uploading [Order_Items]...")
        cursor.executemany(
            "INSERT INTO Order_Items (order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, freight_value) VALUES (?, ?, ?, ?, ?, ?, ?)",
            data_frames['order_items'].values.tolist()
        )
        conn.commit()
        print("[Order_Items] loaded!")

        # 8. Order Payments
        print("Uploading [Order_Payments]...")
        cursor.executemany(
            "INSERT INTO Order_Payments (order_id, payment_sequential, payment_type, payment_installments, payment_value) VALUES (?, ?, ?, ?, ?)",
            data_frames['payments'].values.tolist()
        )
        conn.commit()
        print("[Order_Payments] loaded!")

        # 9. Order Reviews
        print(" Uploading [Order_Reviews]...")
        cursor.executemany(
            "INSERT INTO Order_Reviews (review_id, order_id, review_score, review_comment_title, review_comment_message, review_creation_date, review_answer_timestamp) VALUES (?, ?, ?, ?, ?, ?, ?)",
            data_frames['reviews'].values.tolist()
        )
        conn.commit()
        print(" [Order_Reviews] loaded!")

        cursor.close()
        conn.close()
        print(" ALL DATA LOADED TO SQL SERVER SUCCESSFULLY 100%!")

    except Exception as e:
        print(f" Error while loading data: {e}")


def run_etl_pipeline():
    print("Starting ETL Pipeline execution...\n")
    
    dfs = {
        'customers': clean_customers(),
        'order_items': clean_order_item(),
        'payments': clean_order_payment(),
        'orders': clean_order_dataset(),
        'category': clean_category(),
        'geoloc': clean_geoloc(),
        'products': clean_product_dataset(),
        'reviews': clean_reviews(),
        'sellers': clean_sellers_dataset()
    }
    print(" All datasets extracted and transformed successfully!")

    load_to_sql(dfs)

if __name__ == "__main__":
    run_etl_pipeline()    
