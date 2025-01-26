import matplotlib.pyplot as plt

def plot_window(samples,
                labels=None,
                predictions=None,
                nb_samples_to_plot=4):
    """
    Plot the samples, labels, and predictions for a given window.
    Labels and predictions are superposed and optional.
    We suppose that samples, labels, and predictions only have one feature.

    Parameters
    ----------
    samples: Tensor
        The weather data used for predictions.
        It corresponds to the previous steps.
    labels: Optional[Tensor]
        The true values.
    predictions: Optional[Tensor]
        The predicted values.
    nb_samples_to_plot: int
        The number of samples to plot.
    """
    # select elements to plot
    samples = samples[:nb_samples_to_plot, :]
    if labels is not None:
        labels = labels[:nb_samples_to_plot, :]
    if predictions is not None:
        predictions = predictions[:nb_samples_to_plot, :]

    pred_timesteps = 0 if predictions is None else predictions.shape[1]
    labels_timesteps = 0 if labels is None else labels.shape[1]

    # initiate figure
    fig, axes = plt.subplots(nrows=samples.shape[0], ncols=1, figsize=(10, 2 * samples.shape[0]))

    # plot samples
    for i, sample in enumerate(samples):
        ax = axes[i]
        ax.plot(range(-samples.shape[1], 0), sample, label="samples", color="b")

        # plot labels
        if labels is not None:
            ax.plot(range(0, labels.shape[1]), labels[i], label="labels", color="g")

        # plot predictions
        if predictions is not None:
            ax.plot(range(0, predictions.shape[1]), predictions[i], label="predictions", color="r")

        ax.set_xlabel("Time steps (hours)")
        ax.set_xticks(range(-samples.shape[1], max(pred_timesteps, labels_timesteps), 24))
        ax.legend()

    plt.tight_layout()
    plt.show()