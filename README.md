# social_simulator

This Project is using Python to simulate the impact of random chance and risk events on the accumulation of individual wealth.

Assumption：
  Every half year 20% of the risk event happend that the individual will lost 50% of the wealth.
  Every half year 30% of the chance even happened that the individual will have a chance to double the wealth.
  Every individual have the ability score (percentage of the chance to double the wealth when a change event shows up).
  The Ability score distribution follows a normal distribution with median 50 and 10 standard deviation and limited between 0-100
  Individual wealth loss and gain depends entirely on events and each individual automatically has 1024 wealth at the age of 20. 

Experiment:
  Each experiment will randomly generate 1000 individuals to form a society, and simulate their risk opportunities from 20 to 70 years old.
  After the experiment, a scatter diagram of wealth distribution and ability distribution will be displayed.
  After the experiment, the ability distribution bar chart will be displayed.
  After the experiment is over, the wealth trajectories of the wealthiest and lowest wealth people will be displayed, as well as their ability value and final amount of wealth.
  The experiment will analyze the distribution of wealth for all people at age 70, proportion of total wealth held by the wealthiest and share of total wealth held by the wealthiest 20%.
  
  
  
  
  
