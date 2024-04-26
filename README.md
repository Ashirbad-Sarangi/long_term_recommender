# Long Term Recommender

A long-term recommender system is a sophisticated algorithmic framework designed to provide personalized recommendations to users over an extended period. Unlike short-term recommenders, which may focus on immediate preferences or recent interactions, long-term recommenders take into account historical user behaviors and preferences to offer recommendations that align with users' evolving interests and needs.

These systems typically leverage large volumes of data, encompassing user interactions with items or content over time. This data can include a variety of signals, such as ratings, purchases, clicks, views, and other forms of user engagement. By analyzing this rich dataset, long-term recommenders strive to discern patterns and trends in user behavior, allowing them to make informed predictions about users' future preferences.


## Markov Decision Process

A Markov Decision Process (MDP) is a mathematical framework used to model decision-making problems where outcomes are influenced by both random events and the decisions made by an agent. At its core, an MDP consists of states, actions, transition probabilities, rewards, and policies. States represent the possible situations or conditions of the system, while actions denote the choices available to the decision-maker. Transition probabilities capture the likelihood of transitioning between states when specific actions are taken, reflecting the uncertainty inherent in the system's dynamics. Immediate rewards associated with actions in states guide the decision-making process, aiming to maximize long-term cumulative rewards. Policies define strategies for selecting actions in states to optimize overall performance. MDPs find applications in diverse fields, including robotics, economics, and artificial intelligence, offering a formal framework for modeling and solving sequential decision-making problems under uncertainty.

## Deep Reinforcement Learning

In the realm of long-term recommendation systems, Deep Reinforcement Learning (DRL) emerges as a potent methodology for optimizing sequential decision-making processes over extended periods. Within this framework, the recommendation process is conceptualized as an agent-environment interaction, where the agent—representing the recommender system—learns to make optimal recommendations through trial and error, aiming to maximize cumulative rewards over time. Key to this approach is the formulation of states, actions, and rewards: states encapsulate user and item contexts, actions denote potential recommendations, and rewards reflect the efficacy of these recommendations in achieving long-term user engagement or satisfaction. Utilizing deep neural networks, such as deep Q-networks (DQN) or policy gradients, the DRL agent learns a policy to navigate the recommendation space, leveraging historical interaction data to iteratively refine its decision-making strategy. While promising, deploying DRL-based long-term recommender systems requires careful consideration of training stability, scalability, and interpretability challenges, alongside robust evaluation methodologies. Yet, the potential benefits—such as enhanced adaptability to evolving user preferences and the discovery of novel recommendation strategies—underscore the significance of integrating DRL techniques into the fabric of long-term recommendation systems.

## Method Used 

In this repository, a deep reinforcement technique is used to make a long term recommender. Various other methods are used in its publications. It is based on this paper : 

Huang, L., Fu, M., Li, F., Qu, H., Liu, Y. and Chen, W., 2021. A deep reinforcement learning based long-term recommender system. Knowledge-Based Systems, 213, p.106706.
