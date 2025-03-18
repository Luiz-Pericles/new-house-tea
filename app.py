from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Gift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ambiente = db.Column(db.String(100))
    categoria = db.Column(db.String(100))
    item = db.Column(db.String(255), nullable=False)
    reserved_by = db.Column(db.String(100))
    option = db.Column(db.String(50))
    price = db.Column(db.Float)

# Página de Convite
@app.route("/")
def invite():
    return render_template("invite.html")

# Página que lista as categorias (ambientes)
@app.route("/presentes")
def gift_list():
    # Busca os ambientes distintos no banco
    ambientes = [row[0] for row in db.session.query(Gift.ambiente).distinct().all()]
    
    return render_template("gift_list.html", ambientes=ambientes)

# Página que mostra os presentes de um determinado ambiente
@app.route("/presentes/<ambiente>")
def gift_category(ambiente):
    gifts = Gift.query.filter_by(ambiente=ambiente).all()
    return render_template("gift_category.html", gifts=gifts, ambiente=ambiente)

@app.route("/reserve/<int:gift_id>", methods=["GET", "POST"])
def reserve(gift_id):
    gift = Gift.query.get_or_404(gift_id)
    pix_key = "12345678900@banco.com"
    
    if request.method == "POST":
        option = request.form.get("option")
        name = request.form.get("name")
        if name and option:
            gift.reserved_by = name
            gift.option = option
            db.session.commit()
            return redirect(url_for("gift_category", ambiente=gift.ambiente))
        else:
            error = "Por favor, preencha todos os campos."
            return render_template("reserve.html", gift=gift, pix_key=pix_key, error=error)
    
    return render_template("reserve.html", gift=gift, pix_key=pix_key)

if __name__ == "__main__":
    app.run(debug=True)
