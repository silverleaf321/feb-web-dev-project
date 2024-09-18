from flask import Flask, render_template, request, jsonify
import graphing  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    file = request.files['file']
    
    column_names = graphing.load_csv(file)
    return jsonify(column_names)  

@app.route('/generate_graph', methods=['POST'])
def generate_graph():
    data = request.json
    x_col = data['xAxis']
    y_col = data['yAxis']
    graph_type = data['graphType']

    if graph_type == 'scatter':
        plot_url = graphing.scatterplot(x_col, y_col)
    elif graph_type == 'bar':
        plot_url = graphing.barplot(x_col, y_col)
    else:
        return jsonify({"error": "Invalid graph type"}), 400

    return jsonify({'plot_url': plot_url})


if __name__ == '__main__':
    app.run(debug=True)
