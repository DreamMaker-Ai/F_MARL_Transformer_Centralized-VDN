import numpy as np
import matplotlib.pyplot as plt

from finetuning_config import Config


def main():
    config = Config()
    scenario_id = 9
    num_red_platoons = 8
    num_blue_platoons = 12

    plt.figure(figsize=(8, 8))

    mat = np.zeros((15, 15, 3))

    config.read_test_scenario(scenario_id=scenario_id)
    reds = config.red_pos
    blues = config.blue_pos

    for k, red in enumerate(reds):
        if k < num_red_platoons:
            mat[red[0], red[1], 0] = 0.5
        else:
            mat[red[0], red[1], 0] = 1

    for k, blue in enumerate(blues):
        if k < num_blue_platoons:
            mat[blue[0], blue[1], 2] = 1
        else:
            mat[blue[0], blue[1], 2] = 0.5

    plt.title(f'scenario {scenario_id}')
    plt.tick_params(bottom=False, labelbottom=False)
    plt.imshow(mat)

    plt.savefig('nominal_scenarios', dpi=300)
    plt.show()


if __name__ == '__main__':
    main()
