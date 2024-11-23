import hydra
from omegaconf import DictConfig
import os
import logging
import subprocess
import shutil
from hydra.core.hydra_config import HydraConfig

logger = logging.getLogger(__name__)

@hydra.main(config_name="config", version_base=None, config_path="conf")
def main(cfg: DictConfig) -> None:

    logger.info("Start Processing")

    # Hydraで出力されたconfigのパスを取得
    param_path = os.path.join(
        HydraConfig.get().runtime.output_dir, 
        ".hydra", 
        "config.yaml",
        )
    
    # 上記で取得したconfigをkedroのデフォルトのディレクトリにコピーする。
    shutil.copy(param_path, "./conf/base/parameters.yaml")

    # kedroをサブプロセスで実行
    command = [
        "kedro", 
        "run", 
        ]

    subprocess.run(command)

    logger.info("Finish")

if __name__ == "__main__":
    main()
