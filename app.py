import matplotlib
matplotlib.use('Agg')   # MUST be before any other matplotlib import

from flask import Flask, jsonify, render_template
from simulation import SPHSimulation

app = Flask(__name__)
sim = SPHSimulation()   # one shared simulation instance

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/frame")
def frame():
    sim.step_n(3)
    img = sim.get_frame_base64()
    return jsonify({"image": img, "state": sim.state, "step": sim.step_count})

@app.route("/action/collapse", methods=["POST"])
def collapse():
    sim.initiate_collapse()
    return jsonify({"status": "collapse initiated"})

@app.route("/action/reset", methods=["POST"])
def reset():
    sim.reset()
    return jsonify({"status": "reset"})

if __name__ == "__main__":
    app.run(debug=True)