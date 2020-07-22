from kaggle_environments import make, evaluate
import numpy as np
import random


def main():

    # # Create the game environment
    # # Set debug=True to see the errors if your agent refuses to run
    # env = make("connectx", debug=True)

    # # List of available default agents
    # # print(list(env.agents))

    # # Two random agents play one game round
    # env.run([agent_007, "random"])

    # # Show the game
    # out = env.render(mode="ansi")
    # print(out)


    get_win_percentages(agent_007, "random", 1)


def get_win_percentages(agent1, agent2, n_rounds=100):
    # Use default Connect Four setup
    config = {'rows': 6, 'columns': 7, 'inarow': 4}
    # Agent 1 goes first (roughly) half the time
    outcomes = evaluate("connectx", [agent1, agent2], config, [], n_rounds)

    print(outcomes)

    # print("Agent 1 Win Percentage:", np.round(outcomes.count([1,-1])/len(outcomes), 2))
    # print("Agent 2 Win Percentage:", np.round(outcomes.count([-1,1])/len(outcomes), 2))
    # print("Number of Invalid Plays by Agent 1:", outcomes.count([None, 0]))
    # print("Number of Invalid Plays by Agent 2:", outcomes.count([0, None]))

# Selects random valid column
def agent_007(obs, config):
    # print("Observable")
    print(obs.board)
    # print(obs.mark)

    # print("Config")
    # print(config.columns)
    # print(config.rows)
    # print(config.inarow)

    valid_moves = [col for col in range(config.columns) if obs.board[col] == 0]
    return valid_moves[0]



if __name__ == '__main__':
    main()