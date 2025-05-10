from flask import Flask, render_template

app = Flask(__name__)

# Subject-wise files with Azure links
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
        {"name": "OS_Midterm_2022.pdf", "url": "https://your-azure-link.com/OS_Midterm_2022.pdf"}
    ],
    "Design and Analysis of Algorithms": [
        {"name": "DAA_PYQ_2021.pdf", "url": "https://your-azure-link.com/DAA_PYQ_2021.pdf"}
    ],
    "Data Mining and Predictive Modelling": [
        {"name": "DMPM_Final_2023.pdf", "url": "https://your-azure-link.com/DMPM_Final_2023.pdf"}
    ]
}

@app.route('/')
def index():
    subjects = list(subjects_data.keys())
    return render_template('index.html', subjects=subjects)

@app.route('/subject/<subject>')
def subject(subject):
    files = subjects_data.get(subject)
    if not files:
        return "Subject not found", 404
    return render_template('subject.html', subject=subject, files=files)

if __name__ == '__main__':
    app.run(debug=True)
