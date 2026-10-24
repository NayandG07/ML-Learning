# Linear Regression from Scratch: Session Notes

## 1. Full Workflow Algorithm with Explanations
Linear Regression is a supervised learning algorithm used for predicting a continuous numerical value (like predicting house prices or temperature). 

### Key Terminology
- **`X` (Independent Variable / Features):** The data you already have and use to make a prediction (e.g., Square Footage of a house). It is "independent" because you aren't trying to change or predict it.
- **`y` (Dependent Variable / Target):** The value you are trying to predict. It is "dependent" because its value depends on what `X` is (e.g., House Price).

When trained using **Gradient Descent**, the workflow is as follows:

1. **Initialize Parameters:** 
   - **What:** Start with random or zero values for your weights ($w$) and bias ($b$).
   - **Why:** The model has to start somewhere. It initially guesses randomly, and then slowly corrects its guess over time.
2. **Forward Pass (Prediction):** 
   - **What:** For every data point $X$, calculate the model's current prediction: $y_{pred} = w \cdot X + b$
   - **Why:** We need to see what the model *currently* thinks the answers are so we can measure how wrong it is.
3. **Calculate Error (Cost Function):** 
   - **What:** Measure how far off the predictions are from the actual true values ($y$). We use Mean Squared Error (MSE).
   - **Why:** We need a single mathematical number that represents "how bad the model is currently doing." The goal is to make this number as close to 0 as possible.
4. **Calculate Gradients:** 
   - **What:** Determine the direction to change the parameters to minimize the error using calculus (derivatives).
     - $dw = \frac{1}{N} \sum 2 \cdot X \cdot (y_{pred} - y)$
     - $db = \frac{1}{N} \sum 2 \cdot (y_{pred} - y)$
   - **Why:** The gradient acts like a compass. If you are standing on a hill (high error), the gradient points in the direction of the steepest slope downhill (towards lower error).
5. **Update Parameters:** 
   - **What:** Adjust $w$ and $b$ by taking a small step downhill:
     - $w = w - (learning\_rate \cdot dw)$
     - $b = b - (learning\_rate \cdot db)$
   - **Why:** This actually moves our model closer to the correct answer. We subtract the gradient because the gradient points *up* the hill, and we want to go *down*.
6. **Repeat:** 
   - **What:** Loop through steps 2-5 for a set number of `iterations`.
   - **Why:** One step is rarely enough to find the bottom of the hill. We have to take many small steps until we finally reach the bottom (the minimum error).

---

## 2. Deep Dive: What is the Learning Rate?
The `learning_rate` (often represented by the Greek letter alpha, $\alpha$) is a **hyperparameter**. This means it's a setting you configure *before* the model runs, rather than something the model learns on its own.

It controls **how big of a step** the model takes during step 5 of the workflow.

### How it affects the model:
- **If the learning rate is too small (e.g., 0.0000001):** The model takes incredibly tiny steps. It will eventually find the right answer, but it will take millions of iterations and run very slowly.
- **If the learning rate is "just right" (e.g., 0.01):** The model takes perfectly sized steps and glides smoothly down to the minimum error in a reasonable amount of time.
- **If the learning rate is too big (e.g., 100):** The model takes massive, reckless steps. It might step completely over the minimum error, bounce up the other side of the hill, and actually get *worse* and *worse* until the numbers explode to infinity. (This is called "diverging").

---

## 3. Working with Real Datasets
If you download a real dataset (like a CSV file predicting house prices based on square footage), here is how you use your model with it:

1. **Load the Data:** Use a library like `pandas` to read the CSV file.
2. **Extract X and y:** 
   - `X` becomes the column you are using to predict (e.g., Square Footage). Convert it to a NumPy array.
   - `y` becomes the target column you want to guess (e.g., House Price). Convert it to a NumPy array.
3. **Train / Test Split (Crucial for preventing Overfitting!):**
   - If you test your model on the exact same data it was trained on, you don't know if it actually learned the underlying pattern, or if it just memorized the answers to the test. 
   - To prevent this, randomly split your data into a **Training Set** (e.g. 80%) to train the model, and a **Test Set** (e.g. 20%) that the model has never seen to test its true performance.
