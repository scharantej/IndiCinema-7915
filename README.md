**Flask Application to Analyze Indian Movie History**

**HTML Files**

- **index.html**: This file is the main landing page of the application. It will contain the necessary HTML elements to display the interface for analyzing Indian movie history.
- **results.html**: This file will display the results of the analysis performed on the Indian movie history data.

**Routes**

- **@app.route('/')**: This route maps to the main landing page of the application. When the user accesses the root URL, this function will be executed and it will render the 'index.html' file.
- **@app.route('/analyze', methods=['POST'])**: This route is triggered when the user submits an analysis request. It will receive the form data containing the parameters for the analysis (e.g., movie genre, year range, etc.), and then perform the analysis accordingly. After the analysis, it will redirect the user to the 'results.html' file, passing on the analysis results.