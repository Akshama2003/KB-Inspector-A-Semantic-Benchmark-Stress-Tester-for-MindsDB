import requests

# Replace with your MindsDB credentials
MINDSDB_HOST = "http://cloud.mindsdb.com/sql/query"
HEADERS = {"Authorization": "Bearer YOUR_TOKEN_HERE"}

def run_sql(query):
    response = requests.post(MINDSDB_HOST, json={"query": query}, headers=HEADERS)
    return response.json()

def create_kb(kb_name):
    return run_sql(f"CREATE KNOWLEDGE_BASE {kb_name};")

def insert_data(kb_name, df):
    for _, row in df.iterrows():
        content = f"{row['headline']} - {row['short_description']}"
        meta = {"category": row["category"], "authors": row.get("authors", "unknown")}
        query = f"""
        INSERT INTO {kb_name} (content, metadata_columns)
        VALUES ("{content}", {meta});
        """
        run_sql(query)

def semantic_query(kb_name, query):
    sql = f"""SELECT content FROM {kb_name} WHERE content LIKE "{query}";"""
    return run_sql(sql)
