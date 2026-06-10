import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))

print("Loading CSVs...")

orders = pd.read_csv("data/raw/olist_orders_dataset.csv")
products = pd.read_csv("data/raw/olist_products_dataset.csv")
customers = pd.read_csv("data/raw/olist_customers_dataset.csv")
sellers = pd.read_csv("data/raw/olist_sellers_dataset.csv")
reviews = pd.read_csv("data/raw/olist_order_reviews_dataset.csv")
geo = pd.read_csv("data/raw/olist_geolocation_dataset.csv")
order_items = pd.read_csv("data/raw/olist_order_items_dataset.csv")

print("Creating tables...")

customers.rename(columns={"customer_id":"user_id","customer_city":"city","customer_state":"state"}, inplace=True)
customers[["user_id","city","state"]].drop_duplicates().to_sql("dim_users", engine, if_exists="replace", index=False)
print("dim_users done")

products[["product_id","product_category_name","product_photos_qty"]].rename(columns={"product_category_name":"category_name","product_photos_qty":"photos_qty"}).to_sql("dim_products", engine, if_exists="replace", index=False)
print("dim_products done")

sellers.to_sql("dim_sellers", engine, if_exists="replace", index=False)
print("dim_sellers done")

reviews[["review_id","order_id","review_score"]].drop_duplicates("review_id").to_sql("dim_reviews", engine, if_exists="replace", index=False)
print("dim_reviews done")

geo.rename(columns={"geolocation_zip_code_prefix":"zip_code_prefix","geolocation_city":"city","geolocation_state":"state","geolocation_lat":"lat","geolocation_lng":"lng"}, inplace=True)
geo[["zip_code_prefix","city","state","lat","lng"]].drop_duplicates().to_sql("dim_geography", engine, if_exists="replace", index=False)
print("dim_geography done")

merged = orders.merge(order_items[["order_id","product_id","seller_id","price"]], on="order_id")
merged.rename(columns={"customer_id":"user_id","price":"order_total_usd","order_purchase_timestamp":"created_at"}, inplace=True)
merged[["order_id","user_id","product_id","seller_id","order_total_usd","order_status","created_at"]].to_sql("fact_orders", engine, if_exists="replace", index=False)
print("fact_orders done")

print("MySQL seeded successfully!")