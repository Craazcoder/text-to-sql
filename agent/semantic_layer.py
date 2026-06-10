SEMANTIC_LAYER = {
    "fact_orders": {
        "description": "Central fact table. One row per order-product pair.",
        "columns": {
            "order_total_usd": "Always SUM this for revenue. Filter order_status='delivered' for accurate revenue.",
            "order_status": "Values: delivered, shipped, canceled, processing.",
            "created_at": "Order placement timestamp. Use for time-based filters."
        }
    },
    "dim_products": {"description": "Product catalog with category info."},
    "dim_users": {"description": "Customer dimension. city/state are customer location."},
    "dim_sellers": {"description": "Seller dimension. seller_city/seller_state are seller location."},
    "dim_reviews": {"description": "One review per order. review_score is 1-5."},
    "dim_geography": {"description": "Zip-level lat/lng for geographic analysis."}
}