"""
This file is used to store reward functions to be used in snake_env.py
"""

def basic_reward_func(reward_dict) -> float:
    """
    Basic reward function that rewards the snake for consuming a fruit, 
    punishes it for colliding with itself or a wall, and rewards nothing otherwise.

    reward_dict:
        did_consume_fruit: boolean representing whether a snake consumed a fruit in the last move
        did_collide_wall: boolean representing whether a snake collided with itself in the last move
        did_collide_body: boolean representing whether a snake collided with a wall in the last move

    output: 
        an integer representing a reward assigned to the snake agent based on the inputs provided
    """
    if reward_dict["did_consume_fruit"]:
        return 1
    elif reward_dict["did_collide_wall"] or reward_dict["did_collide_body"]:
        return -1
    else: 
        return 0

def basic_reward_func_with_move_ceiling(reward_dict) -> float:
    """
    Basic reward function that rewards the snake for consuming a fruit, 
    punishes it for colliding with itself or a wall, punishes it for running
    out of moves after not consuming a fruit, and rewards nothing otherwise.

    reward_dict:
        did_consume_fruit: boolean representing whether a snake consumed a fruit in the last move
        did_collide_wall: boolean representing whether a snake collided with itself in the last move
        did_collide_body: boolean representing whether a snake collided with a wall in the last move
        did_exceed_allowed_moves_no_fruit: boolean representing whether a snake has exceeded the number of allowable 
                                           moves without consuming a fruit

    output: 
        a float representing a reward assigned to the snake agent based on the inputs provided
    """
    if reward_dict["did_consume_fruit"]:
        return 10.0
    elif reward_dict["did_collide_wall"] or reward_dict["did_collide_body"]:
        return -1.0
    elif reward_dict["did_exceed_allowed_moves_no_fruit"]:
        return -5.0
    else: 
        return 0.0
    
def reward_closer_to_fruit(reward_dict) -> float:
    """
    Reward function that rewards the snake for consuming a fruit and getting closer to fruit,
    punishes it for colliding with itself or a wall, and rewards nothing otherwise.

    reward_dict:
        did_consume_fruit: boolean representing whether a snake consumed a fruit in the last move
        did_move_closer_to_fruit: boolean representing whether a snake moved closer to the fruit
        did_collide_wall: boolean representing whether a snake collided with itself in the last move
        did_collide_body: boolean representing whether a snake collided with a wall in the last move

    output: 
        an integer representing a reward assigned to the snake agent based on the inputs provided
    """
    if reward_dict["did_consume_fruit"]:
        return 10
    elif reward_dict["did_move_closer_to_fruit"]:
        return 1
    elif reward_dict["did_collide_wall"] or reward_dict["did_collide_body"]:
        return -1
    else: 
        return 0
