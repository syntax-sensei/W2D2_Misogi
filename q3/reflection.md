# Reflection: Perceptron From Scratch

### Initial vs. Final Predictions
At the start, the model's predictions were almost random due to randomly initialized weights. It could not distinguish apples from bananas effectively. After training, the model achieved close to 100% accuracy on the small dataset, showing that even a simple logistic model can learn well-separated data when properly trained.

### Learning Rate Impact
The learning rate was critical in achieving convergence. With a rate of 0.1, the model was able to steadily decrease the loss without overshooting. If the learning rate were too low, learning would have been extremely slow; if too high, it might have diverged. Finding the right learning rate was like adjusting a volume knob — too quiet (slow learning), too loud (instability), just right (fast and stable convergence).

### DJ-Knob / Child-Learning Analogy
Training this model reminded me of how a child learns — not all at once, but gradually adjusting based on feedback. The learning rate is like a DJ knob: if turned too far, the child overreacts to each example; if too soft, the child barely learns. This analogy helped me understand why tuning the learning rate is crucial in gradient descent.

### Takeaways
Building logistic regression from scratch deepened my understanding of the math behind AI. I now see how weights, bias, and the sigmoid function work together. Training over 500 epochs showed how loss and accuracy evolve, reinforcing the concepts of overfitting, convergence, and gradient-based optimization.
