BLOCKED_KEYWORDS = ["drop", "delete", "truncate", "update", "insert", "alter"]

def is_safe_sql(sql: str) -> bool:
    lowered = sql.lower()
    return not any(kw in lowered for kw in BLOCKED_KEYWORDS)