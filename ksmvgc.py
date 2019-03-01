from vgcsc import app, db
from config import Config
from vgcsc.models import Access, Membership, Profile, Executive, PastExecutive

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Access": Access, "Membership": Membership, "Executive": Executive, \
        "PastExecutive":PastExecutive, "Config": Config}

if __name__ == "__main__":
    with vgcsc.app_context():
        app.run(debug=True)