from sqlalchemy import Column, String, Float, Integer, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class FactOrders(Base):
    __tablename__ = "fact_orders"
    order_id = Column(String(50), primary_key=True)
    user_id = Column(String(50))
    product_id = Column(String(50))
    seller_id = Column(String(50))
    order_total_usd = Column(Float)
    order_status = Column(String(30))
    created_at = Column(DateTime)

class DimProducts(Base):
    __tablename__ = "dim_products"
    product_id = Column(String(50), primary_key=True)
    category_name = Column(String(100))
    photos_qty = Column(Integer)

class DimUsers(Base):
    __tablename__ = "dim_users"
    user_id = Column(String(50), primary_key=True)
    city = Column(String(100))
    state = Column(String(50))

class DimSellers(Base):
    __tablename__ = "dim_sellers"
    seller_id = Column(String(50), primary_key=True)
    seller_city = Column(String(100))
    seller_state = Column(String(50))

class DimReviews(Base):
    __tablename__ = "dim_reviews"
    review_id = Column(String(50), primary_key=True)
    order_id = Column(String(50))
    review_score = Column(Integer)

class DimGeography(Base):
    __tablename__ = "dim_geography"
    geo_id = Column(Integer, primary_key=True, autoincrement=True)
    zip_code_prefix = Column(String(10))
    city = Column(String(100))
    state = Column(String(50))
    lat = Column(Float)
    lng = Column(Float)