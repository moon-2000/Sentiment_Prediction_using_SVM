# model_dispatcher.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

models = {
    "svm_lin_C01": SVC(kernel="linear", C=0.1),
    "svm_lin_C1": SVC(kernel="linear", C=1),
    "svm_lin_C10": SVC(kernel="linear", C=10),
    "svm_lin_C100": SVC(kernel="linear", C=100),
    "svm_poly_C01": SVC(kernel="poly", C=0.1),
    "svm_poly_C1": SVC(kernel="poly", C=1),
    "svm_poly_C10": SVC(kernel="poly", C=10),
    "svm_poly_C100": SVC(kernel="poly", C=100),
    "svm_sig_C01": SVC(kernel='sigmoid', C=0.1),
    "svm_sig_C1": SVC(kernel='sigmoid', C=1),
    "svm_sig_C10": SVC(kernel='sigmoid', C=10),
    "svm_sig_C100": SVC(kernel='sigmoid', C=100)
}
