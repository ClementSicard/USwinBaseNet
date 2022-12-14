import numpy as np
from sklearn.svm import LinearSVC
from sklearn.metrics import f1_score
import sys
from datetime import datetime

sys.path.append("..")
from utils import *


def run(train_path: str, val_path: str, test_path: str):
    # Load data
    log("Loading data...")
    train_images, train_masks, val_images, val_masks = load_data(train_path, val_path)

    log(f"\tTraining images: {train_images.shape[0]}")
    log(f"\tTraining masks: {train_masks.shape[0]}")
    log(f"\tValidation images: {val_images.shape[0]}")
    log(f"\tValidation masks: {val_masks.shape[0]}")

    log("Creating patches...")
    train_patches, train_labels = image_to_patches(train_images, train_masks)
    val_patches, val_labels = image_to_patches(val_images, val_masks)

    # Extract features
    log("Extracting features...")
    x_train = extract_features(train_patches)
    x_val = extract_features(val_patches)

    log("Training model...")
    # Train model
    model = LinearSVC().fit(x_train, train_labels)
    log(f"\tTraining accuracy: {model.score(x_train, train_labels)}")
    log(f"Validation accuracy: {model.score(x_val, val_labels)}")

    test_path = os.path.join(test_path, "images")
    test_filenames = sorted(glob(test_path + "/*.png"))
    test_images = load_all_from_path(test_path)
    test_patches = image_to_patches(test_images)
    x_test = extract_features(test_patches)
    log("Making predictions...")
    test_pred = model.predict(x_test).reshape(
        -1, test_images.shape[1] // PATCH_SIZE, test_images.shape[2] // PATCH_SIZE
    )
    log(f"Test predictions shape: {test_pred.shape}")
    now = datetime.now()
    t = now.strftime("%Y-%m-%d_%H:%M:%S")
    os.makedirs("submissions", exist_ok=True)
    create_submission(
        test_pred,
        test_filenames,
        submission_filename=f"./submissions/baseline_svc_submission_{t}.csv",
    )
