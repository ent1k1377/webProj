from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs
from sqlalchemy.sql.expression import label
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init(f"db/mars_explorer.db")
    app.run()


@app.route("/")
def index():
    session = db_session.create_session()
    job = session.query(Jobs, User).filter(User.id == Jobs.team_leader)
    return render_template("jobs.html", jobss=job)


if __name__ == '__main__':
    main()
