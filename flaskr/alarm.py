import functools
from flask import (
    Blueprint, flash, g, render_template, request, url_for
)


bp = Blueprint('alarm',  __name__, url_prefix='/alarm')

@bp.route('/settings', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        alarm_time = request.form['alarmTimeForm']
        error = None

        if not alarm_time:
            error = "Need to submit an alarm time"
        
        if error is None:
            with open("alarm_time.txt", 'w') as f:
                f.write(alarm_time)
        
        flash(error)
    
    return render_template('alarm/settings.html')

