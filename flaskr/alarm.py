import functools
from flask import (
    Blueprint, flash, g, render_template, request, url_for
)


bp = Blueprint('alarm',  __name__)

@bp.route('/', methods=('GET', 'POST'))
def get_input():
    if request.method == 'POST':
        alarm_time = request.form['alarmTimeForm']
        error = None

        if not alarm_time:
            error = "Need to submit an alarm time"
            flash(error)
        
        if error is None:
            with open("alarm_time.txt", 'w') as f:
                f.write(alarm_time)      
           
    return render_template('settings.html')

