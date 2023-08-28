import numpy as np
import gym


class Config:
    def __init__(self):
        # Define simulation cond.
        self.show_each_episode_result = False  # mainly for debug
        self.draw_win_distributions = False  # mainly for debug
        self.max_episodes_test_play = 1000  # default=50 for training

        # Animation setting
        self.make_animation = False  # Use self.max_episodes_test_play=1

        # Time plot of a test setting
        self.make_time_plot = False  # Use self.max_episodes_test_play=1

        # Define environment parameters
        self.grid_size = 15  # default=20
        self.offset = 0  # blue-team offset from edges

        # Define gym spaces
        self.action_dim = 5
        self.action_space = gym.spaces.Discrete(self.action_dim)

        observation_low = 0.
        observation_high = 1.
        self.observation_channels = 6
        self.n_frames = 1
        self.observation_space = \
            gym.spaces.Box(low=observation_low,
                           high=observation_high,
                           shape=(self.grid_size,
                                  self.grid_size,
                                  self.observation_channels)
                           )

        # Neural nets parameters
        self.hidden_dim = 256
        self.key_dim = 128
        self.num_heads = 2

        self.dropout_rate = 0.2

        self.max_steps = 200  # Default = 150 for training, 200 for test

        # Define Lanchester simulation parameters
        self.threshold = 5.0  # min of forces R & B
        self.log_threshold = np.log(self.threshold)
        self.mul = 2.0  # Minimum platoon force = threshold * mul
        self.dt = .2  # Default=.2

        # Define possible agent parameters
        self.agent_types = ('platoon', 'company')
        self.agent_forces = (50, 150)

        # Define possible red / blue agent parameters
        self.red_platoons = None
        self.red_companies = None
        self.red_pos = None
        self.blue_platoons = None
        self.blue_companies = None
        self.blue_pos = None
        self.efficiencies_red = None
        self.efficiencies_blue = None

        """ Define scenario """
        self.read_test_scenario(scenario_id=1)

        # For paddiing of multi-agents, *3 for adding red agents
        self.max_num_red_agents = (self.red_platoons[1] + self.red_companies[1]) * 1

        # Red team TBD parameters
        self.R0 = None  # initial total force, set in 'generate_red_team'
        self.log_R0 = None
        self.num_red_agents = None  # set in 'define_red_team'
        self.num_red_platoons = None
        self.num_red_companies = None

        # Blue team TBD parameters
        self.B0 = None  # initial total force, set in 'generate_blue_team'
        self.log_B0 = None
        self.num_blue_agents = None  # set in 'define_blue_team'
        self.num_blue_platoons = None
        self.num_blue_companies = None

    def define_blue_team(self):
        """
        Called from reset
            self.num_blue_agents, self.num_blue_platoons, self.num_blue_companies
            will be allocated.
        """
        self.num_blue_platoons = \
            np.random.randint(
                low=self.blue_platoons[0],
                high=self.blue_platoons[1] + 1)

        self.num_blue_companies = \
            np.random.randint(
                low=self.blue_companies[0],
                high=self.blue_companies[1] + 1)

        self.num_blue_agents = self.num_blue_platoons + self.num_blue_companies

    def define_red_team(self):
        """
        Called from reset
            self.num_red_agents, self.num_red_platoons, self.num_red_companies
            will be allocated.
        """
        self.num_red_platoons = \
            np.random.randint(
                low=self.red_platoons[0],
                high=self.red_platoons[1] + 1)

        self.num_red_companies = \
            np.random.randint(
                low=self.red_companies[0],
                high=self.red_companies[1] + 1)

        self.num_red_agents = self.num_red_platoons + self.num_red_companies

    def reset(self):
        """
        Generate new config for new episode
        """
        self.define_blue_team()
        self.define_red_team()

    def read_test_scenario(self, scenario_id):
        if scenario_id == 0:
            self.red_platoons = (8, 8)  # num range of red platoons, default=(5,10)
            self.red_companies = (8, 8)  # num range of red companies, default=(5,10)
            self.red_pos = [[1, 1], [1, 7], [1, 13], [7, 1], [7, 13], [13, 1], [13, 7], [13, 13],
                            [0, 4], [0, 10], [4, 4], [4, 10], [10, 4], [10, 10], [14, 4], [14, 10]]

            self.blue_platoons = (8, 8)  # num range of blue platoons, default=(5,10)
            self.blue_companies = (8, 8)  # num range of blue companies, default=(5,10)
            self.blue_pos = [[3, 3], [3, 7], [3, 11], [7, 3], [7, 11], [11, 3], [11, 7], [11, 11],
                             [0, 7], [3, 5], [3, 9], [5, 0], [5, 3], [5, 11], [5, 14], [14, 7]]

            self.efficiencies_red = (0.4, 0.4)  # range
            self.efficiencies_blue = (0.4, 0.4)

        elif scenario_id == 1:
            self.red_platoons = (8, 8)  # num range of red platoons, default=(5,10)
            self.red_companies = (8, 8)  # num range of red companies, default=(5,10)
            self.red_pos = \
                [[1, 1], [1, 7], [1, 13], [7, 1], [7, 13], [13, 1], [13, 7], [13, 13],
                 [1, 2], [0, 8], [1, 12], [6, 2], [7, 12], [12, 2], [13, 8], [12, 12]]

            self.blue_platoons = (8, 8)  # num range of blue platoons, default=(5,10)
            self.blue_companies = (8, 8)  # num range of blue companies, default=(5,10)
            self.blue_pos = \
                [[5, 6], [5, 7], [5, 8], [7, 6], [7, 7], [7, 8], [9, 6], [9, 7],
                 [6, 6], [6, 7], [6, 8], [8, 6], [8, 7], [8, 8], [10, 6], [10, 7]]

            self.efficiencies_red = (0.4, 0.4)  # range
            self.efficiencies_blue = (0.4, 0.4)

        elif scenario_id == 2:
            self.red_platoons = (9, 9)  # num range of red platoons, default=(5,10)
            self.red_companies = (9, 9)  # num range of red companies, default=(5,10)
            self.red_pos = \
                [[5, 6], [5, 7], [5, 8], [7, 6], [7, 7], [7, 8], [9, 6], [9, 7], [9, 8],
                 [6, 6], [6, 7], [6, 8], [8, 6], [8, 7], [8, 8], [10, 6], [10, 7], [10, 8]]

            self.blue_platoons = (8, 8)  # num range of blue platoons, default=(5,10)
            self.blue_companies = (8, 8)  # num range of blue companies, default=(5,10)
            self.blue_pos = \
                [[1, 1], [1, 7], [1, 13], [7, 1], [7, 13], [13, 1], [13, 7], [13, 13],
                 [1, 2], [1, 8], [1, 12], [7, 2], [7, 12], [13, 2], [13, 8], [13, 12]]

            self.efficiencies_red = (0.4, 0.4)  # range
            self.efficiencies_blue = (0.4, 0.4)

        elif scenario_id == 3:
            self.red_platoons = (8, 8)  # num range of red platoons, default=(5,10)
            self.red_companies = (8, 8)  # num range of red companies, default=(5,10)
            self.red_pos = \
                [[1, 1], [1, 2], [5, 1], [5, 2], [9, 1], [9, 2], [13, 1], [13, 2],
                 [2, 1], [2, 2], [6, 1], [6, 2], [10, 1], [10, 2], [14, 1], [14, 2]]

            self.blue_platoons = (8, 8)  # num range of blue platoons, default=(5,10)
            self.blue_companies = (8, 8)  # num range of blue companies, default=(5,10)
            self.blue_pos = \
                [[1, 12], [1, 13], [5, 12], [5, 13], [9, 12], [9, 13], [13, 12], [13, 13],
                 [2, 12], [2, 13], [6, 12], [6, 13], [10, 12], [10, 13], [14, 12], [14, 13]]

            self.efficiencies_red = (0.4, 0.4)  # range
            self.efficiencies_blue = (0.4, 0.4)

        elif scenario_id == 4:
            self.red_platoons = (8, 8)  # num range of red platoons, default=(5,10)
            self.red_companies = (8, 8)  # num range of red companies, default=(5,10)
            self.red_pos = \
                [[1, 12], [1, 13], [5, 12], [5, 13], [9, 12], [9, 13], [13, 12], [13, 13],
                 [2, 12], [2, 13], [6, 12], [6, 13], [10, 12], [10, 13], [14, 12], [14, 13]]

            self.blue_platoons = (8, 8)  # num range of blue platoons, default=(5,10)
            self.blue_companies = (8, 8)  # num range of blue companies, default=(5,10)
            self.blue_pos = \
                [[1, 1], [1, 2], [5, 1], [5, 2], [9, 1], [9, 2], [13, 1], [13, 2],
                 [2, 1], [2, 2], [6, 1], [6, 2], [10, 1], [10, 2], [14, 1], [14, 2]]

            self.efficiencies_red = (0.4, 0.4)  # range
            self.efficiencies_blue = (0.4, 0.4)

        else:
            raise NotImplementedError()


if __name__ == '__main__':
    config = Config()

    for _ in range(3):
        config.reset()
