from utils import make_test_results_graph_of_increase_number


def main():
    parent_dir = 'trial(max_steps=150)/'

    agent_type = 'platoons'
    make_test_results_graph_of_increase_number(agent_type, parent_dir)

    # agent_type = 'companies'
    # make_test_results_graph_of_increase_number(agent_type, parent_dir)

    agent_type = 'blue_platoons'
    make_test_results_graph_of_increase_number(agent_type, parent_dir)

    # agent_type = 'red_platoons'
    # make_test_results_graph_of_increase_number(agent_type, parent_dir)


if __name__ == '__main__':
    main()
