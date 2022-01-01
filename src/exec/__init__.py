from typing import Optional

from omegaconf import DictConfig
import src.utils as utils

log = utils.get_logger(__name__)


def start(config: DictConfig) -> Optional[float]:
    """Contains the experimental pipeline.
    Instantiates all objects from config.
    Args:
        config (DictConfig): Configuration composed by Hydra.
    Returns:
        Optional[float]: Metric score for hyperparameter optimization.
    """

    # Set seed for random number generators in pytorch, numpy and python.random
    if config.get("seed"):
        log.info(f"Setting seed to {config.get('seed')}")

    # Train the model
    log.info("Starting Experiment")

    # Make sure everything closed properly
    log.info("Finalizing!")
    # Return zero
    return 0