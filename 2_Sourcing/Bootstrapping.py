"""
Bootstrapping: A Comprehensive Guide and Implementation

Bootstrapping is a powerful statistical resampling technique that allows us to:
1. Estimate the sampling distribution of a statistic
2. Calculate confidence intervals
3. Perform hypothesis testing
4. Assess model uncertainty

Key Concept: Bootstrap sampling involves repeatedly sampling WITH REPLACEMENT 
from the original dataset to create many "bootstrap samples" of the same size.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings('ignore')

class BootstrapAnalyzer:
    """
    A comprehensive class for performing various types of bootstrap analysis
    """
    
    def __init__(self, data, n_bootstrap=1000, random_state=42):
        """
        Initialize the Bootstrap Analyzer
        
        Parameters:
        -----------
        data : array-like
            The original dataset
        n_bootstrap : int
            Number of bootstrap samples to generate
        random_state : int
            Random seed for reproducibility
        """
        self.data = np.array(data)
        self.n_bootstrap = n_bootstrap
        self.random_state = random_state
        np.random.seed(random_state)
        
    def basic_bootstrap(self, statistic_func=np.mean):
        """
        Perform basic bootstrap resampling
        
        Parameters:
        -----------
        statistic_func : function
            Function to calculate the statistic (default: mean)
            
        Returns:
        --------
        bootstrap_statistics : array
            Array of bootstrap statistics
        """
        bootstrap_stats = []
        n = len(self.data)
        
        for i in range(self.n_bootstrap):
            # Sample with replacement
            bootstrap_sample = np.random.choice(self.data, size=n, replace=True)
            # Calculate statistic
            stat = statistic_func(bootstrap_sample)
            bootstrap_stats.append(stat)
            
        return np.array(bootstrap_stats)
    
    def confidence_interval(self, statistic_func=np.mean, confidence_level=0.95):
        """
        Calculate bootstrap confidence interval
        
        Parameters:
        -----------
        statistic_func : function
            Function to calculate the statistic
        confidence_level : float
            Confidence level (e.g., 0.95 for 95% CI)
            
        Returns:
        --------
        tuple : (lower_bound, upper_bound, bootstrap_stats)
        """
        bootstrap_stats = self.basic_bootstrap(statistic_func)
        
        alpha = 1 - confidence_level
        lower_percentile = (alpha/2) * 100
        upper_percentile = (1 - alpha/2) * 100
        
        lower_bound = np.percentile(bootstrap_stats, lower_percentile)
        upper_bound = np.percentile(bootstrap_stats, upper_percentile)
        
        return lower_bound, upper_bound, bootstrap_stats
    
    def bias_correction(self, statistic_func=np.mean):
        """
        Calculate bias-corrected bootstrap estimate
        
        Parameters:
        -----------
        statistic_func : function
            Function to calculate the statistic
            
        Returns:
        --------
        dict : Contains original estimate, bootstrap mean, bias, and corrected estimate
        """
        # Original statistic
        original_stat = statistic_func(self.data)
        
        # Bootstrap statistics
        bootstrap_stats = self.basic_bootstrap(statistic_func)
        bootstrap_mean = np.mean(bootstrap_stats)
        
        # Bias calculation
        bias = bootstrap_mean - original_stat
        
        # Bias-corrected estimate
        corrected_estimate = original_stat - bias
        
        return {
            'original_estimate': original_stat,
            'bootstrap_mean': bootstrap_mean,
            'bias': bias,
            'corrected_estimate': corrected_estimate,
            'bootstrap_stats': bootstrap_stats
        }
    
    def plot_bootstrap_distribution(self, statistic_func=np.mean, title="Bootstrap Distribution"):
        """
        Plot the bootstrap distribution
        """
        bootstrap_stats = self.basic_bootstrap(statistic_func)
        original_stat = statistic_func(self.data)
        
        plt.figure(figsize=(10, 6))
        plt.hist(bootstrap_stats, bins=50, alpha=0.7, density=True, color='skyblue', edgecolor='black')
        plt.axvline(original_stat, color='red', linestyle='--', linewidth=2, label=f'Original Statistic: {original_stat:.3f}')
        plt.axvline(np.mean(bootstrap_stats), color='green', linestyle='--', linewidth=2, 
                   label=f'Bootstrap Mean: {np.mean(bootstrap_stats):.3f}')
        
        plt.xlabel('Statistic Value')
        plt.ylabel('Density')
        plt.title(title)
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.show()

class ModelBootstrap:
    """
    Bootstrap methods for machine learning models
    """
    
    def __init__(self, X, y, model_class=LinearRegression, n_bootstrap=1000, random_state=42):
        """
        Initialize Model Bootstrap
        
        Parameters:
        -----------
        X : array-like
            Feature matrix
        y : array-like
            Target variable
        model_class : class
            Machine learning model class
        n_bootstrap : int
            Number of bootstrap samples
        random_state : int
            Random seed
        """
        self.X = np.array(X)
        self.y = np.array(y)
        self.model_class = model_class
        self.n_bootstrap = n_bootstrap
        self.random_state = random_state
        np.random.seed(random_state)
        
    def bootstrap_model_predictions(self, X_test):
        """
        Generate bootstrap predictions for uncertainty estimation
        
        Parameters:
        -----------
        X_test : array-like
            Test features
            
        Returns:
        --------
        predictions : array
            Bootstrap predictions (n_bootstrap x n_test_samples)
        """
        X_test = np.array(X_test)
        n_samples = len(self.X)
        predictions = []
        
        for i in range(self.n_bootstrap):
            # Bootstrap sample indices
            bootstrap_indices = np.random.choice(n_samples, size=n_samples, replace=True)
            
            # Bootstrap sample
            X_bootstrap = self.X[bootstrap_indices]
            y_bootstrap = self.y[bootstrap_indices]
            
            # Fit model and predict
            model = self.model_class()
            model.fit(X_bootstrap, y_bootstrap)
            pred = model.predict(X_test)
            predictions.append(pred)
            
        return np.array(predictions)
    
    def prediction_intervals(self, X_test, confidence_level=0.95):
        """
        Calculate prediction intervals using bootstrap
        
        Parameters:
        -----------
        X_test : array-like
            Test features
        confidence_level : float
            Confidence level
            
        Returns:
        --------
        dict : Contains mean predictions and confidence intervals
        """
        predictions = self.bootstrap_model_predictions(X_test)
        
        alpha = 1 - confidence_level
        lower_percentile = (alpha/2) * 100
        upper_percentile = (1 - alpha/2) * 100
        
        mean_pred = np.mean(predictions, axis=0)
        lower_bound = np.percentile(predictions, lower_percentile, axis=0)
        upper_bound = np.percentile(predictions, upper_percentile, axis=0)
        
        return {
            'mean_prediction': mean_pred,
            'lower_bound': lower_bound,
            'upper_bound': upper_bound,
            'all_predictions': predictions
        }

def demonstrate_bootstrapping():
    """
    Comprehensive demonstration of bootstrapping techniques
    """
    print("=" * 60)
    print("BOOTSTRAPPING DEMONSTRATION")
    print("=" * 60)
    
    # Generate sample data
    np.random.seed(42)
    sample_data = np.random.normal(50, 15, 100)  # Normal distribution with mean=50, std=15
    
    print(f"\n1. BASIC BOOTSTRAP ANALYSIS")
    print(f"Original sample size: {len(sample_data)}")
    print(f"Original sample mean: {np.mean(sample_data):.3f}")
    print(f"Original sample std: {np.std(sample_data, ddof=1):.3f}")
    
    # Initialize bootstrap analyzer
    bootstrap_analyzer = BootstrapAnalyzer(sample_data, n_bootstrap=1000)
    
    # Bootstrap confidence interval for mean
    lower, upper, bootstrap_means = bootstrap_analyzer.confidence_interval(np.mean, 0.95)
    print(f"\n95% Bootstrap Confidence Interval for Mean:")
    print(f"Lower bound: {lower:.3f}")
    print(f"Upper bound: {upper:.3f}")
    print(f"Bootstrap mean estimate: {np.mean(bootstrap_means):.3f}")
    
    # Bootstrap confidence interval for median
    lower_med, upper_med, bootstrap_medians = bootstrap_analyzer.confidence_interval(np.median, 0.95)
    print(f"\n95% Bootstrap Confidence Interval for Median:")
    print(f"Lower bound: {lower_med:.3f}")
    print(f"Upper bound: {upper_med:.3f}")
    print(f"Bootstrap median estimate: {np.mean(bootstrap_medians):.3f}")
    
    # Bias correction
    bias_results = bootstrap_analyzer.bias_correction(np.mean)
    print(f"\n2. BIAS CORRECTION ANALYSIS")
    print(f"Original estimate: {bias_results['original_estimate']:.3f}")
    print(f"Bootstrap mean: {bias_results['bootstrap_mean']:.3f}")
    print(f"Estimated bias: {bias_results['bias']:.3f}")
    print(f"Bias-corrected estimate: {bias_results['corrected_estimate']:.3f}")
    
    # Model bootstrap demonstration
    print(f"\n3. MODEL BOOTSTRAP DEMONSTRATION")
    
    # Generate regression data
    X = np.random.randn(100, 2)
    true_coefficients = [3, -2]
    y = X @ true_coefficients + np.random.randn(100) * 0.5
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Model bootstrap
    model_bootstrap = ModelBootstrap(X_train, y_train, LinearRegression, n_bootstrap=500)
    
    # Get prediction intervals
    pred_intervals = model_bootstrap.prediction_intervals(X_test, confidence_level=0.95)
    
    print(f"Test set size: {len(X_test)}")
    print(f"Mean prediction: {np.mean(pred_intervals['mean_prediction']):.3f}")
    print(f"Average prediction interval width: {np.mean(pred_intervals['upper_bound'] - pred_intervals['lower_bound']):.3f}")
    
    # Calculate coverage (how many true values fall within prediction intervals)
    coverage = np.mean((y_test >= pred_intervals['lower_bound']) & 
                      (y_test <= pred_intervals['upper_bound']))
    print(f"Prediction interval coverage: {coverage:.1%}")
    
    print(f"\n4. BOOTSTRAP APPLICATIONS")
    print("Bootstrap is useful for:")
    print("• Estimating confidence intervals when theoretical distributions are unknown")
    print("• Model validation and uncertainty quantification")
    print("• Bias correction of estimators")
    print("• Hypothesis testing with non-parametric methods")
    print("• Feature importance assessment in machine learning")
    print("• Time series analysis with block bootstrap")
    
    print(f"\n5. ADVANTAGES AND LIMITATIONS")
    print("Advantages:")
    print("• Non-parametric: No assumptions about underlying distribution")
    print("• Versatile: Works with any statistic")
    print("• Simple to implement and understand")
    print("• Provides uncertainty estimates")
    
    print("\nLimitations:")
    print("• Computationally intensive")
    print("• Assumes original sample is representative")
    print("• May not work well with very small samples")
    print("• Can be biased for extreme statistics")

def bootstrap_comparison_example():
    """
    Compare bootstrap results with theoretical results
    """
    print("\n" + "=" * 60)
    print("BOOTSTRAP vs THEORETICAL COMPARISON")
    print("=" * 60)
    
    # Generate data from known distribution
    np.random.seed(42)
    true_mean = 100
    true_std = 20
    sample_size = 50
    
    sample = np.random.normal(true_mean, true_std, sample_size)
    
    # Theoretical confidence interval for mean
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    se_mean = sample_std / np.sqrt(sample_size)
    
    # 95% CI using t-distribution
    t_critical = stats.t.ppf(0.975, df=sample_size-1)
    theoretical_lower = sample_mean - t_critical * se_mean
    theoretical_upper = sample_mean + t_critical * se_mean
    
    # Bootstrap confidence interval
    bootstrap_analyzer = BootstrapAnalyzer(sample, n_bootstrap=2000)
    bootstrap_lower, bootstrap_upper, _ = bootstrap_analyzer.confidence_interval(np.mean, 0.95)
    
    print(f"Sample size: {sample_size}")
    print(f"Sample mean: {sample_mean:.3f}")
    print(f"True population mean: {true_mean}")
    
    print(f"\nTheoretical 95% CI: [{theoretical_lower:.3f}, {theoretical_upper:.3f}]")
    print(f"Bootstrap 95% CI:   [{bootstrap_lower:.3f}, {bootstrap_upper:.3f}]")
    print(f"CI width difference: {abs((bootstrap_upper - bootstrap_lower) - (theoretical_upper - theoretical_lower)):.3f}")
    
    # Check if true mean is captured
    theoretical_captures = theoretical_lower <= true_mean <= theoretical_upper
    bootstrap_captures = bootstrap_lower <= true_mean <= bootstrap_upper
    
    print(f"\nTrue mean captured by theoretical CI: {theoretical_captures}")
    print(f"True mean captured by bootstrap CI: {bootstrap_captures}")

if __name__ == "__main__":
    # Run demonstrations
    demonstrate_bootstrapping()
    bootstrap_comparison_example()
    
    print(f"\n" + "=" * 60)
    print("BOOTSTRAP SUMMARY")
    print("=" * 60)
    print("Bootstrapping is a fundamental technique in modern statistics and machine learning.")
    print("It provides a way to estimate the sampling distribution of any statistic")
    print("without making strong parametric assumptions about the underlying population.")
    print("This makes it invaluable for uncertainty quantification and robust inference.")
