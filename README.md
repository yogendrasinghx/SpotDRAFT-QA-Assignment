<body>
  <h1>UI Automation Test - Readme</h1>

  <h2>Assignment</h2>
  <p>
    The goal of this assignment is to write UI automation tests to validate the following scenario on goodreads.com:
  </p>

  <ol>
    <li>Login to goodreads.com</li>
    <li>Search for a specific book title</li>
    <li>Mark it as 'want to read'</li>
    <li>Remove the selected book from my book list</li>
    <li>Logout</li>
  </ol>

  <h2>Test Cases</h2>
  <p>
    The test cases have been implemented using Python, Selenium WebDriver, and PyTest. Here are the details of each test case:
  </p>

  <h3>Test: Homepage Sign In Button</h3>
  <ul>
    <li>Verifies that clicking on the homepage sign-in button leads to the sign-in page.</li>
  </ul>

  <h3>Test: Login</h3>
  <ul>
    <li>Performs the login process using the provided email and password.</li>
    <li>Verifies that the user is redirected to the "Recent updates | Goodreads" page after successful login.</li>
  </ul>

  <h3>Test: Search Book</h3>
  <ul>
    <li>Searches for a specific book by its title.</li>
    <li>Verifies that the search results page contains the expected book.</li>
  </ul>

  <h3>Test: Add "Want to Read" Book</h3>
  <ul>
    <li>Opens the book information page and marks it as "Want to Read".</li>
    <li>Verifies that a toast message confirming the action is displayed.</li>
  </ul>

  <h3>Test: Open My Books Page</h3>
  <ul>
    <li>Opens the user's "My Books" page.</li>
    <li>Verifies that the page title contains the phrase "books on Goodreads".</li>
  </ul>

  <h3>Test: Remove Selected Book</h3>
  <ul>
    <li>Removes the selected book from the user's book list.</li>
    <li>Verifies that the book is no longer present in the book list.</li>
  </ul>

  <h3>Test: Logout</h3>
  <ul>
    <li>Performs the logout process.</li>
    <li>Verifies that the user is redirected to the Goodreads homepage.</li>
  </ul>

  <h2>Usage</h2>
<p>
  To run the UI automation tests, follow these steps:
</p>
<ol>
  <li>Clone the project repository:</li>
</ol>
<pre><code>git clone https://github.com/your-username/your-project.git
cd your-project/
</code></pre>

<ol start="2">
  <li>Install the required dependencies using pip:</li>
</ol>
<pre><code>pip install -r requirements.txt
</code></pre>
<p>
  The <code>requirements.txt</code> file should contain the necessary dependencies, including Python, Selenium WebDriver, and PyTest.
</p>

<ol start="3">
  <li>Set up the necessary configurations:</li>
</ol>
<ul>
  <li>Update the login credentials and book details in the test code.</li>
  <li>Customize any other relevant configurations as needed.</li>
</ul>

<ol start="4">
  <li>Run the tests using the PyTest framework:</li>
</ol>
<pre><code>pytest test_scenarios.py
</code></pre>
<p>
  This command will execute the test scenarios defined in the <code>test_scenarios.py</code> file.
</p>

<h2>Notes</h2>
<ul>
  <li>Ensure that you have an internet connection during the test execution.</li>
  <li>Make sure to have a compatible version of Python installed.</li>
  <li>It is recommended to set up a virtual environment before installing the project dependencies using pip.</li>
</ul>
</body>
