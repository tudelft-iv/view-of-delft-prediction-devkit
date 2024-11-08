# Benchmark instructions

## Submission rules

- The user can submit up to 25 proposed future trajectories, called modes, for each agent along with a probability the agent follows that proposal. Our metrics (explained below) will measure how well this proposed set of trajectories matches the ground truth.
- Up to half a second of past history can be used to predict the future trajectory for each agent.
- Top leaderboard entries and their papers will be manually reviewed to ensure no cheating was done.
- Each user or team can submit at most five results per month.
- Faulty submissions that return an error on Eval AI do not count towards the submission limit.


## Results format

Users must submit a json file with a list of Predictions for each agent. A Prediction has the following components:

```
instance: Instance token for agent.
sample: Sample token for agent.
prediction: Numpy array of shape [num_modes, n_timesteps, state_dim]
probabilities: Numpy array of shape [num_modes]
```

Each agent in VoD Prediction is indexed by an instance token and a sample token. As mentioned previously, num_modes can be up to 25. Since we are making 3 second predictions at 10 Hz, n_timesteps is 30. We are concerned only with x-y coordinates, so state_dim is 2. Note that the prediction must be reported in the global coordinate frame. Consult the baseline_model_inference script for an example on how to make a submission for two physics-based baseline models.

## Evaluation metrics

Below we define the metrics for the VoD prediction task.

### Minimum Average Displacement Error over k (minADE_k)

The average of pointwise L2 distances between the predicted trajectory and ground truth over the k most likely predictions.

### Minimum Final Displacement Error over k (minFDE_k)

The final displacement error (FDE) is the L2 distance between the final points of the prediction and ground truth. We take the minimum FDE over the k most likely predictions and average over all agents.

### Miss Rate At 2 meters over k (MissRateTopK_0.5_k)

If the maximum pointwise L2 distance between the prediction and ground truth is greater than 0.5 meters, we define the prediction as a miss. For each agent, we take the k most likely predictions and evaluate if any are misses. The MissRateTopK_0.5_k is the proportion of misses over all agents.
