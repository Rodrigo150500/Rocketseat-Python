CREATE TABLE IF NOT EXISTS "users"(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,        
    password TEXT NOT NULL,
    token TEXTO NOT NULL
)