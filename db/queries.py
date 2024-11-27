
CREATE_TABLE_TABLE = """
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    size TEXT,
    price TEXT,
    article TEXT,
    photo
)
"""

INSERT_PRODUCTS = """
    INSERT INTO products (name, category, size, price, article, photo)
    VALUES (?, ?, ?, ?, ?, ?)
"""