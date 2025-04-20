from collections import namedtuple
from enum import Enum
from itertools import batched

Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """
    active_agents = []
    updated_listing = list(agent_listing)

    for agent in updated_listing:
        if agent.category != Condition.DEAD and agent.category != Condition.HEALTHY:
            active_agents.append(agent)
    # If there's an uneven number of agents, the last agent will remain the same.
    if len(active_agents) % 2 != 0:
        active_agents = active_agents[:-1]
    
    if len(active_agents) == 0: 
        return updated_listing  
    
    agent_pairs = list(batched(active_agents, 2))
    for a, b in agent_pairs:
        if a.category == Condition.CURE and b.category == Condition.CURE:
            continue
        elif a.category == Condition.CURE and b.category == Condition.SICK:
            updated_listing[updated_listing.index(b)]= Agent(b.name, Condition.HEALTHY)
        elif a.category == Condition.CURE and b.category == Condition.DYING:
            updated_listing[updated_listing.index(b)] = Agent(b.name, Condition.SICK)
        elif a.category == Condition.SICK and b.category == Condition.CURE:
            updated_listing[updated_listing.index(a)] = Agent(a.name, Condition.HEALTHY)
        elif a.category == Condition.DYING and b.category == Condition.CURE:
            updated_listing[updated_listing.index(a)] = Agent(a.name, Condition.SICK)
        else:
            if a.category == Condition.SICK:
                updated_listing[updated_listing.index(a)] = Agent(a.name, Condition.DYING)
            elif a.category == Condition.DYING:
                updated_listing[updated_listing.index(a)] = Agent(a.name, Condition.DEAD)
            else:
                print("illegal state")
            if b.category == Condition.SICK:
                updated_listing[updated_listing.index(b)] = Agent(b.name, Condition.DYING)
            elif b.category == Condition.DYING:
                updated_listing[updated_listing.index(b)] = Agent(b.name, Condition.DEAD)
            else:
                print("illegal state")

    return updated_listing



# # Example usage
# Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
# Agent = namedtuple("Agent", ("name", "category"))

# agents = (
#         Agent("Alice", Condition.CURE),
#         Agent("Bob", Condition.SICK),
#         Agent("Charlie", Condition.DYING),
#         Agent("David", Condition.CURE),
#         Agent("Eve", Condition.HEALTHY),
#         Agent("Frank", Condition.SICK),
#         Agent("Grace", Condition.SICK),
#         Agent("Heidi", Condition.DYING),
#         Agent("Ivan", Condition.SICK),
#         Agent("Judy", Condition.SICK),
#         Agent("Karl", Condition.DYING),
# )

# print("starting")
# updated_agents = meetup(agents)
# for agent in updated_agents:
#     print(f"{agent.name}: {agent.category.name}")
