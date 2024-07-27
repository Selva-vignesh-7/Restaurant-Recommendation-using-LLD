class Settings:
    def __init__(self):
        pass

    DATASET_FILE = 'C:/Users/yogde/OneDrive/Desktop/final/Restaurnt-Recommendation-System-main/dataset_file/tempe_review_1600.json'
    MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
    # REVIEWS_DATABASE = "Dataset_Challenge_Reviews" # original, trained
    USER_DATABASE = "usr"

    REVIEWS_COLLECTION = "b"
    USER_COLLECTION = "u"
    BUSINESS_COLLECTION = "b"
    USER_STOP="su"
    BUSINESS_STOP="sb"
    USER_PROFILE="up"
    BUSINESS_PROFILE="ub"
    check_user="cu"
    NEW_USER="nu"