import { useState } from "react";
import React from "react";
import "./Home.css";
import axios from 'axios'

//if error comes after submisson of symptoms -> try to convert
const Home = () => {
  const [symptoms, setsymptoms] = useState([]);
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Prepare data to be sent
      const inputData = { symptoms: symptoms.split(',').map(s => s.trim()) };
  
      // Make POST request to the Express server
      const response = await axios.post('http://localhost:3000/', inputData);
  
      // Get the response data
      const data = response.data;
  
      // Helper function to convert string representation of an array to a valid array
      const parseArray = (str) => {
        try {
          // Replace single quotes with double quotes and parse as JSON
          return JSON.parse(str.replace(/'/g, '"'));
        } catch (error) {
          console.error('Error parsing array:', error);
          return [];
        }
      };
  
      // Convert the inner string representations of arrays to valid arrays
      if (Array.isArray(data)) {
        data[1] = parseArray(data[1]);
      }
  
      // Handle the response
      setResult(data);
      console.log(data);  // Log the result
    } catch (err) {
      // Handle errors
      setResult(null);
    }
  };
  
  
  let symptoms_list = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of_urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']
  return (
    <div className="container">
      <div className="heading">
        <h1>Digital Doctor</h1>
      </div>

      <div className="input-box">
        <form onSubmit={handleSubmit}>
          <label>Enter Symptoms:</label>
          <input
            onChange={(e) => setsymptoms(e.target.value)}
            id="manualSymptoms"
            name="manualSymptoms"
            rows="4"
          ></input>
          <button type="submit">Submit</button>
        </form>
      </div>

      <div className="output-box">
        <div className="predicted_disease">
          <h3>Predicted Disease</h3>
        </div>
        {result == null ? null : (<div className="text">{result.predicted_disease}</div>)}
        <div className="Description">
          <h3>Description</h3>
        {result == null ? null : (<div className="text">{result.description[0][1]}</div> )}
        </div>
        <div className="Precaution">
          <h3>Precaution</h3>
          {result == null ? null : (<div className="text">{result.precautions[0].map((item, index) => (<div key={index}> {index+1}. {item == null ? 'Error Fetching Data' : item} </div> ))}</div>)}
        </div>
        <div className="Medication">
          <h3>Medication</h3>
          {result == null ? null : (<div className="text">{result.medications[0][1]}</div>)}
        </div>
        <div className="Diet">
          <h3>Diet</h3>
          {result == null ? null :(<div className="text">{result.diets[0][1]}</div>)}
        </div>
        <div className="Workout">
          <h3>Workout</h3>
          {result == null ? null : (<div className="text">{result.workouts.map((item, index) => (<div key={index}>{index+1}. {item}</div>))} </div>)}
        </div>
      </div>
      {/* <strong>Note : </strong><span>You can only select from these symptoms</span><button onClick={viil}>See List</button> */}
     {/* <div className="list"><span>{symptoms_list.map((item, index)=>(<div key={index}>{index+1} : {item} </div>))}</span></div>  */}
    </div>
  );
};

export default Home;
