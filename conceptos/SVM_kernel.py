import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

# Here I manullay entered a data that is not linearly seperable in 1D
x = np.array([1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30]).reshape(-1, 1)  # Replace YOUR_X_VALUES with your data
y = np.array([1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1])                 # Replace YOUR_Y_VALUES with your class labels

# Non-linear transformation to 2D, (squaring)
def transform_to_2d(X):
    return np.c_[X, X**2]

# Transforming data to 2D
X_transformed = transform_to_2d(x)

# Fitting SVM with a linear kernel in the transformed 2D space
svm = SVC(kernel='linear')
svm.fit(X_transformed, y)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 1D data plot
axes[0].scatter(x, np.zeros_like(x), c=y, cmap='bwr', edgecolors='k')
axes[0].set_title('Original 1D Data')
axes[0].set_xlabel('Feature')
axes[0].set_yticks([])

# 2D transformed data plot
axes[1].scatter(X_transformed[:, 0], X_transformed[:, 1], c=y, cmap='bwr', edgecolors='k')
axes[1].set_title('Transformed 2D Data')
axes[1].set_xlabel('Original Feature')
axes[1].set_ylabel('Transformed Feature (X^2)')

# Plotting the decision boundary in 2D
ax = axes[1]
xlim = ax.get_xlim()
ylim = ax.get_ylim()

xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T

# Getting the separating hyperplane
Z = svm.decision_function(xy).reshape(XX.shape)

# Plotting decision boundary and margins
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])

plt.tight_layout()
plt.show()