from flask import Flask, request, jsonify


app = Flask(__name__)
user = {}


@app.get("/users")
def get_users():
    return jsonify(user)


@app.get("/user/<id>")
def get_user_id(id):
    if str(id) in user:
        return user[str(id)]
    else:
        return "l'utilisateur n'a pas été trouvé", 404


@app.post("/add/user")
def add_users():
    data = request.get_json()

    user[str(len(user))] = data
    return f"L'utilisateur {len(user) - 1} a été ajouté.\nListe de user actuelle : {user} "


@app.put("/update/user/<id>")
def update_user(id):
    if id in user:
        data = request.get_json()
        user[str(id)] = data
        updated_user = {"id": id, "name": data["name"]}
        return f"L'utilisateur {updated_user} a été modifié\nListe de user actuelle : {user}"


@app.delete("/delete/user/<id>")
def del_user(id):
    if id in user:
        deleted_user = user[id]
        del user[id]
        return f"l'utilisateur {deleted_user} a été supprimé.\nListe de user actuelle : {user}"
    else:
        return "L'utilisateur n'a pas été trouvé.", 404
