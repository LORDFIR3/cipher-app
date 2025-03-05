from flask import Flask, request, jsonify, render_template
import caesar
import substitution

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form.get("text", "")
    shift = int(request.form.get("shift", 3))
    encrypted = caesar.caesar_cipher(text, shift)
    return jsonify({"result": encrypted})

@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form.get("text", "")
    shift = int(request.form.get("shift", 3))
    decrypted = caesar.caesar_decipher(text, shift)
    return jsonify({"result": decrypted})

@app.route("/replacement/encrypt", methods=["POST"])
def replacement_encrypt():
    text = request.form.get("text", "")
    key = request.form.get("key", "")
    encrypted = substitution.replacement_cipher(text, key)
    return jsonify({"result": encrypted})

@app.route("/replacement/decrypt", methods=["POST"])
def replacement_decrypt():
    text = request.form.get("text", "")
    key = request.form.get("key", "")
    decrypted = substitution.replacement_decipher(text, key)
    return jsonify({"result": decrypted})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
