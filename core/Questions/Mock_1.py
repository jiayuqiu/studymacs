"""
Secret Santa

Given a list of players, pair up players so that:

1. Each player gives a gift once
2. Each player receives a gift once
3. Players cannot give or receive to themselves
4. Selections must be random

Example input: ["Barney", "Wilma", "Fred", "Pebbles", "Bam Bam"]
Example output: [["Barney", "Wilma"], ["Fred", "Betty"], ["etc", "etc"]]
"""

import random
from copy import deepcopy


def go(players):
    send_list = deepcopy(players)
    receive_list = deepcopy(players)
    pair_list = []

    for _ in players:
        # randomly select one player to send a gift.
        send_random_id = random.randint(0, len(send_list) - 1)
        random_send_player = send_list[send_random_id]

        tmp_receive_list = [x for x in receive_list if x != random_send_player]
        if len(tmp_receive_list) == 0:
            # It is the same name with send and receive player
            # end the loop
            break

        # record the pair
        receive_random_id = random.randint(0, len(tmp_receive_list) - 1)
        random_receive_player = tmp_receive_list[receive_random_id]
        send_list.remove(random_send_player)  # remove element
        receive_list.remove(random_receive_player)
        pair_list.append([random_send_player, random_receive_player])

    return pair_list


# players = [
#     "Fred", "Wilma", "Barney", "Pebbles", "Bam Bam"
# ]

players = [
    "Fred", "Wilma", "Barney", "Pebbles"
]

while True:
    santas = go(players)
    if len(santas) != len(players):
        print(santas)
    else:
        print('the same')
