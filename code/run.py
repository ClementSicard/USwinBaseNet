from utils import *
import argparse
import models.baselines.baseline_svm_classifier as svc
import models.baselines.baseline_patch_cnn as patch_cnn


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "model",
        type=str,
        help="Model to use for training.",
        choices=["baseline-svc", "baseline-unet", "baseline-patch-cnn"],
    )
    parser.add_argument(
        "--train-dir",
        type=str,
        required=True,
        help="Path to the training directory",
    )
    parser.add_argument(
        "--val-dir",
        type=str,
        required=True,
        help="Path to the validation directory",
    )
    parser.add_argument(
        "--test-dir",
        type=str,
        required=True,
        help="Path to the test directory",
    )

    args = parser.parse_args()
    print(vars(args))

    if args.model == "baseline-svc":
        print("Running baseline SVC...")
        svc.run(
            train_path=args.train_dir,
            val_path=args.val_dir,
            test_path=args.test_dir,
        )

    elif args.model == "baseline-patch-cnn":
        print("Running baseline Patch-CNN...")
        patch_cnn.run(
            train_path=args.train_dir,
            val_path=args.val_dir,
            test_path=args.test_dir,
        )

    elif args.model == "baseline-unet":
        print("Running baseline SVC...")
        raise NotImplementedError("Not implemented yet")

    else:
        raise NotImplementedError("Not implemented yet")
