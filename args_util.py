
def find(args, arg):
    try:
        i = args.index(arg)
        return args[i + 1]
    except:
        raise Exception(f"Missing required argument: {arg}")


def parse_args(args):
    args = args[1:]

    config_dict = {}
    required_args = ["-d", "-p", "-i", "-m", "-e"]
    for arg in required_args:
        config_dict[arg] = find(args, arg)

    if ((config_dict["-e"] == "origin") or (config_dict["-e"] == "reducezero") or (config_dict["-e"] == "reducezero_smote")
        or (config_dict["-e"] == "resampling") or (config_dict["-e"] == "undersampling")
        or (config_dict["-e"] == "cvae") or (config_dict["-e"] == "reducezero_cvae")) and len(config_dict) != 5:
        raise Exception(f"{config_dict['-e']} has no -cp or -ep")
    if config_dict["-e"] == "fs" or config_dict["-e"] == "fs_cvae" or config_dict["-e"] == "lda_cvae" or config_dict["-e"] == "lda_smote" or config_dict["-e"] == "reducezero_smote" or config_dict["-e"] == "reducezero":
        config_dict["-cp"] = find(args, "-cp")
        config_dict["-ep"] = find(args, "-ep")
    if config_dict["-e"] not in ["origin", "reducezero","reducezero_smote", "reducezero_cvae", "resampling", "undersampling", "fs", "cvae", "fs_cvae", "smote","lda_cvae","lda_smote"]:
        raise Exception(f"Wrong parameters {config_dict}, please check again.")

    optional_args = ["-r", "-a"]
    for arg in optional_args:
        if arg in args:
            config_dict[arg] = args[args.index(arg) + 1]

    return config_dict
