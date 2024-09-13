document.addEventListener('DOMContentLoaded', function() {
  const speciesSelect = document.getElementById('species');
  const chromosomeInput = document.getElementById('chromosome');
  const ssrtypeSelect = document.getElementById('ssrtype');
  const startInput = document.getElementById('Start');
  const endInput = document.getElementById('End');
  const submitButton = document.getElementById('submit-btn');
  const chartCanvas = document.getElementById('chart-canvas');
  
  // Disable submit button initially
  submitButton.disabled = true;

  // Function to enable/disable submit button based on form validation
  function validateForm() {
    const species = speciesSelect.value;
    const chromosome = chromosomeInput.value;
    const ssrtype = ssrtypeSelect.value;
    const start = startInput.value;
    const end = endInput.value;

    // Enable the submit button only if all fields are filled
    submitButton.disabled = !(species && chromosome && ssrtype && start && end);
  }

  // Event listeners for form inputs
  speciesSelect.addEventListener('change', validateForm);
  chromosomeInput.addEventListener('input', validateForm);
  ssrtypeSelect.addEventListener('change', validateForm);
  startInput.addEventListener('input', validateForm);
  endInput.addEventListener('input', validateForm);

  // Handle form submission
  submitButton.addEventListener('click', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get form data
    const species = speciesSelect.value;
    const chromosome = chromosomeInput.value;
    const ssrtype = ssrtypeSelect.value;
    const start = startInput.value;
    const end = endInput.value;

    // Create an object with form data
    const formData = {
      species: species,
      chromosome: chromosome,
      ssrtype: ssrtype,
      start: parseInt(start, 10), // Convert to integer
      end: parseInt(end, 10)        // Convert to integer
    };

    // Send form data to the PostgreSQL API using a POST request
    fetch('/api/analyze/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
      }
      return response.json();
    })
    .then(data => {
      // Handle the response from the server
      console.log(data);

      // Update the chart with the analysis results if applicable
      if (data.chart_data) {
        updateChart(data.chart_data);
      } else {
        console.error('No chart data returned from the server');
      }
    })
    .catch(error => {
      // Handle any errors
      console.error('Error:', error);
    });
  });

  // Function to update the chart with analysis results
  function updateChart(chartData) {
    // Clear the canvas
    chartCanvas.innerHTML = '';
    new Chart(chartCanvas, {
      type: 'bar',
      data: {
        labels: chartData.labels, // Assuming chartData contains labels
        datasets: [{
          label: 'SSR Count',
          data: chartData.data, // Assuming chartData contains data
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
            precision: 0
          }
        }
      }
    });
  }
});