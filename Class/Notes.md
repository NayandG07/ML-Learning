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
3. **Data Scaling (Crucial for Gradient Descent!):**
   - Real datasets have large numbers (a house might be 2,000 sq ft and cost $500,000). 
   - If you feed numbers this big into Gradient Descent without changing the learning rate, the gradients will explode to infinity.
   - You must **Normalize** or **Standardize** your `X` data so all the numbers are small (e.g., between -1 and 1).
4. **Train and Predict:**
   - Instantiate your model: `model = SimpleLinearRegression()`
   - Train it: `model.fit(X_scaled, y)`
   - Predict: `model.predict(new_unseen_X_scaled)`

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
