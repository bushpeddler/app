"""
faction_governance.py - Handles faction proposals and player voting on economic policies.

This module allows factions to propose new trade policies and enables players to vote on them.
Each policy proposal is stored in the 'governance_policies' table with an initial vote count of zero.
"""

import sqlite3

def propose_policy(faction, policy):
    """
    Inserts a new policy proposal into the governance_policies table.

    Args:
        faction (str): The name of the faction proposing the policy.
        policy (str): The description of the proposed policy.

    Returns:
        str: A confirmation message that the policy was proposed.
    """
    query = """
        INSERT INTO governance_policies (faction, policy, votes)
        VALUES (?, ?, 0)
    """
    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()
        cursor.execute(query, (faction, policy))
        conn.commit()
    return f"📢 {faction} has proposed a new policy: {policy}"

def vote_on_policy(player_id, policy_id):
    """
    Registers a player's vote on a specific policy.

    Args:
        player_id (int): The ID of the player casting the vote.
        policy_id (int): The ID of the policy being voted on.

    Returns:
        str: A confirmation message that the vote was counted.
    """
    query = """
        UPDATE governance_policies
        SET votes = votes + 1
        WHERE id = ?
    """
    with sqlite3.connect("observer_protocol.db") as conn:
        cursor = conn.cursor()
        cursor.execute(query, (policy_id,))
        conn.commit()
    return "✅ Your vote has been counted!"