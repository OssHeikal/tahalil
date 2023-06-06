<h1>tahalil Medical Diagnosis System</h1>

<p>This is a Flask-based web application that provides a medical diagnosis system for various conditions, including heart disease, hepatitis B and C, anemia, and diabetes. Users can input their relevant medical data through web forms or as JSON and receive predictions and reports based on the provided data.</p>

<h2>Installation</h2>

<ol>
  <li>Clone the repository:</li>
</ol>

<pre><code>git clone https://github.com/OssHeikal/tahalil.git
</code></pre>

<p>Install the required dependencies. It is recommended to use a virtual environment:</p>

<pre><code>cd tahalil
python3 -m venv venv
source venv/bin/activate  # Activate the virtual environment
pip install -r requirements.txt
</code></pre>

<p>Run the application:</p>

<pre><code>python app.py
</code></pre>

<h2>Usage</h2>

<p>Visit the home page at <a href="http://localhost:5000">http://localhost:5000</a> to see the welcome screen.</p>

<p>Click on the respective links for each medical condition to access the corresponding diagnosis form:</p>

<ul>
  <li>Heart Disease: <a href="http://localhost:5000/heart_disease">http://localhost:5000/heart_disease</a></li>
  <li>Hepatitis B: <a href="http://localhost:5000/hepatitis_b">http://localhost:5000/hepatitis_b</a></li>
  <li>Hepatitis C: <a href="http://localhost:5000/hepatitis_c">http://localhost:5000/hepatitis_c</a></li>
  <li>Anemia: <a href="http://localhost:5000/anemia">http://localhost:5000/anemia</a></li>
  <li>Diabetes: <a href="http://localhost:5000/diabetes">http://localhost:5000/diabetes</a></li>
</ul>

<p>Fill in the required information in the form and submit it.</p>

<p>The system will generate predictions based on the provided data and display the results along with a report.</p>

<p>You can also make predictions programmatically by sending POST requests to the respective prediction endpoints:</p>

<ul>
  <li>Anemia: <a href="http://localhost:5000/predict/anemia">http://localhost:5000/predict/anemia</a></li>
  <li>Diabetes: <a href="http://localhost:5000/predict_diabetes">http://localhost:5000/predict_diabetes</a></li>
  <li>Hepatitis B: <a href="http://localhost:5000/predict/hepatitis_b">http://localhost:5000/predict/hepatitis_b</a></li>
  <li>Hepatitis C: <a href="http://localhost:5000/predict/hepatitis_c">http://localhost:5000/predict/hepatitis_c</a></li>
  <li>Heart Disease: <a href="http://localhost:5000/predict/heart_disease">http://localhost:5000/predict/heart_disease</a></li>
</ul>

<p>The data can be sent either as JSON or as form data, depending on the content type of the request.</p>

<h2>Contributing</h2>

<p>Contributions are welcome! If you find any issues or want to add new features, please open an issue or submit a pull request.</p>
