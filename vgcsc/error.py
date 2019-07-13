from flask import render_template, make_response
from vgcsc import app, db

@app.errorhandler(404)
def page_not_found_error(error):
    # resp = make_response(render_template('vgcsc/404.html'), 404)
    # resp.headers['X-Something'] = 'A Value'
    # print(resp.headers)
    # return resp
    return render_template('vgcsc/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('vgcsc/500.html'), 500