<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

  <header>
    <h1>Black Scholes Calculator</h1>
    <p>A stylish Python Tkinter GUI for calculating option values using the Black-Scholes Model.</p>
  </header>

  <section>
    <h2>Overview</h2>
    <p>The Black-Scholes Calculator is a financial tool that estimates the theoretical price of European-style options. It takes into account various assumptions to provide a valuation, including constant interest rates, log-normal distribution of stock prices, and more.</p>
  </section>

  <section>
    <h2>Model Assumptions</h2>
    <ol>
      <li><strong>Interest Rate:</strong> Known and constant through time.</li>
      <li><strong>Stock Movement:</strong> Follows a random walk in continuous time, with the variance of stock price paths following a log-normal distribution.</li>
      <li><strong>Volatility:</strong> Assumed to be constant.</li>
      <li><strong>Dividends:</strong> Stock pays no dividends (modifiable to include them).</li>
      <li><strong>Option Exercise:</strong> Options can only be exercised at expiration (European option).</li>
      <li><strong>Transaction Costs:</strong> No transaction costs, fees on shorting, selling, etc.</li>
      <li><strong>Fractional Trading:</strong> Buying/selling fractional amounts of any given stock is possible.</li>
    </ol>
  </section>

  <section>
    <h2>What is Black-Scholes?</h2>
    <p>The Black-Scholes Model is a mathematical model used to calculate the theoretical price of financial options. Developed by economists Fischer Black, Myron Scholes, and Robert Merton, it has been widely used for option pricing since its introduction in 1973.</p>
  </section>

  <section>
    <h2>Note on Underestimated Tail Events</h2>
    <p>While the Black-Scholes Model is a valuable tool, it has limitations, especially in predicting extreme market events (tail events). It assumes a normal distribution of stock prices, which may lead to underestimating the impact of rare, unexpected events. Traders and investors should be aware of these limitations and exercise caution, especially in volatile markets.</p>
  </section>

  <section>
    <h2>Usage</h2>
    <p>To use the Black-Scholes Calculator, simply run the provided Python script (<code>blackScholes.py</code>). Enter the required parameters, such as current asset price, strike price, risk-free rate, time to expiration, volatility, and dividend yield (if applicable). Select the option type (Call, Put, Call with Dividends, Put with Dividends), and click "Calculate" to get the estimated option value.</p>
    <p>Feel free to contribute, report issues, or suggest improvements.</p>
  </section>

  <section>
  <h2>Download and Usage</h2>
  <ul>
    <li><strong>Navigate to the Project Directory:</strong> Use the `cd` command to go to the project directory:</li>
    <code>cd Black_Scholes_Calculator</code>
    <li><strong>Install Dependencies:</strong> Ensure you have Python installed. Install the required dependencies:</li>
    <code>pip install -r requirements.txt</code>
    <li><strong>Run the Application:</strong> Execute the Python script to run the Black-Scholes Calculator:</li>
    <code>python blackScholes.py</code>
    <li><strong>Use the Application:</strong> The GUI will appear. Enter the required parameters, select the option type, and click "Calculate" to get the estimated option value.</li>
  </ul>
</section>


  <footer>
    <p><strong>Disclaimer:</strong> This tool is for educational and informational purposes only. It does not provide financial advice or guarantee accuracy in real-wor
