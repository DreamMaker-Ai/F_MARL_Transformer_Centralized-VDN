import numpy as np
import os
import re
import pickle
import matplotlib.pyplot as plt
from collections import deque
import json
from pathlib import Path


def make_scenario_graph(parent_dir):
    num_red_win_list = []
    num_blue_win_list = []
    num_no_contest_list = []

    num_alive_reds_ratio_list = []
    num_alive_blues_ratio_list = []

    remaining_red_effective_force_ratio_list = []
    remaining_blue_effective_force_ratio_list = []

    episode_rewards_list = []
    episode_lens_list = []
    episode_team_reward_list = []

    parent_dir = 'Before_finetuning/nominal_test_before_finetuning/'
    # file_dir = ['1', '2', '3', '4']
    file_dir = ['7', '8',]

    for file_name in file_dir:
        child_dir = parent_dir + 'scenario=' + file_name + '/result.json'

        with open(child_dir, 'r') as f:
            json_data = json.load(f)

            num_red_win_list.append(json_data['num_red_win'] / 100)
            num_blue_win_list.append(json_data['num_blue_win'] / 100)
            num_no_contest_list.append(json_data['no_contest'] / 100)

            num_alive_reds_ratio_list.append(json_data['num_alive_reds_ratio'])
            num_alive_blues_ratio_list.append(json_data['num_alive_blues_ratio'])

            remaining_red_effective_force_ratio_list. \
                append(json_data['remaining_red_effective_force_ratio'])
            remaining_blue_effective_force_ratio_list. \
                append(json_data['remaining_blue_effective_force_ratio'])

            episode_rewards_list.append(json_data['episode_rewards'])
            episode_lens_list.append(json_data['episode_lens'])
            episode_team_reward_list.append(json_data['episode_team_reward'])

    savedir = Path(__file__).parent / parent_dir
    if not os.path.exists(savedir):
        os.mkdir(savedir)

    x = file_dir

    plt.plot(x, num_red_win_list, color='r', marker='o', label='red win')
    plt.plot(x, num_blue_win_list, color='b', marker='o', label='blue win')
    plt.plot(x, num_no_contest_list, color='g', marker='s', label='no contest')
    plt.title('Red win / Blue win / No contest ratio')
    plt.xlabel('scenario id ')
    plt.ylabel('win ratio')
    plt.ylim(-0.05, 1.05)
    plt.minorticks_on()
    plt.legend()
    plt.grid()

    savename = 'win_ratio'
    plt.savefig(str(savedir) + '/' + savename + '.png', dpi=500)
    plt.show()

    plt.plot(x, num_alive_reds_ratio_list, color='r', marker='o', label='alive reds')
    plt.plot(x, num_alive_blues_ratio_list, color='b', marker='o', label='alive blues')
    plt.plot(x, remaining_red_effective_force_ratio_list,
             color='r', marker='o', label='reds force', linestyle='dashed')
    plt.plot(x, remaining_blue_effective_force_ratio_list,
             color='b', marker='o', label='blues force', linestyle='dashed')
    plt.title('Survive agents and Remaining forces ratio')
    plt.xlabel('scenario id')
    plt.ylabel('ratio')
    plt.ylim(-0.05, 1.05)
    plt.minorticks_on()
    plt.legend()
    plt.grid()
    # plt.yscale('log')

    savename = 'alive_agents_ratio'
    plt.savefig(str(savedir) + '/' + savename + '.png', dpi=500)
    plt.show()

    plt.plot(x, episode_team_reward_list, color='r', marker='o', label='average team reward')
    plt.plot(x, episode_rewards_list, color='m', marker='o', label='average episode reward',
             linestyle='dotted')
    plt.plot(x, episode_lens_list, color='b', marker='s', label='average episode length')

    plt.title('Average rewards and length of episodes')
    plt.xlabel('scenario id')
    plt.ylabel('rewards & length')
    plt.minorticks_on()
    plt.legend()
    plt.grid()

    savename = 'rewards_length'
    plt.savefig(str(savedir) + '/' + savename + '.png', dpi=500)
    plt.show()


def main():
    make_scenario_graph(parent_dir='Before')  # 'Before' or 'After'


if __name__ == '__main__':
    main()
