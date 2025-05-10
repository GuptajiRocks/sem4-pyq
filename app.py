from flask import Flask, render_template, request

app = Flask(__name__)

subjects_data = {
    "Computer Networks": [
        {"name": "QP1", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CMCA508_Computer+Network-Layers+and+Protocols.pdf"},
        {"name": "QP2", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CMCA508+_Computer+Network-Layers+and+Protocols+.pdf"},
        {"name": "QP3", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET207_COMPUTER_NETWORKS.pdf"},
        {"name": "QP4", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET207_Computer+Networks.pdf"},
        {"name": "QP5", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET207_Computer+Networks1.pdf"},
        {"name": "QP6", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/EECE314L_Computer+Networks.pdf"}
    ],
    "Operating Systems": [
        {"name": "QP1", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CBCA203_OPERATING+SYSTEM+CONCEPTS.pdf"},
        {"name": "QP2", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CBSC-202+FUNDAMENTALS+OF+OPERATING+SYSTEM.pdf"},
        {"name": "QP3", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CMCA505_Operating+System+Essentials.pdf"},
        {"name": "QP4", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET209_OPERATING_SYSTEM (1).pdf"},
        {"name": "QP5", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET209_Operating+Systems1.pdf"},
        {"name": "QP6", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET209_OPERATING_SYSTEM (1).pdf"},
        {"name": "QP7", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET209_OPERATING_SYSTEM (2).pdf"},
        {"name": "QP8", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET209_Operating+Systems.pdf"}
    ],
    "Design and Analysis of Algorithms": [
        {"name": "QP1", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CBSC203_Algorithm+Analysis+and+Design+.pdf"},
        {"name": "QP2", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET206 DESIGN AND ANALYSIS OF ALGORITHMS.pdf"},
        {"name": "QP3", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET206_DESIGN_AND_ANALYSIS_OF_ALGORITHM (1).pdf"},
        {"name": "QP4", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET206_DESIGN_AND_ANALYSIS_OF_ALGORITHM (2).pdf"},
        {"name": "QP5", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET206_DESIGN_AND_ANALYSIS_OF_ALGORITHM.pdf"},
        {"name": "QP6", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET206_Design+and+Analysis+of+Algorithm.pdf"},
        {"name": "QP7", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET206_Design+and+Analysis+of+Algorithms (1).pdf"},
        {"name": "QP8", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET206_Design+and+Analysis+of+Algorithms.pdf"},
        {"name": "QP9", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET206_Design+and+Analysis+of+Algorithms+ (1).pdf"},
        {"name": "QP10", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/CSET206_Design+and+Analysis+of+Algorithms+.pdf"},
        {"name": "QP11", "url": "https://trialtwo.blob.core.windows.net/sem5-pyq/G23.pdf"}
    ],
    "Data Mining and Predictive Modelling": [
        {"name": "DMPM_Final_2023.pdf", "url": "https://your-azure-link.com/DMPM_Final_2023.pdf"}
    ]
}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', subjects=list(subjects_data.keys()))

@app.route('/subject', methods=['POST'])
def subject():
    selected_subject = request.form.get('subject')
    files = subjects_data.get(selected_subject)
    if not files:
        return "Subject not found", 404
    return render_template('subject.html', subject=selected_subject, files=files)

if __name__ == '__main__':
    app.run(debug=True)
