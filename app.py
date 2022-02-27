from itsdangerous import json
import streamlit as st
import joblib
import os

import numpy as np

def main():
    st.header("Car Evaluation ML App")
    actions = ["Predictive Analystics","EDA"]
    act = st.sidebar.selectbox("Choose the Action",actions)

    def load_model_n_predict(model_file):
        loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
        return loaded_model

    
    def get_value(key,dict):
        val = dict[key]
        return val


    buying_label = {"vhigh":0,"low":1,"med":2,"high":3}
    main_label = {"vhigh":0,"low":1,"med":2,"high":3}
    doors_label = {"2":0,"3":1,"5 more":2,"4":3}
    persons_label = {"2":0,"4":1,"more":2}
    lug_boot_label = {"small":0,"big":1,"med":2}
    safety_label = {"high":0,"med":1,"low":2}
    class_label = {0:"good",1:"acceptable",2:"very good",3:"unacceptable"}



    if act == "Predictive Analystics":

        bl = ["vhigh","low","med","high"]
        buying_level = st.selectbox("Select Buying Level",bl)
        

        ml = ["vhigh","low","med","high"]
        maintainance_level = st.selectbox("Select Maintenance Level",ml)

        nd = ["2","3","4","5 more"]
        number_doors = st.selectbox("Select Number of Doors",nd)

        number_of_persons = st.selectbox("Select number of Persons",("2","4","more"))

        bl = ["small","big","med"]
        boot_level = st.selectbox("Select Luggage Boot Level",bl)

        sf = ["high","med","low"]
        safety = st.selectbox("Select the Level of Safety",sf)

        st.subheader("Options Selected")
        st.json({"buying":buying_level, "maint":maintainance_level, "doors":number_doors
        ,"person":number_of_persons, "lug_boot":boot_level, "safety": safety})

        buying_level_ml = get_value(buying_level,buying_label)
        #st.write(buying_level_ml)

        maintainance_level_ml = get_value(maintainance_level,main_label)
        #st.write(maintainance_level_ml)

        noofdoors_ml = get_value(number_doors,doors_label)
        #st.write(noofdoors_ml)

        noofporson_ml = get_value(number_of_persons,persons_label)
        #st.write(noofporson_ml)

        bootlevel_ml = get_value(boot_level,lug_boot_label)
        #st.write(bootlevel_ml)

        safety_label_ml = get_value(safety,safety_label)
        #st.write(safety_label_ml)

        results = [buying_level_ml,maintainance_level_ml,noofdoors_ml,noofporson_ml,bootlevel_ml,safety_label_ml]
        sample_data = np.array(results).reshape(1, -1)










        model = st.selectbox("Model Choice",["Logistic Regression","Naive Bayes","MLP Classifier"])
        if st.button("Evaluate"):
            if model == "Logistic Regression":
                predictor = load_model_n_predict("models/logit_car_model.pkl")
                prediction = predictor.predict(sample_data)
                #st.write(prediction)
                p = int(prediction)
                st.success(get_value(p,class_label))

            if model == "Naive Bayes":
                predictor = load_model_n_predict("models/nb_car_model.pkl")
                prediction = predictor.predict(sample_data)
                st.write(prediction)
                p=int(prediction)
                st.success(get_value(p,class_label))

            if model == "MLP Classifier":
                predictor = load_model_n_predict("models/nn_clf_car_model.pkl")
                prediction = predictor.predict(sample_data)
                p=int(prediction)
                st.success(get_value(p,class_label))
















if __name__=='__main__':
    main()