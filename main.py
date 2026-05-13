from flask import Flask, render_template, send_from_directory, request, redirect

app = Flask(__name__)

CANONICAL_HOST = "benswieskowski.com"


@app.before_request
def redirect_www_to_apex():
    host = request.headers.get("Host", "").split(":")[0]
    if host == f"www.{CANONICAL_HOST}":
        return redirect(f"https://{CANONICAL_HOST}{request.full_path}".rstrip("?"), code=301)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/robots.txt")
def robots_txt():
    return send_from_directory(app.static_folder, "robots.txt", mimetype="text/plain")


@app.route("/sitemap.xml")
def sitemap_xml():
    return send_from_directory(app.static_folder, "sitemap.xml", mimetype="application/xml")


if __name__ == "__main__":
    app.run(debug=True)
