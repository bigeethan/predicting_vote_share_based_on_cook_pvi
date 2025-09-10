import numpy as np
import pickle

# Code for creating and training the model is provided in this comment
#
# pandas, sklearn, and linear_model from sklearn are imported
#
# r_data = pd.read_csv("R_Vote_Share_vs_PVI.csv")
# prediction_label = "voter_share"
#
# r_x = np.array(r_data["pvi"]).reshape(-1, 1)
# r_y = np.array(r_data[prediction_label])
#
# best = 0
# for _ in range(30):
#    r_x_train, r_x_test, r_y_train, r_y_test = sklearn.model_selection.train_test_split(r_x, r_y, test_size=0.1)
#
#    linear_regression = linear_model.LinearRegression()
#    linear_regression.fit(r_x_train, r_y_train)
#    score = linear_regression.score(r_x_test, r_y_test)
#
#    if score > best:
#        best = score
#        with open("r_vote_share_model.pickle", "wb") as f:
#            pickle.dump(linear_regression, f)

saved_vote_share_model = open("r_vote_share_model.pickle", "rb")
linear_regression = pickle.load(saved_vote_share_model)

user_inputted_pvi = int(input("Please enter a Cook PVI value (negatives represent more Democrat, positives represent more Republican)\n"))
pvi_for_model = np.array([user_inputted_pvi]).reshape(-1, 1)
vote_share_prediction = linear_regression.predict(pvi_for_model)
print(f"\nBased on a Cook PVI of {pvi_for_model[0]}, a Republican is expected to get {round(vote_share_prediction[0], 2)}% of the vote")
