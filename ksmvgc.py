from vgcsc import app, db
from vgcsc.models import Access, Membership, Profile

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Access": Access, "Membership": Membership}

if __name__ == "__main__":
    with vgcsc.app_context():
        app.run(debug=True)