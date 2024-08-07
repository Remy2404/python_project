from flask import Flask, render_template, jsonify
from map_sim import cambodia_graph, mst_algorithm_step, get_initial_map_data

app = Flask(__name__)

mst_step_generator = None

@app.route('/')
def index():
    return render_template('cambodia_mst_map3.2.html')

@app.route('/start_mst')
def start_mst():
    global mst_step_generator
    mst_step_generator = mst_algorithm_step(cambodia_graph)
    initial_map_data = get_initial_map_data(cambodia_graph)
    return jsonify({'initial_map_data': initial_map_data})

@app.route('/next_mst_step')
def next_mst_step():
    global mst_step_generator
    try:
        map_update = next(mst_step_generator)
        return jsonify({'map_update': map_update})
    except StopIteration:
        return jsonify({'map_update': None})

if __name__ == '__main__':
    app.run(debug=True)