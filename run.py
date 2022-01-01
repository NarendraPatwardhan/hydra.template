import dotenv
import hydra
from omegaconf import DictConfig

# load environment variables from `.env` file if it exists
# recursively searches for `.env` in all folders starting from work dir
dotenv.load_dotenv(override=True)


@hydra.main(config_path="configs/", config_name="index.yaml")
def main(config: DictConfig):

    import src.exec as exec
    import src.utils as utils

    # A couple of optional utilities to improve quality of life
    utils.extras(config)

    # Pretty print config using Rich library
    if config.get("print_config"):
        utils.print_config(config, resolve=True)

    # Run the experiment
    return exec.start(config)


if __name__ == "__main__":
    main()