4. **Data Scaling:**
   - Real datasets have large numbers (a house might be 2,000 sq ft and cost $500,000). 
   - If you feed numbers this big into Gradient Descent without changing the learning rate, the gradients will explode to infinity.
   - You must **Normalize** or **Standardize** your `X` data so all the numbers are small (e.g., between -1 and 1). *Note: Calculate the mean/std ONLY on the training data, then use those numbers to scale both the training and test data!*
5. **Train, Predict, and Evaluate:**
   - Instantiate your model: `model = SimpleLinearRegression()`
   - Train it: `model.fit(X_train_scaled, y_train)`
   - Predict: `predictions = model.predict(X_test_scaled)`
   - Evaluate: Compare `predictions` to `y_test` using Regression metrics.

---

## 4. Pseudocode
```text
function train_linear_regression(X, y, learning_rate, iterations):
    N = length(X)
    w = 0
    b = 0
    
    loop for 'iterations' times:
        // 1. Predict
        y_pred = (w * X) + b
        
        // 2. Calculate raw error
        error = y_pred - y
        
        // 3. Calculate gradients
        dw = (1 / N) * sum(2 * X * error)
        db = (1 / N) * sum(2 * error)
        
        // 4. Update parameters
        w = w - (learning_rate * dw)
        b = b - (learning_rate * db)
        
    return w, b
```

---

## 5. Dry Run Simulation (Iteration 1)
**Given Data:**
- $X = [1, 2]$
- $y = [3, 5]$ (Target rule: $y = 2X + 1$)
- `learning_rate` = 0.1
- $N = 2$

**Initial State:** $w = 0, b = 0$

**1. Prediction ($y_{pred} = w \cdot X + b$):**
- `y_pred = [0, 0]`

**2. Error ($y_{pred} - y$):**
- `error = [0, 0] - [3, 5] = [-3, -5]`

**3. Gradients:**
- $dw = \frac{1}{2} \cdot ((2 \cdot 1 \cdot -3) + (2 \cdot 2 \cdot -5)) = \frac{-26}{2} = -13$
- $db = \frac{1}{2} \cdot ((2 \cdot -3) + (2 \cdot -5)) = \frac{-16}{2} = -8$

**4. Update Parameters:**
- $w = 0 - (0.1 \cdot -13) = +1.3$
- $b = 0 - (0.1 \cdot -8) = +0.8$

*(In one step, parameters jumped closer to the true answers of w=2, b=1)*

---
---

# Logistic Regression from Scratch: Session Notes

## 1. Intuition: What is Logistic Regression?
At its core, Logistic Regression is trying to find the **best possible line (or hyperplane)** that perfectly separates two different groups of data (e.g., Spam vs. Not Spam, Malignant vs. Benign). 

Imagine drawing a line down a piece of paper so that all the red dots are on one side, and all the blue dots are on the other. That line is your decision boundary.

## 2. Why use Logistic Regression for Classification?
Why can't we just use regular **Linear Regression** to classify things as 0 or 1?
1. **Unbounded Outputs:** Linear regression draws a straight line that goes from $-\infty$ to $+\infty$. If we are predicting a probability, getting an answer of `-1.5` or `3.2` makes absolutely no sense. Probabilities must strictly be between 0 and 1.
2. **Outlier Sensitivity:** Linear Regression gets heavily skewed by outliers. If you have an extreme data point, it drags the whole line with it, which completely ruins your decision boundary. 

Logistic Regression solves this by using the **Sigmoid function** to gently bend that straight line into an "S-shape" that is strictly bounded between 0 and 1, making it perfect for probabilities.

## 3. How does it learn? (The Algorithm)
Logistic Regression learns using **Gradient Descent**, exactly like Linear Regression, but with a different cost function. 

