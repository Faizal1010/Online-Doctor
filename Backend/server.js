const express = require('express')
const bodyParser = require('body-parser')
const { exec } = require('child_process')
const cors = require('cors')
const app = express()

app.use(cors())
app.use(bodyParser.json())

app.post('/', (req, res) => {
  const symptoms = req.body.symptoms;
  const { exec } = require('child_process');

  const inputData = JSON.stringify({ symptoms: symptoms });

  // Escape double quotes and format the command
  const escapedInputData = inputData.replace(/"/g, '\\"');
  const command = `python "E:/Machine Learning/ML MERN/MedicineRecommendationSystem/Backend/Python/predict.py" "${escapedInputData}"`;
  
  // Execute the command
  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return res.status(500).json({ error: 'Internal Server Error' });
    }
    // Log any stderr output
    if (stderr) {
      console.error(`stderr: ${stderr}`);
    }
    // Parse and send the JSON response
    try {
      const main_data = JSON.parse(stdout);
      res.json(main_data);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError);
      res.status(500).json({ error: 'Error parsing JSON' });
    }
  });
});



app.listen(3000, () => {
    console.log('App running on port 3000')
})