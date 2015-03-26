from flask import Flask, render_template, redirect, url_for, request, jsonify
from forms import IndexForm

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='q(k@ybgfsftbv1$x4a$oht8-6#0pskj08!7bl+$mgej=b2pwf_'
)


data = {
        "Audi": ["A1", "A2", "A3", "A4", "A6", "Q3", "Q7"],
        "Ford": ["Focus", "Fiesta", "Mondeo", "Kuga"],
        "Skoda": ["Fabia", "Octavia", "Rapid", "Yeti"]
}


@app.route("/", methods=['GET', 'POST'])
def index():
    form = IndexForm()
    form.car.choices = [(key, key) for key in data]
    if form.validate_on_submit():
        context_dict = {"car": '', "model": '', "run": 0}
        return redirect(url_for('choice', context_dict=context_dict))
    return render_template('index.html', form=form)


@app.route('/choice')
def choice():
    car = request.args.get('car')
    model = request.args.get('model')
    run = request.args.get('run')
    return render_template('choice.html', context_dict={'car': car,
                                                        'model': model,
                                                        'run': run})


@app.route('/suggest_models/')
def suggest_models():
    car = request.args.get('car')
    models = data[car]
    return jsonify(models=models)


if __name__ == "__main__":
    app.run()
