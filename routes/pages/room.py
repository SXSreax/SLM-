from flask import Blueprint, render_template
import random
import string

room_bp = Blueprint('room', __name__)

@room_bp.route('/room')
def room():
    code = ''.join(random.choices(string.ascii_letters, k=8))
    return render_template('room.html', code=code)