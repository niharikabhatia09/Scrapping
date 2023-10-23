import sqlite3
conn = sqlite3.connect('web_scraping_data.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS scraped_data (
        id INTEGER PRIMARY KEY,
        title TEXT,
        content TEXT
    )
''')
conn.commit()
conn.close()

conn = sqlite3.connect('web_scraping_data.db')
cursor = conn.cursor()

scraped_title = "Sample Title"
scraped_content = "This is some scraped content."
cursor.execute("INSERT INTO scraped_data (title, content) VALUES (?, ?)", (scraped_title, scraped_content))


conn.commit()
conn.close()
