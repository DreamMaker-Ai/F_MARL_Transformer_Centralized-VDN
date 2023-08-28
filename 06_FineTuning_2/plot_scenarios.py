import numpy as np
import matplotlib.pyplot as plt

from finetuning_config import Config


def main():
    config = Config()
    scenario_id = 5

    fig, ax = plt.subplots(nrows=2, ncols=2, squeeze=False, figsize=(8, 8))

    for i in range(2):
        for j in range(2):
            mat = np.zeros((15, 15, 3))

            config.read_test_scenario(scenario_id=scenario_id)
            reds = config.red_pos
            blues = config.blue_pos

            for k, red in enumerate(reds):
                if k < 8:
                    mat[red[0], red[1], 0] = 0.5
                else:
                    mat[red[0], red[1], 0] = 1

            for k, blue in enumerate(blues):
                if k < 8:
                    mat[blue[0], blue[1], 2] = 1
                else:
                    mat[blue[0], blue[1], 2] = 0.5

            ax[i, j].set_title(f'scenario {scenario_id}')
            ax[i, j].tick_params(bottom=False, labelbottom=False)
            ax[i, j].imshow(mat)

            scenario_id += 1

    plt.show()
    fig.savefig('nominal_scenarios', dpi=300)


if __name__ == '__main__':
    main()
