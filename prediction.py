import pickle


def make_prediction(player_name, dataframe):
    try:
        player_data = dataframe.loc[player_name.lower()]
        player_data = player_data.to_numpy().reshape(1, -1)
        model = pickle.load(open('rf_model.pkl', 'rb'))
        prediction = model.predict(player_data)
        fl_prediction = prediction[0].item()
        if fl_prediction < -2.9:
            return "Projected NBA BPM: " + str(round(fl_prediction, 1)) + ". Likely end-of-bench player."
        elif -3.0 < fl_prediction < -0.9:
            return "Projected NBA BPM: " + str(round(fl_prediction, 1)) + ". Likely bench player."
        elif -1.0 < fl_prediction < 1.1:
            return "Projected NBA BPM: " + str(round(fl_prediction, 1)) + ". Likely starter or sixth man."
        else:
            return "Projected NBA BPM: " + str(round(fl_prediction, 1)) + ". Likely All-Star."
    except (Exception,):
        return "Player not found. Check for misspellings or try another player."
