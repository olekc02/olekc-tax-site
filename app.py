from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__)

# ---- Routes ----

@app.route("/")
def home():
    """
    Homepage with hero, services, referral, and contact sections.
    Pass a payment link via the OLEKC_PAYMENT_LINK environment variable (optional).
    """
    payment_link = os.environ.get("OLEKC_PAYMENT_LINK")  # e.g., Square/PayPal checkout URL
    return render_template("index.html", payment_link=payment_link)

@app.route("/health")
def health():
    """Simple health check for uptime monitors."""
    return {"status": "ok"}, 200

@app.route("/favicon.ico")
def favicon():
    """Serve a favicon if you put one at static/img/favicon.ico."""
    try:
        return send_from_directory(
            os.path.join(app.root_path, "static", "img"),
            "favicon.ico",
            mimetype="image/vnd.microsoft.icon",
        )
    except Exception:
        abort(404)

@app.route("/robots.txt")
def robots():
    """Optional: allow indexing; adjust if you want to block bots."""
    return "User-agent: *\nAllow: /", 200, {"Content-Type": "text/plain; charset=utf-8"}

# ---- App entrypoint (Render requires binding to 0.0.0.0 and PORT) ----

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # debug=True is fine locally; Render ignores it
    app.run(host="0.0.0.0", port=port, debug=True)
