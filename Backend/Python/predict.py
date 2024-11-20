import sys
import pickle
import json
import pandas as pd
import numpy as np

# Load the model
with open('E:/Machine Learning/ML MERN/MedicineRecommendationSystem/Backend/Python/model.pkl', 'rb') as file:
    svc = pickle.load(file)

symptoms_dict = {'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12, 'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56, 'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60, 'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85, 'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89, 'foul_smell_of urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98, 'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102, 'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111, 'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115, 'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119, 'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131}

diseases_list = {15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction', 33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma', 23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)', 28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A', 19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis', 36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack', 39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis', 5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection', 35: 'Psoriasis', 27: 'Impetigo'}


# Load datasets
precautions = pd.read_csv('E:/Machine Learning/ML MERN/MedicineRecommendationSystem/Backend/Python/datasets/precautions_df.csv')
medication = pd.read_csv('E:/Machine Learning/ML MERN/MedicineRecommendationSystem/Backend/Python/datasets/medications.csv')
workout = pd.read_csv('E:/Machine Learning/ML MERN/MedicineRecommendationSystem/Backend/Python/datasets/workout_df.csv')
description = pd.read_csv('E:/Machine Learning/ML MERN/MedicineRecommendationSystem/Backend/Python/datasets/description.csv')
diets = pd.read_csv('E:/Machine Learning/ML MERN/MedicineRecommendationSystem/Backend/Python/datasets/diets.csv')

def handle_nan(value):
    if isinstance(value, float) and (value != value):  # Check for NaN
        return None
    return value

def handle_data(data):
    if isinstance(data, (list, tuple)):
        return [handle_data(item) for item in data]
    elif isinstance(data, dict):
        return {key: handle_data(value) for key, value in data.items()}
    else:
        return handle_nan(data)

def helper(dis):
    desc = description[description['Disease'] == dis].values
    pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values
    med = medication[medication['Disease'] == dis].values
    diet = diets[diets['Disease'] == dis].values
    wrkout = workout[workout['disease'] == dis]['workout'].values

    return desc, pre, med, diet, wrkout

# Read input from command line
if len(sys.argv) > 1:
    input_data = sys.argv[1]
    try:
        data = json.loads(input_data)
        symptoms = data.get('symptoms', [])
        
        # Preprocess symptoms
        symptom_values = [0] * len(symptoms_dict)
        for symptom in symptoms:
            if symptom in symptoms_dict:
                symptom_values[symptoms_dict[symptom]] = 1

        # Prediction
        prediction = svc.predict([symptom_values])
        predicted_disease = diseases_list.get(prediction[0], 'Unknown')

        # Get helper data
        desc, pre, med, diet, wrkout = helper(predicted_disease)

    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        sys.exit(1)  # Exit with error code

# Handle NaN values in response
response = {
    'description': handle_data(desc.tolist() if hasattr(desc, 'tolist') else desc),
    'precautions': handle_data(pre.tolist() if hasattr(pre, 'tolist') else pre),
    'medications': handle_data(med.tolist() if hasattr(med, 'tolist') else med),
    'diets': handle_data(diet.tolist() if hasattr(diet, 'tolist') else diet),
    'workouts': handle_data(wrkout.tolist() if hasattr(wrkout, 'tolist') else wrkout),
    'predicted_disease': handle_data(predicted_disease.tolist() if hasattr(predicted_disease, 'tolist') else predicted_disease)
}

# Print the JSON response
print(json.dumps(response))