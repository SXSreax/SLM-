from flask import Blueprint, render_template
import random
import string

room_bp = Blueprint('room', __name__)

@room_bp.route('/room')
def room():
    room_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return render_template('pages/room.html', room_code=room_code)