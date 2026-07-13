from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="database",
        user="root",
        password="rootpass",
        database="mydb"
    )


@app.route('/')
def home():
    return "Hello from Flask Backend!"


@app.route('/users')
def users():

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")

    data = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