Instead of measuring the raw distance from the line (Mean Squared Error), it uses **Log Loss (Binary Cross-Entropy)**.
- If the true answer is `1` (Spam), and the model predicts `0.99` probability, the penalty is very small.
- If the true answer is `1` (Spam), and the model predicts `0.01` probability, the penalty explodes to a massive number.

By calculating the gradients (derivatives) of this Log Loss curve, the model figures out which way to tweak its weights to lower that massive penalty, slowly wiggling the decision boundary line until it separates the classes as best as it can.

---

## 4. Full Workflow Algorithm with Explanations
Logistic Regression is a supervised learning algorithm used for **binary classification** (predicting whether something belongs to class 0 or class 1). It builds directly on top of the concepts of Linear Regression.

When trained using **Gradient Descent**, the workflow is as follows:

1. **Initialize Parameters:** 
   - Start with weights ($w$) and bias ($b$) set to zero (or random values).
2. **Forward Pass (Prediction):** 
   - **Linear Model:** First, calculate the linear equation exactly like Linear Regression: $z = w \cdot X + b$
   - **Sigmoid Function:** Then, pass $z$ through the Sigmoid function to squash it into a probability between 0 and 1: $y_{pred} = \frac{1}{1 + e^{-z}}$
3. **Calculate Error (Cost Function):** 
   - Instead of Mean Squared Error, Logistic Regression uses **Log Loss (Binary Cross-Entropy)**. This heavily penalizes the model if it is confident but wrong (e.g., predicting 99% probability for class 1 when the true class is 0).
4. **Calculate Gradients:** 
   - Determine the direction to change the parameters. Mathematically, the derivative of Log Loss with the Sigmoid function simplifies beautifully to look almost identical to Linear Regression gradients:
     - $dw = \frac{1}{N} \cdot X^T \cdot (y_{pred} - y)$
     - $db = \frac{1}{N} \cdot \sum(y_{pred} - y)$
5. **Update Parameters:** 
   - Adjust $w$ and $b$ using the learning rate, just like Linear Regression:
     - $w = w - (learning\_rate \cdot dw)$
     - $b = b - (learning\_rate \cdot db)$
6. **Repeat:** 
   - Loop for a set number of `iterations` until the model learns the decision boundary.

---

## 2. Deep Dive: The Sigmoid Function and Decision Boundary

### The Sigmoid Function ($\sigma$)
To classify data, we need outputs between 0 and 1 (probabilities). A straight line ($z = w \cdot X + b$) can go to positive or negative infinity. 

The Sigmoid function, $\sigma(z) = \frac{1}{1 + e^{-z}}$, solves this:
- If $z$ is a large positive number, $e^{-z}$ approaches 0, so the result approaches $1/1 = 1$.
- If $z$ is a large negative number, $e^{-z}$ approaches infinity, so the result approaches $1/\infty = 0$.
- If $z = 0$, the result is exactly $0.5$.

### Decision Boundary
Once the model outputs a probability (e.g., 0.85), we need to turn it into a final class (0 or 1) during inference. We do this by applying a **threshold**:
- If $y_{pred} > 0.5$, classify as **1**
- If $y_{pred} \leq 0.5$, classify as **0**

---

## 3. Pseudocode
```text
class LogisticRegression:
    function init(learning_rate, iterations):
        self.learning_rate = learning_rate
        self.iterations = iterations

    function _sigmoid(z):
        return 1 / (1 + exp(-z))

    function fit(X, y):
        N = length(X)
        self.w = zeros(features)
        self.b = 0
        
        loop for 'iterations' times:
            // 1. Forward Pass
            z = (X * self.w) + self.b
            y_pred = self._sigmoid(z)
            
            // 2. Gradients
            dw = (1 / N) * dot_product(transpose(X), (y_pred - y))
            db = (1 / N) * sum(y_pred - y)
            
            // 3. Update parameters
            self.w = self.w - (self.learning_rate * dw)
            self.b = self.b - (self.learning_rate * db)

    function predict(X):
        z = (X * self.w) + self.b
        y_pred = self._sigmoid(z)
        
        // Apply threshold
        predictions = [1 if p > 0.5 else 0 for p in y_pred]
        return predictions
```
