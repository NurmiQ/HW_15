import sqlite3
import json
from flask import Flask


app = Flask(__name__)


@app.get("/<itemid>")
def get_item(itemid):
    with sqlite3.connect("animals.db") as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(
            f"""
            SELECT *
            FROM animals a 
            join annimal_type at2 
            WHERE a."index" = {itemid}
            """
        ).fetchone()

        result = dict(result)

        return app.response_class(
            json.dumps(result),
            status=200,
            mimetype="application/json")


if __name__ == '__main__':
    app.run()

